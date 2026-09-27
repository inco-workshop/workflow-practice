"""
Phase 4 Comparative Analysis: KRAS G12C ligand landscape 구조 비교

목적 (CLAUDE.md Phase 4):
 - 어떤 ligand가 동일 pocket을 사용하는가?
 - 어떤 residue와 상호작용하는가? (거리 기반 pocket-lining residue 식별)
 - Sotorasib(6OIM) 대비 switch-II loop conformation 차이 (PMID 40391409의 "5.6 A at residue 65" claim 독립 재확인)
 - RMC-6291(9BFX)의 결합 부위가 나머지와 구조적으로 다른 site인지 확인

입력: analysis/structures/{6OIM.pdb, 6UT0.pdb, 9DMM.cif, 9BFX.cif} (RCSB PDB에서 직접 다운로드한 원자료)
출력: analysis/results_structural_comparison.md (사람이 읽을 수 있는 표), 이 스크립트 자체(재실행 가능)

주의: 이 스크립트는 "Observation" 수준 evidence를 생성한다 (직접 좌표 계산).
      문헌의 해석(예: pocket 이름 "switch-II pocket")은 별도 literature evidence로 이미 확보되어 있으며,
      여기서는 그 문헌 주장을 좌표 수준에서 독립적으로 재확인/보강하는 것이 목적이다.
"""

import warnings
from pathlib import Path

import numpy as np
from Bio.PDB import PDBParser, MMCIFParser, Superimposer
from Bio.PDB.Polypeptide import is_aa

warnings.filterwarnings("ignore")

BASE = Path(__file__).parent
STRUCT_DIR = BASE / "structures"

STRUCTURES = {
    "sotorasib": {"id": "6OIM", "file": "6OIM.pdb", "format": "pdb",
                  "kras_chain_candidates": ["A"], "ligand_resname": None},
    "adagrasib": {"id": "6UT0", "file": "6UT0.pdb", "format": "pdb",
                  "kras_chain_candidates": ["A", "B", "C", "D"], "ligand_resname": None},
    "divarasib": {"id": "9DMM", "file": "9DMM.cif", "format": "cif",
                  "kras_chain_candidates": ["A"], "ligand_resname": None},
    "RMC-6291": {"id": "9BFX", "file": "9BFX.cif", "format": "cif",
                 "kras_chain_candidates": ["A", "C"], "ligand_resname": None},
}

EXCLUDE_HET = {"HOH", "GDP", "GNP", "MG", "GTP", "ACT", "ZN", "SO4", "PO4", "EDO", "GOL"}


def load_structure(info):
    path = STRUCT_DIR / info["file"]
    if info["format"] == "pdb":
        parser = PDBParser(QUIET=True)
    else:
        parser = MMCIFParser(QUIET=True)
    return parser.get_structure(info["id"], str(path))


def find_ligand_residues(structure):
    """HETATM residues excluding common crystallization additives / nucleotides."""
    found = []
    for model in structure:
        for chain in model:
            for res in chain:
                hetflag = res.id[0]
                if hetflag.startswith("H_") or (hetflag != " " and hetflag != "W"):
                    resname = res.resname.strip()
                    if resname not in EXCLUDE_HET and resname != "HOH":
                        found.append((chain.id, res))
        break  # first model only
    return found


def get_kras_ca_dict(structure, chain_ids):
    """Return {resseq: CA atom} for the first matching protein chain that looks like KRAS (~170 aa)."""
    model = next(iter(structure))
    for cid in chain_ids:
        if cid in model:
            chain = model[cid]
            ca = {}
            for res in chain:
                if is_aa(res, standard=True) and "CA" in res:
                    ca[res.id[1]] = res["CA"]
            if 100 < len(ca) < 200:
                return cid, ca
    # fallback: scan all chains for one with 100-200 CA atoms
    for chain in model:
        ca = {}
        for res in chain:
            if is_aa(res, standard=True) and "CA" in res:
                ca[res.id[1]] = res["CA"]
        if 100 < len(ca) < 200:
            return chain.id, ca
    raise ValueError("No KRAS-like chain found")


def pocket_residues(structure, chain_id, ligand_res, cutoff=4.5):
    """Residues (on the KRAS chain) with any atom within `cutoff` A of any ligand atom."""
    model = next(iter(structure))
    kras_chain = model[chain_id]
    ligand_atoms = list(ligand_res.get_atoms())
    contacts = set()
    for res in kras_chain:
        if not is_aa(res, standard=True):
            continue
        for atom in res:
            for lig_atom in ligand_atoms:
                if (atom.coord - lig_atom.coord).dot(atom.coord - lig_atom.coord) ** 0.5 <= cutoff:
                    contacts.add((res.id[1], res.resname))
                    break
            else:
                continue
            break
    return sorted(contacts)


def main():
    results = {}
    for name, info in STRUCTURES.items():
        struct = load_structure(info)
        chain_id, ca_dict = get_kras_ca_dict(struct, info["kras_chain_candidates"])
        ligands = find_ligand_residues(struct)
        # pick the ligand residue on/near the KRAS chain (largest non-excluded HETATM, or covalently linked to CYS12)
        results[name] = {
            "chain_id": chain_id,
            "ca_dict": ca_dict,
            "ligands_found": [(cid, r.resname, r.id) for cid, r in ligands],
            "struct": struct,
        }
        print(f"[{name} / {info['id']}] KRAS-like chain = {chain_id}, n_CA = {len(ca_dict)}")
        print(f"  HETATM (non-solvent/ion) residues found: {results[name]['ligands_found']}")

    # ---- Superimpose adagrasib & divarasib onto sotorasib using common CA residues 1-166 (core, excludes C-term tail) ----
    ref_name = "sotorasib"
    ref_ca = results[ref_name]["ca_dict"]
    core_range = range(1, 167)  # KRAS G-domain core, avoids flexible C-terminal residues

    print("\n=== Superposition onto sotorasib (6OIM) using core CA atoms (resid 1-166, excluding switch-I/II: 25-40, 57-75) ===")
    # exclude switch-I (25-40) and switch-II (57-76) from the superposition frame so we measure THEIR movement, not fit to them
    rigid_ids = [i for i in core_range if not (25 <= i <= 40) and not (57 <= i <= 76)]

    switch2_residue_of_interest = 65  # per PMID 40391409 claim (Ca of residue 65)

    comparison_rows = []
    for name in ["adagrasib", "divarasib", "RMC-6291"]:
        mobile_ca = results[name]["ca_dict"]
        common_ids = [i for i in rigid_ids if i in ref_ca and i in mobile_ca]
        if len(common_ids) < 20:
            print(f"  {name}: insufficient common rigid-core residues ({len(common_ids)}) for superposition — skipped")
            continue
        fixed_atoms = [ref_ca[i] for i in common_ids]
        moving_atoms = [mobile_ca[i] for i in common_ids]
        sup = Superimposer()
        sup.set_atoms(fixed_atoms, moving_atoms)
        rms_core = sup.rms

        # apply rotation/translation to ALL mobile CA atoms, then compare residue 65 (and switch-II range) to reference
        mobile_all_ids = sorted(mobile_ca.keys())
        mobile_coords = np.array([mobile_ca[i].coord for i in mobile_all_ids])
        rot, tran = sup.rotran
        mobile_transformed = mobile_coords @ rot + tran
        mobile_transformed_dict = dict(zip(mobile_all_ids, mobile_transformed))

        row = {"ligand": name, "core_superposition_rmsd_A": round(rms_core, 2), "n_core_atoms": len(common_ids)}
        if switch2_residue_of_interest in ref_ca and switch2_residue_of_interest in mobile_transformed_dict:
            d = np.linalg.norm(ref_ca[switch2_residue_of_interest].coord - mobile_transformed_dict[switch2_residue_of_interest])
            row["resid65_CA_delta_A_vs_sotorasib"] = round(float(d), 2)
        else:
            row["resid65_CA_delta_A_vs_sotorasib"] = "N/A (residue not resolved in one structure)"

        # switch-II loop-wide displacement (residues 57-76), where resolved in both
        deltas = []
        for i in range(57, 77):
            if i in ref_ca and i in mobile_transformed_dict:
                deltas.append(float(np.linalg.norm(ref_ca[i].coord - mobile_transformed_dict[i])))
        row["switchII_57_76_mean_CA_delta_A"] = round(float(np.mean(deltas)), 2) if deltas else "N/A"
        row["switchII_57_76_max_CA_delta_A"] = round(float(np.max(deltas)), 2) if deltas else "N/A"
        comparison_rows.append(row)
        print(f"  {name}: core RMSD={rms_core:.2f} A (n={len(common_ids)}); "
              f"resid65 CA delta vs sotorasib={row['resid65_CA_delta_A_vs_sotorasib']} A; "
              f"switch-II(57-76) mean/max delta={row['switchII_57_76_mean_CA_delta_A']}/{row['switchII_57_76_max_CA_delta_A']} A")

    # ---- Pocket residue identification per structure (KRAS chain residues within 4.5A of the largest non-solvent ligand) ----
    print("\n=== Pocket-lining residues (KRAS chain atoms within 4.5 A of inhibitor) ===")
    pocket_summary = {}
    for name, info in STRUCTURES.items():
        struct = results[name]["struct"]
        chain_id = results[name]["chain_id"]
        ligs = results[name]["ligands_found"]
        if not ligs:
            print(f"  {name}: no distinct inhibitor HETATM residue identified automatically")
            continue
        # choose the ligand with the most atoms (the small-molecule inhibitor, not ions)
        model = next(iter(struct))
        best = None
        best_natoms = 0
        for cid, resname, resid in ligs:
            res = model[cid][resid]
            n = len(list(res.get_atoms()))
            if n > best_natoms:
                best_natoms = n
                best = (cid, res, resname)
        if best is None:
            continue
        lig_chain, lig_res, resname = best
        contacts = pocket_residues(struct, chain_id, lig_res, cutoff=4.5)
        pocket_summary[name] = {"ligand_resname": resname, "ligand_chain": lig_chain, "contacts": contacts}
        contact_str = ", ".join(f"{rn}{rid}" for rid, rn in contacts)
        print(f"  {name} (ligand={resname} in chain {lig_chain}): {contact_str}")

    # ---- write markdown report ----
    out = BASE / "results_structural_comparison.md"
    with open(out, "w") as f:
        f.write("# Structural Comparison — Reproducible Analysis Output\n\n")
        f.write("생성 스크립트: `analysis/structural_comparison.py` (Biopython 기반, RCSB PDB 원자료 직접 파싱)\n\n")
        f.write("## 1. Superposition — switch-II loop displacement relative to sotorasib (6OIM)\n\n")
        f.write("Rigid-core superposition은 switch-I(25-40)/switch-II(57-76)를 제외한 KRAS G-domain 잔기로 수행하여, ")
        f.write("switch-II 영역 자체의 움직임을 측정 대상으로 남겼다.\n\n")
        f.write("| Ligand | Core superposition RMSD (A) | n core atoms | Residue 65 CA delta vs sotorasib (A) | Switch-II(57-76) mean/max CA delta (A) |\n")
        f.write("|---|---|---|---|---|\n")
        for row in comparison_rows:
            f.write(f"| {row['ligand']} | {row['core_superposition_rmsd_A']} | {row['n_core_atoms']} | "
                     f"{row['resid65_CA_delta_A_vs_sotorasib']} | {row['switchII_57_76_mean_CA_delta_A']} / {row['switchII_57_76_max_CA_delta_A']} |\n")
        f.write("\n## 2. Pocket-lining residues (KRAS chain, within 4.5 A of inhibitor heavy atoms)\n\n")
        f.write("| Ligand | Ligand residue code | KRAS chain | Contact residues (<=4.5 A) |\n")
        f.write("|---|---|---|---|\n")
        for name, d in pocket_summary.items():
            contact_str = ", ".join(f"{rn}{rid}" for rid, rn in d["contacts"])
            f.write(f"| {name} | {d['ligand_resname']} | {d['ligand_chain']} | {contact_str} |\n")
        f.write("\n## Notes / Limitations\n\n")
        f.write("- 이 수치는 각 PDB 엔트리의 asymmetric unit 중 첫 번째로 발견된 KRAS 유사 체인을 사용해 계산되었다 "
                "(예: 6UT0은 4개 체인 중 하나만 사용).\n")
        f.write("- Cutoff 4.5 A는 임의로 정한 접촉 기준이며, 문헌에서 사용하는 정의(예: 4.0 A heavy-atom contact)와 "
                "다를 수 있다. 절대적인 잔기 목록보다 '어떤 잔기가 반복적으로 나타나는가'에 집중해서 해석해야 한다.\n")
        f.write("- RMC-6291(9BFX)의 리간드-KRAS 접촉은 CypA 계면과는 별도로 계산되었으며, CypA 자체와의 접촉 잔기는 "
                "이 스크립트에서 별도로 산출하지 않았다 (필요 시 추가 분석 가능).\n")
        f.write("- 이 분석은 Observation 수준이며, 여기서 관찰된 거리 차이가 실제 binding affinity/potency 차이의 "
                "'원인'이라고 해석하지 않는다 (Inference와 분리).\n")
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()

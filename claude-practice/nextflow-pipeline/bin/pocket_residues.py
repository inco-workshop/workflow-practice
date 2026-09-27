#!/usr/bin/env python3
"""리간드와 접촉하는 KRAS 잔기(pocket-lining residue)를 계산한다.

analysis/structural_comparison.py의 pocket 계산 부분을 구조 하나 단위로 분리한 것이다.
결과는 TSV 한 파일로 출력하여 Nextflow process 사이에서 주고받을 수 있게 한다.
"""

import argparse
import warnings

from Bio.PDB import MMCIFParser, PDBParser
from Bio.PDB.Polypeptide import is_aa

warnings.filterwarnings("ignore")

# 결정화 첨가물·이온·뉴클레오타이드는 리간드 후보에서 제외한다
EXCLUDE_HET = {
    "HOH", "GDP", "GNP", "MG", "GTP", "ACT", "ZN", "SO4", "PO4", "EDO", "GOL",
}


def load_structure(path):
    parser = MMCIFParser(QUIET=True) if str(path).endswith(".cif") else PDBParser(QUIET=True)
    return parser.get_structure("structure", str(path))


def find_kras_chain(structure, chain_candidates):
    """KRAS로 보이는 사슬(잔기 100~200개)의 id와 CA atom 사전을 반환한다."""
    model = next(iter(structure))

    def ca_of(chain):
        return {res.id[1]: res["CA"] for res in chain if is_aa(res, standard=True) and "CA" in res}

    for cid in chain_candidates:
        if cid in model:
            ca = ca_of(model[cid])
            if 100 < len(ca) < 200:
                return cid, ca

    # 후보 사슬에서 못 찾으면 전체 사슬을 훑는다
    for chain in model:
        ca = ca_of(chain)
        if 100 < len(ca) < 200:
            return chain.id, ca

    raise ValueError("KRAS로 보이는 사슬을 찾지 못했습니다")


def find_inhibitor(structure):
    """가장 원자 수가 많은 비-용매 HETATM 잔기를 저해제로 본다."""
    model = next(iter(structure))
    best = None
    best_natoms = 0

    for chain in model:
        for res in chain:
            hetflag = res.id[0]
            if not (hetflag.startswith("H_") or hetflag not in (" ", "W")):
                continue
            resname = res.resname.strip()
            if resname in EXCLUDE_HET:
                continue
            natoms = len(list(res.get_atoms()))
            if natoms > best_natoms:
                best_natoms = natoms
                best = (chain.id, res, resname)

    return best


def contact_residues(structure, chain_id, ligand_res, cutoff):
    """리간드 원자로부터 cutoff 이내에 원자가 하나라도 있는 KRAS 잔기 목록."""
    model = next(iter(structure))
    kras_chain = model[chain_id]
    ligand_atoms = list(ligand_res.get_atoms())

    contacts = set()
    for res in kras_chain:
        if not is_aa(res, standard=True):
            continue
        for atom in res:
            if any((atom - lig) <= cutoff for lig in ligand_atoms):
                contacts.add((res.id[1], res.resname.strip()))
                break

    return sorted(contacts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--structure", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--chains", default="", help="세미콜론으로 구분한 KRAS 사슬 후보 (예: A;B)")
    ap.add_argument("--cutoff", type=float, default=4.5)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    chain_candidates = [c for c in args.chains.split(";") if c]

    structure = load_structure(args.structure)
    chain_id, _ = find_kras_chain(structure, chain_candidates)

    inhibitor = find_inhibitor(structure)
    if inhibitor is None:
        raise SystemExit(f"[{args.name}] 저해제로 볼 만한 HETATM 잔기를 찾지 못했습니다")

    _, ligand_res, ligand_resname = inhibitor
    contacts = contact_residues(structure, chain_id, ligand_res, args.cutoff)

    with open(args.out, "w") as fh:
        fh.write("ligand\tligand_resname\tkras_chain\tresidue_id\tresidue_name\n")
        for resid, resname in contacts:
            fh.write(f"{args.name}\t{ligand_resname}\t{chain_id}\t{resid}\t{resname}\n")

    print(f"[{args.name}] chain={chain_id} ligand={ligand_resname} contacts={len(contacts)}")


if __name__ == "__main__":
    main()

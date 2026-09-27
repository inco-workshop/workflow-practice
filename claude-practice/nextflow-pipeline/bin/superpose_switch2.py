#!/usr/bin/env python3
"""기준 구조에 중첩한 뒤 switch-II loop의 변위를 측정한다.

중첩(superposition)에는 switch-I(25-40)·switch-II(57-76)를 제외한 core 잔기만 사용한다.
그래야 switch 영역 자체의 움직임이 측정 대상으로 남는다.
"""

import argparse
import warnings

import numpy as np
from Bio.PDB import MMCIFParser, PDBParser, Superimposer
from Bio.PDB.Polypeptide import is_aa

warnings.filterwarnings("ignore")

CORE_RANGE = range(1, 167)      # KRAS G-domain core (유연한 C-말단 제외)
SWITCH1 = range(25, 41)
SWITCH2 = range(57, 77)
RESIDUE_OF_INTEREST = 65        # PMID 40391409가 지목한 잔기


def load_structure(path):
    parser = MMCIFParser(QUIET=True) if str(path).endswith(".cif") else PDBParser(QUIET=True)
    return parser.get_structure("structure", str(path))


def find_kras_ca(structure, chain_candidates):
    """KRAS로 보이는 사슬의 {잔기번호: CA atom} 사전을 반환한다."""
    model = next(iter(structure))

    def ca_of(chain):
        return {res.id[1]: res["CA"] for res in chain if is_aa(res, standard=True) and "CA" in res}

    for cid in chain_candidates:
        if cid in model:
            ca = ca_of(model[cid])
            if 100 < len(ca) < 200:
                return ca

    for chain in model:
        ca = ca_of(chain)
        if 100 < len(ca) < 200:
            return ca

    raise ValueError("KRAS로 보이는 사슬을 찾지 못했습니다")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reference", required=True)
    ap.add_argument("--mobile", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--chains", default="")
    ap.add_argument("--ref-chains", default="", help="기준 구조의 사슬 후보 (미지정 시 자동 탐색)")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    mobile_ca = find_kras_ca(load_structure(args.mobile),
                             [c for c in args.chains.split(";") if c])
    ref_ca = find_kras_ca(load_structure(args.reference),
                          [c for c in args.ref_chains.split(";") if c])

    # switch 영역을 뺀 core 잔기 중, 두 구조 모두에서 관측된 것만 중첩에 사용
    rigid_ids = [
        i for i in CORE_RANGE
        if i not in SWITCH1 and i not in SWITCH2 and i in ref_ca and i in mobile_ca
    ]

    if len(rigid_ids) < 20:
        raise SystemExit(f"[{args.name}] 중첩에 쓸 공통 core 잔기가 부족합니다 ({len(rigid_ids)}개)")

    sup = Superimposer()
    sup.set_atoms([ref_ca[i] for i in rigid_ids], [mobile_ca[i] for i in rigid_ids])
    rot, tran = sup.rotran

    # 중첩 변환을 mobile 구조 전체에 적용한 뒤 기준 구조와 비교
    moved = {i: atom.coord @ rot + tran for i, atom in mobile_ca.items()}

    if RESIDUE_OF_INTEREST in ref_ca and RESIDUE_OF_INTEREST in moved:
        delta65 = float(np.linalg.norm(
            ref_ca[RESIDUE_OF_INTEREST].coord - moved[RESIDUE_OF_INTEREST]
        ))
        delta65 = f"{delta65:.2f}"
    else:
        delta65 = "NA"

    deltas = [
        float(np.linalg.norm(ref_ca[i].coord - moved[i]))
        for i in SWITCH2
        if i in ref_ca and i in moved
    ]
    mean_delta = f"{np.mean(deltas):.2f}" if deltas else "NA"
    max_delta = f"{np.max(deltas):.2f}" if deltas else "NA"

    with open(args.out, "w") as fh:
        fh.write("ligand\tcore_rmsd_A\tn_core_atoms\tresid65_delta_A"
                 "\tswitchII_mean_delta_A\tswitchII_max_delta_A\n")
        fh.write(f"{args.name}\t{sup.rms:.2f}\t{len(rigid_ids)}"
                 f"\t{delta65}\t{mean_delta}\t{max_delta}\n")

    print(f"[{args.name}] core RMSD={sup.rms:.2f} A (n={len(rigid_ids)}), "
          f"resid65 delta={delta65} A, switch-II mean/max={mean_delta}/{max_delta} A")


if __name__ == "__main__":
    main()

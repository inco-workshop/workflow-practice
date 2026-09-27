#!/usr/bin/env python3
"""구조별 분석 결과를 모아 비교 리포트를 작성한다.

여러 구조에서 반복적으로 나타나는 pocket 잔기(consensus)를 뽑고,
switch-II 변위 표와 함께 하나의 markdown 문서로 정리한다.
"""

import argparse
from collections import defaultdict


def read_tsv(path):
    with open(path) as fh:
        lines = [line.rstrip("\n") for line in fh if line.strip()]
    if not lines:
        return []
    header = lines[0].split("\t")
    return [dict(zip(header, line.split("\t"))) for line in lines[1:]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pocket", nargs="+", required=True)
    ap.add_argument("--switch2", nargs="+", required=True)
    ap.add_argument("--reference", required=True)
    ap.add_argument("--cutoff", default="4.5")
    ap.add_argument("--out-report", required=True)
    ap.add_argument("--out-consensus", required=True)
    args = ap.parse_args()

    # ---- pocket 잔기 집계 ----
    pocket_by_ligand = {}
    ligand_resname = {}
    for path in args.pocket:
        rows = read_tsv(path)
        if not rows:
            continue
        name = rows[0]["ligand"]
        ligand_resname[name] = rows[0]["ligand_resname"]
        pocket_by_ligand[name] = {
            (int(r["residue_id"]), r["residue_name"]) for r in rows
        }

    residue_count = defaultdict(int)
    for residues in pocket_by_ligand.values():
        for residue in residues:
            residue_count[residue] += 1

    n_structures = len(pocket_by_ligand)
    consensus = sorted(residue_count.items(), key=lambda kv: kv[0][0])

    with open(args.out_consensus, "w") as fh:
        fh.write("residue_id\tresidue_name\tn_structures\tligands\n")
        for (resid, resname), count in consensus:
            ligands = ";".join(
                sorted(n for n, rs in pocket_by_ligand.items() if (resid, resname) in rs)
            )
            fh.write(f"{resid}\t{resname}\t{count}\t{ligands}\n")

    # ---- switch-II 변위 집계 ----
    switch_rows = []
    for path in args.switch2:
        switch_rows.extend(read_tsv(path))
    switch_rows.sort(key=lambda r: r["ligand"])

    # ---- 리포트 작성 ----
    with open(args.out_report, "w") as fh:
        fh.write("# KRAS G12C 구조 비교 — 파이프라인 출력\n\n")
        fh.write(f"- 기준 구조: **{args.reference}**\n")
        fh.write(f"- 접촉 기준 거리: {args.cutoff} A\n")
        fh.write(f"- 비교한 구조 수: {n_structures}\n\n")

        fh.write("## 1. Switch-II loop 변위 (기준 구조 대비)\n\n")
        fh.write("| Ligand | Core RMSD (A) | n core atoms | Residue 65 delta (A) "
                 "| Switch-II mean/max delta (A) |\n")
        fh.write("|---|---|---|---|---|\n")
        for row in switch_rows:
            fh.write(f"| {row['ligand']} | {row['core_rmsd_A']} | {row['n_core_atoms']} "
                     f"| {row['resid65_delta_A']} "
                     f"| {row['switchII_mean_delta_A']} / {row['switchII_max_delta_A']} |\n")

        fh.write("\n## 2. Pocket-lining residue\n\n")
        fh.write("| Ligand | Ligand resname | n residues |\n")
        fh.write("|---|---|---|\n")
        for name in sorted(pocket_by_ligand):
            fh.write(f"| {name} | {ligand_resname.get(name, 'NA')} "
                     f"| {len(pocket_by_ligand[name])} |\n")

        fh.write(f"\n### 모든 구조({n_structures}개)에서 공통으로 나타난 잔기\n\n")
        shared_all = [f"{rn}{rid}" for (rid, rn), c in consensus if c == n_structures]
        fh.write((", ".join(shared_all) if shared_all else "없음") + "\n")

        if n_structures > 2:
            threshold = n_structures - 1
            fh.write(f"\n### {threshold}개 이상의 구조에서 나타난 잔기\n\n")
            shared_most = [f"{rn}{rid}" for (rid, rn), c in consensus if c >= threshold]
            fh.write((", ".join(shared_most) if shared_most else "없음") + "\n")

        fh.write("\n## Notes / Limitations\n\n")
        fh.write("- 각 구조의 asymmetric unit 중 KRAS로 보이는 첫 번째 사슬만 사용했다.\n")
        fh.write(f"- 접촉 기준 {args.cutoff} A는 임의로 정한 값이며 문헌의 정의와 다를 수 있다.\n")
        fh.write("- 이 출력은 Observation 수준이며, 거리 차이가 binding affinity 차이의 "
                 "'원인'이라는 해석은 포함하지 않는다.\n")

    print(f"Wrote {args.out_report} and {args.out_consensus}")


if __name__ == "__main__":
    main()

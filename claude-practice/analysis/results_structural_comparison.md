# Structural Comparison — Reproducible Analysis Output

생성 스크립트: `analysis/structural_comparison.py` (Biopython 기반, RCSB PDB 원자료 직접 파싱)

## 1. Superposition — switch-II loop displacement relative to sotorasib (6OIM)

Rigid-core superposition은 switch-I(25-40)/switch-II(57-76)를 제외한 KRAS G-domain 잔기로 수행하여, switch-II 영역 자체의 움직임을 측정 대상으로 남겼다.

| Ligand | Core superposition RMSD (A) | n core atoms | Residue 65 CA delta vs sotorasib (A) | Switch-II(57-76) mean/max CA delta (A) |
|---|---|---|---|---|
| adagrasib | 0.61 | 127 | 4.55 | 2.06 / 5.0 |
| divarasib | 0.48 | 127 | 5.52 | 2.38 / 5.97 |
| RMC-6291 | 0.54 | 127 | 4.85 | 2.83 / 6.21 |

## 2. Pocket-lining residues (KRAS chain, within 4.5 A of inhibitor heavy atoms)

| Ligand | Ligand residue code | KRAS chain | Contact residues (<=4.5 A) |
|---|---|---|---|
| sotorasib | MOV | A | VAL9, GLY10, ALA11, CYS12, GLY13, LYS16, PRO34, THR58, ALA59, GLY60, GLN61, GLU62, GLU63, ARG68, ASP69, MET72, HIS95, TYR96, GLN99, ILE100, VAL103 |
| adagrasib | M1X | A | VAL9, GLY10, ALA11, CYS12, GLY13, LYS16, PRO34, THR35, THR58, ALA59, GLY60, GLN61, GLU62, GLU63, TYR64, ARG68, ASP69, MET72, PHE78, ASP92, HIS95, TYR96, GLN99, ILE100, ARG102, VAL103 |
| divarasib | A1AWR | A | VAL9, GLY10, ALA11, CYS12, GLY13, LYS16, PRO34, THR35, THR58, ALA59, GLY60, GLN61, GLU62, GLU63, TYR64, ARG68, ASP69, MET72, PHE78, LYS88, ASP92, HIS95, TYR96, GLN99, ILE100, ARG102, VAL103 |
| RMC-6291 | A1AOD | A | CYS12, TYR32, PRO34, THR35, ILE36, GLU37, ALA59, GLY60, GLN61, TYR64, MET67, TYR71 |

## Notes / Limitations

- 이 수치는 각 PDB 엔트리의 asymmetric unit 중 첫 번째로 발견된 KRAS 유사 체인을 사용해 계산되었다 (예: 6UT0은 4개 체인 중 하나만 사용).
- Cutoff 4.5 A는 임의로 정한 접촉 기준이며, 문헌에서 사용하는 정의(예: 4.0 A heavy-atom contact)와 다를 수 있다. 절대적인 잔기 목록보다 '어떤 잔기가 반복적으로 나타나는가'에 집중해서 해석해야 한다.
- RMC-6291(9BFX)의 리간드-KRAS 접촉은 CypA 계면과는 별도로 계산되었으며, CypA 자체와의 접촉 잔기는 이 스크립트에서 별도로 산출하지 않았다 (필요 시 추가 분석 가능).
- 이 분석은 Observation 수준이며, 여기서 관찰된 거리 차이가 실제 binding affinity/potency 차이의 '원인'이라고 해석하지 않는다 (Inference와 분리).

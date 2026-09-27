# Phase 4 — Comparative Analysis

작성일: 2026-08-27
상태: DRAFT — CHECKPOINT 2/3 사이. 아직 candidate ranking 없음 (Phase 5는 별도 승인 후 진행 예정).

이 문서는 CLAUDE.md §13에서 요구하는 비교 분석 질문에 대해, `analysis/structural_comparison.py`로 생성한
자체 좌표 계산 결과(`analysis/results_structural_comparison.md`)와 `02_evidence_table.md` / `03_ligand_landscape.md`의
문헌 evidence를 종합하여 답한다.

---

## Q1. 어떤 ligand가 동일 pocket을 사용하는가?

**Evidence**: PDB 6OIM(sotorasib), 6UT0(adagrasib), 9DMM(divarasib) 세 구조 모두에서, KRAS 사슬 중 리간드로부터 4.5 Å 이내에 있는 접촉 잔기 집합이 실질적으로 동일하다:

- 공통 핵심 잔기: Val9, Gly10, Ala11, Cys12, Gly13, Lys16, Pro34, Thr58, Ala59, Gly60, Gln61, Glu62, Glu63, Arg68, Asp69, Met72, **His95**, **Tyr96**, Gln99, Ile100, Val103
- Adagrasib/divarasib는 추가로 Thr35, Tyr64, Phe78, Asp92, Arg102와도 접촉 (사토라십보다 약간 넓은 footprint)

이는 세 화합물이 동일한 "switch-II pocket"을 사용한다는 기존 문헌 주장(Ostrem 2013, Ganguly & Yoo 2022 등, Literature Claim)을 **좌표 수준 Observation으로 독립 재확인**한 것이다.

반면 **RMC-6291(9BFX)**의 접촉 잔기(Cys12, Tyr32, Pro34, Thr35, Ile36, Glu37, Ala59, Gly60, Gln61, Tyr64, Met67, Tyr71)는 위 세 화합물과 겹치는 부분(Cys12, Pro34, Ala59, Gly60, Gln61, Tyr64 정도)이 있지만, His95/Tyr96/Gln99/Ile100/Val103 등 switch-II pocket의 "안쪽" 특징적 잔기가 전부 빠져 있다. → **RMC-6291은 동일 pocket이 아니라 부분적으로 겹치는 인접 표면을 이용하는 별개의 결합 부위**라는 해석이 가능하다(Inference, 좌표 관찰에 기반).

## Q2. 어떤 residue와 상호작용하는가? (Q1과 통합 답변, 위 목록 참고)

가장 눈에 띄는 것은 **His95와 Tyr96이 sotorasib/adagrasib/divarasib 세 구조 모두에서 공통 접촉 잔기로 확인**된다는 점이다. 이는 `03_ligand_landscape.md`에 기록된 문헌 근거(PMID 40640254: "His95 mutation negatively impacts... GDC-6036 [divarasib]"; "Tyr96 co-mutation reduces the affinity of both inhibitors")와 정확히 부합한다. 즉, MD 시뮬레이션 기반 논문이 예측한 resistance-관련 잔기가 실제 결정구조에서도 물리적으로 리간드와 접촉하는 pocket-lining residue임이 확인되어, **서로 다른 독립적 방법론(실험 결정구조 vs MD+biochemical assay)이 같은 잔기를 지목**하는 수렴적 증거(convergent evidence)를 이룬다.

## Q3. Covalent / non-covalent mechanism의 차이는 무엇인가?

- Sotorasib, adagrasib, divarasib, RMC-6291 **넷 다 Cys12에 covalent** 결합한다는 점은 동일하다(각 PDB 구조에서 리간드가 Cys12 근접/연결로 관찰됨). 즉 "covalent vs non-covalent"라는 축으로는 이 landscape 내에서 뚜렷한 대조군이 확보되지 않았다 — 이는 한계로 기록한다(순수 non-covalent G12C 특이적 임상후보는 이번 조사에서 확보하지 못함).
- 대신 **"어떤 상태(GDP-bound OFF vs GTP-bound ON)의 KRAS에 covalent 결합하는가"**라는 축에서 뚜렷한 차이가 나타난다: sotorasib/adagrasib/divarasib는 GDP 결합 구조로 관찰되고, RMC-6291는 GNP(비가수분해 GTP 유사체) 결합 구조로 관찰된다. 이는 RQ2에서 "binding mode 차이"를 논할 때 covalent 여부보다 더 중요한 구분축일 수 있다(Inference).

## Q4. Binding pose는 어떻게 다른가?

Sotorasib를 기준으로 나머지 구조를 core(비-switch 영역) 기준 중첩(superposition, RMSD 0.48–0.61 Å, n=127 Cα)한 뒤 switch-II loop(57–76)의 변위를 측정했다:

| Ligand | Residue 65 Cα 거리차 (Å) | Switch-II(57-76) 평균/최대 변위 (Å) |
|---|---|---|
| Adagrasib | 4.55 | 2.06 / 5.00 |
| Divarasib | 5.52 | 2.38 / 5.97 |
| RMC-6291 | 4.85 | 2.83 / 6.21 |

Divarasib의 5.52 Å는 문헌(PMID 40391409)이 보고한 "최대 5.6 Å" 수치와 거의 일치하여, **문헌 주장을 원자료로 독립 재현**했다. Adagrasib도 4.55 Å로 상당한 switch-II 재배치를 보이며, RMC-6291은 애초에 다른 site를 쓰므로 이 비교의 해석 자체가 제한적이다(같은 pocket 안에서의 conformational 차이가 아니라 애초에 다른 상태/부위 비교이기 때문).

**해석의 한계**: 이 수치는 asymmetric unit 내 첫 번째 체인만 사용했고, cutoff·정렬 방식이 논문 방법론과 정확히 같지 않을 수 있다. 따라서 "몇 Å 차이"라는 절대값보다 "sotorasib/adagrasib/divarasib 순으로 switch-II 변위가 커지는 경향이 있고, 이는 동일 방향의 문헌 보고와 일치한다"는 정성적 결론에 무게를 둔다.

## Q5. 구조적 차이가 activity 차이와 일관되는가?

- 부분적으로만 확인 가능하다. `02_evidence_table.md`/`03_ligand_landscape.md`에 기록된 정량 데이터는 화합물마다 assay 종류·세포주가 달라 (C4, Not directly comparable) 구조적 차이와 potency 차이를 직접 대응시킬 수 없다.
- 다만 **resistance mutation 민감도**는 구조와 일관된 설명이 가능하다: divarasib이 His95 mutation에 특히 민감하다는 문헌 보고(PMID 40640254)는, His95가 divarasib의 실제 pocket-lining residue임을 이번 분석이 확인함으로써 **구조적으로 타당한 설명**을 얻는다 (His95 자체가 사라지거나 바뀌면 접촉이 소실되므로).
- 이것은 Inference이지 activity 차이의 "증명"이 아니다 — His95 mutation이 실제로 결합력을 낮춘다는 것은 별도의 biochemical 실험(원 논문의 assay)에서 온 것이고, 이 구조 분석은 "왜 그럴듯한가"에 대한 구조적 근거를 더한 것뿐이다.

## Q6. Resistance와 관련된 차이가 보고되어 있는가?

- Tyr96, His95 공-변이(co-mutation)가 divarasib/olomorasib에 다르게 영향을 준다는 것이 `03_ligand_landscape.md`에 이미 기록되어 있다 (PMID 40640254). 이번 구조 분석은 His95/Tyr96가 sotorasib/adagrasib/divarasib 전체의 공통 pocket residue임을 보여주므로, **이 resistance mutation들이 divarasib 한 화합물만의 특수한 취약점이 아니라, switch-II pocket을 쓰는 계열 전체의 잠재적 공통 취약점일 가능성**을 시사한다(Hypothesis 수준 — olomorasib이 상대적으로 덜 민감하다는 보고와는 배치될 수 있어 추가 검증 필요).
- RMC-6291처럼 아예 다른 상태(GTP-bound)/다른 접촉 잔기 세트를 쓰는 화합물은 His95/Tyr96 유래 resistance에 원리적으로 덜 취약할 수 있다는 것이 구조적으로 그럴듯하지만(Hypothesis), 이번 조사에서 RMC-6291에 대한 resistance 데이터 자체는 확보하지 못했다(Not found) — 순수 추정이며 확인되지 않았음을 명시한다.

## Q7. 동일 assay 조건에서 비교할 수 있는 데이터가 있는가?

- 이번 세션에서 확보한 IC50/Kd 데이터는 화합물마다 다른 assay(사토라십: pERK/antiproliferation in MIAPaCa2; adagrasib/divarasib: 수치 미확보; olomorasib/divarasib: PMID 40640254의 "biochemical assay"는 정성적 서술만 확인)로, **동일 조건 비교가 가능한 데이터셋은 이번 조사에서 확보되지 않았다.** 이는 한계로 남긴다.

---

## Tool / Method 기록 (재현성)

- 구조 다운로드: `curl https://files.rcsb.org/download/{ID}.pdb` (6OIM, 6UT0) 및 `.cif` (9DMM, 9BFX — 신규 항목은 legacy PDB 포맷 미제공, mmCIF만 가능함을 확인)
- 분석 라이브러리: Biopython 1.88, numpy 2.5.2 (이번 세션에서 `pip install`로 설치)
- 스크립트: `analysis/structural_comparison.py` (Superimposer 기반 rigid-core 중첩 + NeighborSearch 없이 직접 거리 계산으로 pocket 잔기 산출)
- 원시 실행 로그와 표: `analysis/results_structural_comparison.md`

## 이번 Phase에서 새로 해소된 한계 (이전 evidence table 대비)

- `02_evidence_table.md` B6 ("Key residue 정보 없음")이 D3로 해소됨 — His95, Tyr96 등 residue-level 정보를 원자료 좌표에서 직접 확인.
- `03_ligand_landscape.md`의 "개별 residue 목록 미확보" 표시가 sotorasib/adagrasib/divarasib/RMC-6291 전체에 대해 해소됨.

## 여전히 남아있는 gap

- Olomorasib은 실험 구조 자체가 없어 이번 좌표 분석 대상에서 제외됨 (문헌이 명시한 한계, 여전히 미해결).
- RMC-6291의 CypA 쪽 접촉 잔기는 계산하지 않음 (KRAS 쪽만 계산).
- IC50/Kd의 동일 조건 비교는 여전히 불가능 (Q7).
- ToolUniverse는 이번 세션 내내 재연결되지 않음 — 이번 구조 분석은 전적으로 BioMCP(문헌/임상) + RCSB REST API(구조) + 자체 Biopython 계산으로 수행됨.

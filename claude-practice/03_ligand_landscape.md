# Ligand Landscape — Phase 3 (RQ2)

작성일: 2026-08-27
상태: DRAFT — CHECKPOINT 2 검토 전. 아직 candidate ranking 없음.

## 후보 선정 기준 (왜 이 리간드들을 비교 대상에 포함했는가)

검색 상위 결과라는 이유만으로 포함하지 않기 위해, 다음 기준으로 포함 이유를 명시한다.

1. **Sotorasib** — 이 연구의 reference drug (RQ1에서 이미 분석).
2. **Adagrasib (MRTX849)** — sotorasib과 함께 유일하게 KRAS G12C 표적으로 FDA 승인된 covalent 억제제. 동일한 switch-II pocket 기전을 공유하는지 직접 비교 가능.
3. **Divarasib (GDC-6036)** — 최근 발표된 고해상도 결정구조(PMID 40391409)가 sotorasib/adagrasib과 "동일 pocket이지만 switch-II loop conformation이 다르다"는 것을 직접 보고하여, 구조적 비교의 근거가 명확함. 임상시험에서 승인 약물보다 높은 반응률이 보고됨(review 수준 claim).
4. **Olomorasib (LY3537982)** — divarasib과 동일한 논문(PMID 40640254)에서 나란히 비교된 최신 세대 covalent 억제제. Resistance mutation(Tyr96, His95) 민감도가 divarasib과 다르게 보고되어 있어 selectivity/resistance 비교에 유용.
5. **RMC-6291 (Elironrasib)** — 나머지 4개와 근본적으로 다른 기전(GDP-bound switch-II pocket이 아니라 GTP-bound active state를 CypA와의 tri-complex로 표적)을 사용하는 것으로 ClinicalTrials.gov에 "KRAS G12C(ON) inhibitor"로 명시되어 있어, "covalent/non-covalent" 뿐 아니라 "inactive-state vs active-state targeting"이라는 중요한 대조축을 제공.

**이번 pass에서 深profile하지 않은 후보 (식별은 되었으나 근거 미확보 — 누락을 숨기지 않기 위해 명시)**:
- Garsorasib, Fulzerasib — BioMCP `search drug --target KRAS`로 식별됨 (ChEMBL/DrugBank 등록 확인). 미국 FDA 승인 기록은 조회되지 않음(Not found). 다른 지역(중국 NMPA 등) 승인 여부는 이번 세션에서 원자료로 확인하지 못했으므로 추측하여 기재하지 않음.
- Lonafarnib — target=KRAS로 검색되었으나 mechanism은 "Protein farnesyltransferase inhibitor"로, G12C pocket을 직접 표적하지 않는 별개 접근(RAS membrane localization 저해)이라 이번 landscape 비교에서 제외.
- ARS-853 / ARS-1620 (Ostrem 2013 계열 이후 세대 연구용 covalent tool compound) — switch-II pocket 발견 및 초기 최적화 과정에서 핵심적인 화합물이나, 이번 조사에서 구조/활성 데이터를 별도로 조회하지 못함 (시간/범위 제약). 후속 조사 대상으로 남김.

---

## Ligand Landscape Table

| Ligand | Target | Binding Mode | Pocket / Protein State | Key Residue(s) | Structure (PDB) | Activity | Development Status | Evidence ID |
|---|---|---|---|---|---|---|---|---|
| **Sotorasib** (AMG 510) | KRAS G12C | Covalent (irreversible), acrylamide–Cys12 | Switch-II pocket; GDP-bound (inactive/OFF) state only | **Cys12(covalent), Val9/Gly10/Ala11/Gly13/Lys16/Pro34/Thr58/Ala59/Gly60/Gln61/Glu62/Glu63/Arg68/Asp69/Met72/His95/Tyr96/Gln99/Ile100/Val103** — 4.5Å 이내 접촉 잔기, 자체 구조 분석으로 확인 (Phase 4, `analysis/results_structural_comparison.md`) | 6OIM (1.65 Å, KRAS G12C + AMG 510(PDB ligand code: MOV) covalent + GDP + Mg2+) | Cellular: pERK IC50 68 nM, antiproliferation IC50 5.0 nM (MIAPaCa2); G12S 세포주에서 36,500 nM | FDA 승인 (NSCLC, mCRC) | L-S1 (`02_evidence_table.md` 참고) |
| **Adagrasib** (MRTX849) | KRAS G12C | Covalent (irreversible), acrylamide–Cys12 | Switch-II pocket; GDP-bound (inactive/OFF) state | Cys12(covalent) + sotorasib과 거의 동일한 접촉 잔기 세트(Val9-Gly13, Lys16, Pro34, Thr35, Thr58-Glu63, Arg68, Asp69, Met72, Phe78, Asp92, **His95, Tyr96**, Gln99, Ile100, Arg102, Val103) — 자체 구조 분석(9UT0→6UT0)으로 확인 | 6UT0 (1.94 Å, KRAS G12C + MRTX849 covalent + GDP + Mg2+). 별도로 9O0R (1.81 Å, "wild-type KRAS (GDP-bound) + MRTX849") 존재 — WT 배경에서 non-covalent 유사 결합을 보인 구조로 추정되며, 이 구조의 결합이 covalent인지 여부는 이번 조사에서 확인하지 못함 (Not confirmed) | 정량 수치(IC50/Kd)는 이번 세션에서 ChEMBL API 반복 실패로 미확보 (아래 tool failure 참고). Fell et al. 2020 원문 abstract는 "potent, selective covalent inhibitor"로만 서술 (수치 없음) | FDA 승인 (2022-12-12, NSCLC) | L-S2 |
| **Divarasib** (GDC-6036) | KRAS G12C | Covalent (irreversible) | Switch-II pocket과 동일 부위에 결합하나, switch-II loop conformation이 sotorasib과 상당히 다름 — 문헌 보고 최대 5.6 Å(residue 65 Cα), **자체 좌표 계산으로 5.52 Å 독립 재확인**(Phase 4) | Cys12(covalent) + adagrasib과 거의 동일한 접촉 잔기(Val9-Gly13, Lys16, Pro34, Thr35, Thr58-Glu63, Tyr64, Arg68, Asp69, Met72, Phe78, Lys88, Asp92, **His95, Tyr96**, Gln99, Ile100, Arg102, Val103) — His95 mutation이 divarasib 결합력을 특히 저하시킨다는 문헌 보고(PMID 40640254)와 일관됨(His95가 실제 접촉 잔기로 확인됨) | 9DMM (1.79 Å, KRAS G12C + divarasib covalent + GDP + Mg2+) | "Enhanced covalent target engagement in vitro" 및 G12C에 대한 높은 특이성 보고(review 수준 claim, 수치 미확보); 임상에서 일부 경우 기존 승인 약물보다 높은 overall response rate 보고(review claim, 1차 임상 데이터 직접 대조 안 함) | 임상시험 진행 중 (late-stage clinical trials로 서술됨; 이번 세션에서 구체적 NCT/phase 직접 조회 안 함) | L-S3, L-S4 |
| **Olomorasib** (LY3537982) | KRAS G12C | Covalent(추정 — MD 시뮬레이션 기반, 실험적 co-crystal 구조는 이번 논문 시점 기준 공개되지 않음) | Switch-II pocket (SII-P)으로 추정; 실험 구조 부재로 "Observation"이 아닌 "Inference(MD 기반)"로 분류 | Tyr96 co-mutation 시 divarasib/olomorasib 모두 결합력 저하; His95 mutation은 divarasib에만 유의한 저하 유발, olomorasib은 상대적으로 덜 영향받음. 다른 RAS isoform의 G12C(HRAS/NRAS G12C 추정)에 대해서도 높은 활성 유지 — divarasib과의 selectivity 차이 | **없음 (Not found)** — PMID 40640254 원문이 명시적으로 "co-crystal structures... currently unavailable"라고 기술 | 생화학적 assay로 high affinity 확인(정성적 서술, 수치는 원문 확인 필요) | 임상시험 진행 중 (구체적 단계 이번 세션 미확인) | L-S5 |
| **RMC-6291** (Elironrasib) | KRAS G12C — **GTP-bound (active/ON) 상태 특이적** | Non-canonical: covalent bond to Cys12이지만, switch-II pocket이 아니라 **cyclophilin A(CypA) 표면을 화학적으로 재구성**하여 형성된 새로운 계면을 통해 CypA:drug:KRAS G12C **tri-complex**를 형성 | Active(GTP-bound) state 특이적 신생 계면 (switch-II pocket 아님) — GNP(비가수분해성 GTP 유사체) 결합 확인 | Cys12(covalent), Tyr32, Pro34, Thr35, Ile36, Glu37, Ala59, Gly60, Gln61, Tyr64, Met67, Tyr71 — **자체 구조 분석으로 확인(4.5Å 이내, KRAS 쪽 접촉만)**. Sotorasib/adagrasib/divarasib의 pocket 잔기 세트(His95, Tyr96, Gln99, Ile100, Val103 등)와 뚜렷이 다름 — switch-II pocket이 아닌 별개 site임을 좌표 수준에서 독립 확인. CypA 표면 잔기는 이번 분석에서 별도 산출 안 함 | 9BFX (1.4 Å, "Tri-complex of Elironrasib (RMC-6291), KRAS G12C, and CypA" — ligand GNP, Mg2+) | "Tumor regressions in multiple human cancer models" (Schulze & Lito 2023 abstract, 수치 미확보) | 임상시험 1상 (NCT05462717, Revolution Medicines 후원, active/not recruiting) — 미승인 | L-S6, L-S7 |

**Phase 4 구조 분석 근거**: 위 표의 굵게 표시된 residue 목록과 5.52 Å 수치는 문헌 인용이 아니라, RCSB PDB에서 직접 다운로드한 좌표(6OIM/6UT0/9DMM/9BFX)를 Biopython으로 파싱하여 자체 계산한 결과이다. 스크립트와 원본 출력은 `analysis/structural_comparison.py`, `analysis/results_structural_comparison.md` 참고. 상세 해석은 `analysis/04_comparative_analysis.md` 참고.

---

## Sotorasib 대비 비교 요약 (Comparative Notes — 아직 결론 아님, RQ2 서술 목적)

- **공유되는 기전 축 (4/5)**: Sotorasib, adagrasib, divarasib, (추정)olomorasib은 모두 Cys12에 covalent하게 결합하며 switch-II pocket(또는 그 추정 부위)을 이용해 KRAS G12C를 GDP-bound inactive 상태로 고정하는 것으로 보고됨. 이는 서로 독립적인 구조 논문(6OIM/6UT0/9DMM 각각 별도 PDB deposit)에서 관찰되어 재현성 있는 패턴으로 보인다.
- **구조적 차이가 존재함**: 같은 pocket을 쓰더라도 switch-II loop conformation은 화합물마다 다르다(divarasib vs sotorasib, 최대 5.6 Å 차이, PMID 40391409 직접 관찰). 이는 "같은 pocket = 동일한 결합"이 아님을 보여주는 직접적 evidence이며, binding pose 차이가 potency/selectivity/resistance profile 차이의 구조적 근거가 될 수 있다는 해석(Inference)은 가능하지만, 이 자체가 활성 차이를 증명하지는 않는다.
- **Resistance mutation 민감도 차이**: His95 mutation은 divarasib에는 유의한 영향을 주지만 olomorasib에는 상대적으로 덜 영향을 준다(PMID 40640254, MD+biochemical). Tyr96 mutation은 두 화합물 모두에 영향. → "동일 pocket을 쓰는 약물이라도 resistance mutation에 대한 취약성은 다를 수 있다"는 것을 시사하는 구체적 근거.
- **근본적으로 다른 기전 (1/5)**: RMC-6291은 GDP-bound switch-II pocket 접근이 아니라 GTP-bound active state를 CypA tri-complex로 표적한다. 이는 "resistance mechanism이 다를 가능성"을 시사하는 구조적 근거(9BFX, GNP 리간드 관찰)이지만, 이 구조적 차이가 실제 임상적 resistance 극복으로 이어지는지는 별도의 biochemical/clinical evidence가 필요하다 (현재는 확인 안 됨).
- **정량적 직접 비교의 한계**: 이번 세션에서 확보한 IC50/Kd 수치는 화합물마다 assay 종류(cellular pERK, antiproliferation 등)와 세포주가 다르고, adagrasib/divarasib/olomorasib의 수치는 아직 원자료로 직접 확보하지 못했다. 따라서 **potency 순위를 매기는 것은 현재 근거로는 "Not directly comparable"**로 처리한다.

---

## Tool / Data Access Failures (Phase 3 관련, 추가분)

| 시도 | 실패 내용 | 원인(추정) | 대응 |
|---|---|---|---|
| ChEMBL activity API — adagrasib (`molecule_chembl_id=CHEMBL4594350`) | HTTP 500 (재시도 2회, limit 20/5 모두 실패) | ChEMBL REST 서버 측 문제로 추정 (sotorasib 조회는 동일 엔드포인트 형식으로 성공했었음) | 미해결 — 정량 데이터를 문헌 abstract(정성적 서술)로 대체. 재시도 필요 항목으로 표시 |
| ChEMBL activity API — divarasib (`molecule_chembl_id=CHEMBL5095236`) | HTTP 500 | 상동 | 상동 |
| BioMCP `get drug RMC-6291` / `get drug elironrasib` | "No exact drug match" — 구조화 DB(DrugBank/MyChem)에 아직 미등재로 추정 | 개발 초기 단계 화합물이라 구조화 drug DB에 없을 가능성 | ClinicalTrials.gov trial record(NCT05462717)와 RCSB PDB(9BFX)로 대체 확인 |

---

## CHECKPOINT 2 관련 자체 점검

- 구조적 evidence(PDB)와 activity evidence가 혼동되지 않도록 표에서 분리했다.
- Biochemical과 cellular evidence 구분: 현재 확보된 수치는 대부분 cellular assay이며, 순수 biochemical Kd는 아직 없음 (sotorasib 포함 전체 landscape 공통 한계).
- 서로 다른 assay 조건의 IC50는 위 "정량적 직접 비교의 한계"에 명시한 대로 직접 순위 비교하지 않았다.
- Evidence가 부족한 candidate: adagrasib(정량 수치), olomorasib(구조 전체), RMC-6291(정량 수치, CypA residue 상세) — 모두 명시적으로 "Not found"/"미확보"로 표시함.

이 ligand landscape를 기반으로 RQ2 comparative analysis(Phase 4)와 candidate prioritization(Phase 5)으로 넘어가기 전에, 검토를 요청합니다.

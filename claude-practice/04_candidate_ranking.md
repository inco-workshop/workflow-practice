# Phase 5 — Candidate Prioritization

작성일: 2026-08-27
상태: DRAFT — **CHECKPOINT 3 대기 중. 아직 최종 candidate ranking(순위 결정)은 수행하지 않았다.**
(CLAUDE.md §16 규칙: "이 단계에서는 아직 최종 candidate ranking을 수행하지 않는다" → checkpoint 승인 후 순위화 진행)

---

## 0. 평가 기준 (candidate 결과를 보기 전에 먼저 정의함)

아래 기준은 지금까지 확보한 evidence 카테고리(`02_evidence_table.md`, `03_ligand_landscape.md`, `analysis/04_comparative_analysis.md`)를 반영하여 정의했다. **이 기준을 정의한 시점에는 아직 어떤 후보가 우선순위에서 앞서는지 계산하지 않았다.**

| # | 평가 영역 | 무엇을 보는가 | 근거 카테고리 |
|---|---|---|---|
| 1 | Target relevance | KRAS G12C를 직접·선택적으로 표적하는가 (WT/타 mutant 대비 selectivity) | A, B |
| 2 | Structural evidence quality | 실험적 co-crystal 구조가 존재하는가, pocket/residue가 직접 확인되었는가 | D |
| 3 | Binding mechanism differentiation | Sotorasib(reference) 대비 결합 상태(GDP/GTP)·pocket·covalent 여부가 기존 표준과 다른가 — "왜 새로 검증할 가치가 있는가"의 핵심 | B, D |
| 4 | Quantitative activity evidence | IC50/Kd 등 수치 데이터가 존재하고 assay 조건이 명시되어 있는가 | C |
| 5 | Cellular/biological evidence | Cellular assay 이상의 근거(동물모델 등)가 있는가 | E |
| 6 | Development stage / clinical evidence | 임상 진입 단계, 승인 여부, 기존 약물 대비 차별화 근거 | F |
| 7 | Resistance-related evidence | 알려진 resistance mutation에 대한 취약성/강건성 근거가 있는가 | Phase 4 comparative |
| 8 | Evidence completeness | 위 항목들 중 "Not found"로 남은 항목이 얼마나 많은가 (근거 공백 자체를 하나의 평가축으로 다룸) | 전체 |

**기준 선정 이유**: RQ3는 "후속 검증할 candidate hypothesis"를 요구하므로, 이미 완전히 검증되어 승인된 화합물(sotorasib, adagrasib)보다는 "**구조적으로 흥미롭거나 차별화되지만 아직 근거가 불완전한**" 화합물을 부각하는 기준(#3, #7, #8)에 의도적으로 비중을 두었다. 이는 "단순히 IC50이 가장 낮은 화합물을 추천"하는 방식과는 다른 접근이다.

**이 기준은 후보 평가 결과를 본 뒤 변경하지 않는다.** 변경이 필요하면 사유를 이 문서에 기록한다 (현재까지 변경 없음).

---

## 1. 평가 대상 범위에 대한 판단

- **Sotorasib, Adagrasib**: 이미 FDA 승인되어 임상적으로 검증된 약물이다. RQ3가 요구하는 "후속 검증이 필요한 candidate hypothesis"라는 틀에는 해당하지 않으므로, 이 둘은 **비교 기준선(baseline)**으로만 사용하고 candidate shortlist에서 제외한다. (이 판단 자체도 evidence 기반 판단이며 임의 배제가 아님을 명시)
- **Divarasib, Olomorasib, RMC-6291**: 아직 임상시험 단계이며 완전한 근거가 확보되지 않아 RQ3의 candidate hypothesis 틀에 부합한다. 이 셋을 shortlist로 다룬다.

---

## 2. Candidate Shortlist (Evidence → Interpretation → Limitation → Hypothesis)

### Candidate 1: Divarasib (GDC-6036)

**Evidence**
- 실험적 co-crystal 구조 확보 (PDB 9DMM, 1.79 Å; Fernando/Craven/Shokat, PMID 40391409, 원문 직접 확인).
- 자체 좌표 분석 결과, sotorasib/adagrasib와 동일한 pocket 잔기(Cys12, His95, Tyr96 등)를 공유하되 switch-II loop 위치가 sotorasib 대비 5.52 Å 변위 (자체 계산, `analysis/results_structural_comparison.md`).
- 문헌(review 수준): "enhanced covalent target engagement in vitro" 및 G12C에 대한 높은 specificity, 일부 경우 승인 약물보다 높은 overall response rate (PMID 40391409 abstract, 수치 미확보).
- His95 mutation이 divarasib 결합력을 특히 저하시킨다는 MD+biochemical 근거 (PMID 40640254) — 이번 자체 구조 분석에서 His95가 실제 pocket-lining residue임이 확인되어 구조적으로 일관됨.

**Interpretation**
- 동일한 switch-II pocket 계열 내에서 sotorasib/adagrasib보다 결합 pose가 다르고, in vitro 결합력이 강화되었다는 review-level 주장과, 그 결합력 차이가 특정 residue(His95) 의존적일 수 있다는 구조적 정합성이 함께 존재한다. 즉 "같은 기전 계열이지만 더 최적화된 버전"이라는 해석이 현재 근거로는 합리적이다.

**Limitation**
- "Enhanced potency"나 "높은 ORR" 주장은 review abstract 수준이며, 이번 세션에서 1차 임상 데이터(NCT 번호, 구체적 ORR/PFS 수치)를 직접 대조하지 못했다.
- 순수 biochemical IC50/Kd 수치를 ChEMBL API 반복 실패로 확보하지 못해 (tool failure, `03_ligand_landscape.md` 기록) sotorasib과의 정량적 potency 비교가 불가능하다.
- His95 mutation에 대한 취약성은 잠재적 resistance 약점으로 작용할 수 있다 — 즉 구조적 장점(향상된 결합)과 잠재적 약점(resistance 취약성)이 공존한다.

**Hypothesis**
- 현재 확보된 구조적 evidence(독립 재현된 pose 차이, 확인된 pocket 잔기)는 divarasib이 sotorasib/adagrasib와 기전적으로 연속선상에 있으면서도 결합 방식이 다르다는 것을 지지한다. 그러나 cellular/clinical 수준에서 실제 우위를 입증하려면 동일 조건 하 정량적 potency 비교와 1차 임상 데이터 확인이 필요한 **후속 검증 후보**로 제안한다.

---

### Candidate 2: Olomorasib (LY3537982)

**Evidence**
- 실험적 co-crystal 구조는 **존재하지 않음** (PMID 40640254 원문이 명시적으로 "currently unavailable"라고 기술 — Not found).
- 동일 논문에서 MD 시뮬레이션 + biochemical assay로 "high affinity for KRAS(G12C)" 확인 (수치는 원문 미확인).
- Tyr96 co-mutation은 divarasib과 마찬가지로 olomorasib 결합력도 저하시키나, **His95 mutation은 olomorasib에는 유의한 영향을 주지 않음** (divarasib과의 핵심 차별점).
- Olomorasib은 KRAS G12C뿐 아니라 **다른 RAS isoform의 G12C**(문헌에서 HRAS/NRAS G12C로 추정되나 원문에서 정확한 isoform 명시 여부는 이번 세션에서 재확인 못함)에도 높은 활성을 유지 — divarasib은 이 특성이 보고되지 않음.

**Interpretation**
- His95 저항성 mutation에 대한 상대적 강건성은, 만약 향후 sotorasib/adagrasib/divarasib 치료 후 His95 관련 resistance가 임상적으로 나타난다면 올로모라십이 대안이 될 수 있음을 시사하는 근거가 된다.
- Isoform-broad 활성은 selectivity 측면에서는 오히려 trade-off일 수 있다 (G12C-selectivity가 낮다는 뜻일 수도 있음) — 이는 장점과 단점 중 어느 쪽으로 해석할지 이 evidence만으로는 단정할 수 없다.

**Limitation**
- 구조 evidence가 전무하다 (Not found) — pocket/residue 상호작용에 대한 주장은 전부 MD 시뮬레이션(Inference)에 기반하며, 실험적으로 직접 관찰된 것이 아니다. 이번 자체 구조 분석(Phase 4)도 olomorasib에는 적용하지 못했다(입력 구조 부재).
- 정량 수치(IC50/Kd) 자체를 확보하지 못함.
- "다른 RAS isoform G12C에 대한 활성 유지"의 정확한 isoform과 수치를 원문에서 재확인하지 못함 — 이 claim은 abstract 요약 수준으로만 확인된 것이며 과대해석하지 않아야 한다.

**Hypothesis**
- His95 관련 resistance에 대한 상대적 강건성은, 구조가 확인되기 전까지는 **가설(Hypothesis)**로만 다뤄야 한다. 실험적 co-crystal 구조 확보와 정량적 biochemical 데이터 확인을 최우선 후속 검증 항목으로 제안한다. 현재로서는 "구조적 근거가 가장 약한" 후보이다.

---

### Candidate 3: RMC-6291 (Elironrasib)

**Evidence**
- 실험적 tri-complex 구조 확보 (PDB 9BFX, 1.4 Å — 이번 landscape 내 가장 높은 해상도; CypA:RMC-6291:KRAS G12C).
- GNP(비가수분해 GTP 유사체) 결합 확인 → **GTP-bound active state**를 직접 표적한다는 것이 구조적으로 명확히 관찰됨 (다른 후보들과 근본적으로 다른 축).
- 자체 구조 분석: KRAS 쪽 접촉 잔기(Cys12, Tyr32, Pro34, Thr35, Ile36, Glu37, Ala59, Gly60, Gln61, Tyr64, Met67, Tyr71)가 sotorasib/adagrasib/divarasib의 switch-II pocket 잔기 세트와 뚜렷이 다름 — "다른 site"라는 주장이 좌표 수준에서 확인됨.
- Schulze & Lito 2023 (Science, PMID 37590355) abstract: "tumor regressions in multiple human cancer models" (동물 모델 수준 evidence, 수치 미확보).
- ClinicalTrials.gov에 "KRAS G12C(ON) inhibitor"로 명시 (NCT05462717, Phase 1, active/not recruiting, Revolution Medicines 후원).

**Interpretation**
- GDP-bound 상태를 표적하는 4개 화합물과 달리 GTP-bound 상태를 직접 표적한다는 것은, switch-II pocket 계열 약물에 대한 resistance(예: nucleotide cycling 변화, GTP-bound 비율 증가로 인한 회피)가 발생한 경우에도 이론적으로 작동할 수 있는 **기전적으로 상호보완적인 옵션**이라는 해석을 가능하게 한다.
- His95/Tyr96 의존적 pocket을 사용하지 않으므로, 그 잔기의 mutation에 의한 resistance에는 원리적으로 덜 취약할 것이라는 추정이 구조적으로 그럴듯하다.

**Limitation**
- 이는 여전히 Phase 1 임상시험 단계이며, 안전성/PK/실제 임상 효능 데이터는 이번 세션에서 확보하지 못했다.
- "Resistance에 덜 취약할 것"이라는 해석은 구조적 그럴듯함(plausibility)일 뿐, 실제 resistance mutation panel에 대한 biochemical 데이터로 검증된 것이 아니다 (Not found — 순수 Hypothesis).
- Tri-complex 기전 자체가 CypA 발현 수준·조직 분포 등 새로운 변수를 도입하며, 이번 조사에서 CypA 쪽 접촉 잔기나 CypA 발현 관련 근거는 확보하지 않았다.
- 정량적 IC50/Kd, 동물 모델의 구체적 수치 모두 미확보.

**Hypothesis**
- 구조적으로 가장 차별화된 기전(active-state targeting)을 가지며, 이는 기존 4개 화합물이 공유하는 resistance 취약점(His95/Tyr96 pocket 의존성)을 우회할 수 있는 **가장 근본적으로 다른 대안**일 가능성을 제기한다. 그러나 임상적 근거가 가장 부족한 초기 단계이므로, "구조적으로 흥미롭지만 임상적으로는 가장 검증되지 않은" 후보로 분류하고, biochemical resistance panel 검증과 초기 임상 안전성/효능 데이터 확인을 최우선 후속 과제로 제안한다.

---

## 3. Missing Evidence Summary (후보별)

| Candidate | 확보된 강점 | 핵심 결여 evidence |
|---|---|---|
| Divarasib | 구조(실험), pose 차이 독립 재현, resistance 메커니즘 정합성 | 정량 IC50/Kd, 1차 임상 데이터 수치 |
| Olomorasib | Resistance 상대적 강건성(His95), broad isoform 활성 (모두 review 수준) | 실험 구조 전무, 정량 데이터 전무 |
| RMC-6291 | 가장 높은 해상도 구조, 기전적으로 가장 차별화됨, ClinicalTrials.gov 공식 기전 설명 | 임상 데이터, resistance panel 검증, 정량 데이터, CypA 쪽 상세 |

## 4. 아직 수행하지 않은 것

- 세 후보 간 명시적 순위(1위/2위/3위) 부여 — 기준별 점수화 또는 종합 판단은 **CHECKPOINT 3 승인 후** 진행 예정.
- Sotorasib/adagrasib 대비 "우수하다"는 결론 — 아직 내리지 않음 (정량 비교 불가능하므로).

---

## CHECKPOINT 3 — CANDIDATE REVIEW

- **Candidate shortlist**: Divarasib, Olomorasib, RMC-6291 (sotorasib/adagrasib는 이미 승인된 baseline으로 제외 — 근거는 §1 참고)
- **후보 선정 기준**: 위 §0의 8개 평가 영역 (candidate 결과를 보기 전에 먼저 정의함)
- **후보별 핵심 evidence**: §2 각 후보의 "Evidence" 항목 참고 (요약: divarasib=구조+pose차이 재현, olomorasib=resistance 강건성이나 구조 전무, RMC-6291=가장 차별화된 기전+최고해상도 구조)
- **후보별 missing evidence**: §3 표 참고
- **후보별 major limitation**: §2 각 후보의 "Limitation" 항목 참고 (공통: 정량 데이터 부족, 임상 1차 데이터 미확인)

**CHECKPOINT 3 승인됨** (사용자 확인, 2026-08-27) — 아래 §5에서 §0의 기준을 그대로 적용해 최종 순위를 산정한다. 기준은 후보 결과를 본 뒤 변경하지 않았다.

---

## 5. Final Ranking (§0 기준 적용)

### 5.1 기준별 평가 매트릭스 (High / Medium / Low / Not available — 후보 간 상대 비교이며 절대 점수 아님)

| # | 평가 영역 | Divarasib | Olomorasib | RMC-6291 |
|---|---|---|---|---|
| 1 | Target relevance (G12C 선택성) | High (review: G12C 대한 높은 specificity) | Medium (G12C 특이적이나 타 RAS isoform G12C에도 활성 — selectivity 폭이 다른 방향) | High (ClinicalTrials.gov가 명시적으로 "G12C(ON) inhibitor"로 규정) |
| 2 | Structural evidence quality | High (실험 co-crystal, 자체 좌표 분석 완료) | **Not available** (실험 구조 없음, MD 추정만) | High (실험 co-crystal, 최고 해상도 1.4Å, 자체 좌표 분석 완료) |
| 3 | Binding mechanism differentiation (가중 기준) | Medium (같은 pocket, pose 차이는 독립 재현했으나 "새로운 기전"은 아님) | Low/Unknown (기전 자체가 구조로 확인 안 됨) | **High** (GDP→GTP-bound 표적 전환, tri-complex — 이 landscape에서 유일하게 근본적으로 다른 기전) |
| 4 | Quantitative activity evidence | Low (이번 세션 미확보) | Low (정성적 서술만) | Low (이번 세션 미확보) |
| 5 | Cellular/biological evidence | Low (in vitro engagement 강화 claim만, 수치 없음) | Low (biochemical assay만 언급) | Medium (동물모델 tumor regression 보고, 그러나 수치 없음) |
| 6 | Development stage / clinical evidence | Medium-High (late-stage clinical, review에서 ORR 우위 시사 — 단 1차 데이터 미확인) | Medium (임상 진행 중, 단계 미확인) | Low (Phase 1, 가장 초기 단계) |
| 7 | Resistance-related evidence (가중 기준) | Medium (His95 취약성이 **구체적으로 확인**됨 — 약점이지만 "evidence 있음") | Medium-High (His95에 상대적으로 강건하다는 근거 있음 — 단, 구조로 뒷받침되지 않음) | Low (이론적 plausibility만 있고 실측 resistance panel 데이터 없음 — Hypothesis 수준) |
| 8 | Evidence completeness | Medium (구조+일부 기전 확보, 정량/1차 임상 결여) | Low (구조 자체가 없어 결여 항목이 가장 많음) | Medium (구조는 최상급이나 임상/정량 데이터 결여) |

### 5.2 순위 산정 논리

이 매트릭스에서 세 후보는 서로 다른 축에서 강점을 가지므로, 단순 합산 점수화는 서로 다른 종류의 evidence(구조적 확실성 vs 임상 성숙도 vs resistance 가설)를 부적절하게 동일 가중치로 합치는 것이라 판단하여 **하지 않는다**. 대신 §0에서 사전에 명시한 가중 기준(#3 기전 차별화, #7 resistance evidence)을 우선 적용하고, 나머지 기준으로 동점을 해소하는 방식으로 순위를 산정한다.

1. **#3(기전 차별화)에서 RMC-6291이 유일하게 "High"** — 사전에 이 기준에 가중치를 두기로 했으므로, RMC-6291이 "가장 우선 검증할 가치가 있는 구조적 근거"를 갖는다는 결론이 자연스럽게 따라온다. 다만 #6(개발 단계)과 #7(resistance 실측 데이터)에서 가장 약하므로, "최우선 순위"가 "가장 먼저 임상적으로 성공할 후보"를 의미하지는 않는다.
2. **Divarasib은 #2(구조)와 #6(임상 성숙도)에서 가장 균형 잡힌 evidence**를 가지며, #7에서도 (약점이지만) 구체적으로 특성화된 resistance 데이터를 보유한다 — "지금 당장 추가 실험으로 결론을 낼 수 있는 후보"로서의 실행 가능성(actionability)이 가장 높다.
3. **Olomorasib은 #7에서 흥미로운 신호(His95 강건성)를 보이지만, #2(구조 자체 부재)와 #8(전반적 결여)이 가장 취약**하여, 다른 두 후보와 동등하게 비교하기에는 근거 기반이 아직 너무 얇다.

### 5.3 제안하는 우선순위 (순위가 아니라 "왜 검증하는가"가 다름을 강조)

| 순위 | Candidate | 우선 검증 사유 (한 줄) |
|---|---|---|
| 1 | **RMC-6291 (Elironrasib)** | 이 landscape에서 유일하게 기전적으로 근본적으로 다른 후보(GTP-bound 표적) — His95/Tyr96 의존적 resistance를 우회할 잠재력이 가장 크다는 가설을 검증할 가치가 최우선. 단, 임상 근거는 가장 미성숙. |
| 2 | **Divarasib (GDC-6036)** | 구조·기전·임상 성숙도 균형이 가장 좋아 "다음 실험/데이터 확인으로 바로 결론을 강화할 수 있는" 실행 가능성이 가장 높음. His95 취약성이라는 구체적 검증 대상도 이미 식별됨. |
| 3 | **Olomorasib (LY3537982)** | His95 강건성이라는 흥미로운 신호가 있으나, 실험 구조 자체가 없어 다른 두 후보와 동일 선상에서 비교하기 어려움 — 구조 확보가 선행되어야 순위 재평가 가능. |

**중요한 재해석 주의사항**: 이 순위는 "어떤 화합물이 더 나은 신약이 될 것인가"에 대한 예측이 아니다. §0에서 사전에 정의한, 이 프로젝트의 evidence 상태를 반영한 8개 기준(특히 기전 차별화·resistance 축에 가중)을 적용한 결과이며, 만약 "가장 빠르게 실행 가능한 후속 검증"을 최우선 기준으로 삼았다면 divarasib이 1순위가 되었을 것이다. 이 tension을 숨기지 않고 명시한다.

---

## 6. Final Conclusion 표현 (CLAUDE.md §20 규칙 적용)

**피해야 할 표현의 예**: "RMC-6291은 sotorasib보다 우수한 차세대 KRAS G12C 신약이다." (X — 근거 없음)

**이 문서가 실제로 주장하는 것**:
> 현재 확보된 구조적 evidence(실험 co-crystal, 독립적으로 재계산한 pocket 잔기 및 결합 상태)를 기준으로, RMC-6291(Elironrasib)을 "switch-II pocket 계열 약물과 기전적으로 구별되는, resistance 우회 가능성을 검증할 최우선 candidate hypothesis"로 제안한다. 다만 정량적 activity, resistance panel 실측 데이터, 임상 유효성 데이터가 모두 결여되어 있어, 이는 **후속 biochemical/clinical validation이 반드시 필요한 탐색적(exploratory) 가설**이며 확정된 우수성 주장이 아니다.
>
> Divarasib은 구조·기전·임상 성숙도가 가장 균형 잡혀 있어 실행 가능성이 높은 **2차 우선 검증 후보**로 제안하며, His95 관련 resistance 취약성이 구체적 검증 대상으로 이미 식별되어 있다.
>
> Olomorasib은 resistance 강건성이라는 흥미로운 신호가 있으나 구조적 근거가 전무하여, 다른 두 후보와 동등하게 비교하기 위해서는 **실험적 co-crystal 구조 확보가 선행되어야 하는 후보**로 분류한다.

이제 Phase 6 (Verification Audit, `05_verification_audit.md`) — 핵심 claim들을 CLAUDE.md §17의 10개 검증 질문에 따라 재점검 — 로 진행해도 될까요?

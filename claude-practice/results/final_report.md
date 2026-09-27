# Final Report: KRAS G12C 신약 후보 탐색 (Sotorasib을 출발점으로)

작성일: 2026-08-27
근거 파일: `01_research_plan.md`, `02_evidence_table.md`, `03_ligand_landscape.md`, `analysis/04_comparative_analysis.md`, `04_candidate_ranking.md`, `05_verification_audit.md`

---

## 1. Research Question

- **RQ1 (Mechanism)**: KRAS G12C는 왜 약물 표적이 될 수 있으며, sotorasib은 어떤 분자적·구조적 기전으로 KRAS G12C를 억제하는가?
- **RQ2 (Ligand Landscape)**: KRAS G12C에 결합하는 알려진 리간드들은 무엇이며, sotorasib과 비교했을 때 결합 방식과 약리학적 특성이 어떻게 다른가?
- **RQ3 (Candidate Discovery)**: 수집한 evidence를 종합했을 때, 어떤 화합물을 후속 신약 후보물질로 우선 검증해야 하며, 그 근거와 한계는 무엇인가?

## 2. Research Strategy

1. **Phase 1 (Research Plan)**: Sub-question·claim·필요 evidence·data source를 먼저 정의 (`01_research_plan.md`). 이 시점에 candidate ranking은 수행하지 않았다.
2. **Phase 2 (Evidence Hunt)**: BioMCP(PubMed/Europe PMC/ClinVar/ChEMBL/ClinicalTrials.gov 경유)로 sotorasib/KRAS G12C 기전 evidence를 카테고리별(Target/Drug/Quantitative/Structural/Biological/Clinical)로 수집 (`02_evidence_table.md`).
3. **Phase 3 (Ligand Landscape)**: Adagrasib, divarasib, olomorasib, RMC-6291을 포함 근거와 함께 landscape로 구축 (`03_ligand_landscape.md`).
4. **Phase 4 (Comparative Analysis)**: RCSB PDB에서 원자료 좌표(6OIM/6UT0/9DMM/9BFX)를 직접 다운로드하여 Biopython으로 superposition·pocket-residue 분석을 자체 수행 — 문헌 주장을 원자료로 독립 재현 (`analysis/`).
5. **Phase 5 (Candidate Prioritization)**: 결과를 보기 전에 8개 평가 기준을 먼저 정의한 뒤 적용 (`04_candidate_ranking.md`).
6. **Phase 6 (Verification Audit)**: 핵심 claim을 10개 질문으로 재검증, 일부 claim은 원자료(2개 독립 source)로 교차검증 (`05_verification_audit.md`).

**도구 사용 관련 주요 이슈**: ToolUniverse MCP 서버는 이번 연구 전체 기간 동안 재연결되지 않았다 (초기 `uvx` 미설치 → 설치 후에도 세션 내 재연결 미확인). 이로 인해 구조/화합물 분석은 ToolUniverse 대신 BioMCP + RCSB/ChEMBL/Europe PMC REST API 직접 조회 + 자체 Biopython 스크립트로 수행되었다. 이 대체 경로는 검증 가능했으나, ToolUniverse가 제공했을 수 있는 추가 분석(예: 자동화된 pocket druggability 평가)은 수행하지 못했다.

## 3. Reference Drug Mechanism (Sotorasib)

- KRAS G12C(c.34G>T, p.G12C, chr12:g.25398285C>A)는 ClinVar Pathogenic으로 분류된 활성화 돌연변이이며, GAP-mediated GTP hydrolysis를 저해해 GTP-bound(active) 상태 비중을 높인다 (Ostrem & Shokat 2013, PMID 24256730, Literature Claim).
- Sotorasib(AMG 510)은 KRAS G12C의 switch-II pocket에 결합하며, 이 pocket은 GDP-bound(inactive) 상태에서만 존재한다. Cys12와 acrylamide warhead 간 covalent reaction으로 결합해 KRAS G12C를 inactive 상태로 고정한다 (Ganguly & Yoo 2022, PMID 35461718, 원문 직접 인용 확인).
- PDB 6OIM(1.65 Å, RCSB 직접 조회 및 좌표 파싱)에서 covalent 결합·GDP·Mg2+가 함께 관찰되며, 자체 계산으로 pocket-lining residue(Val9-Gly13, Lys16, Pro34, Thr58-Glu63, Arg68, Asp69, Met72, **His95, Tyr96**, Gln99, Ile100, Val103)를 직접 확인했다.
- 정량 evidence(ChEMBL, PMID 31820981): MIAPaCa2(G12C) 세포에서 pERK 억제 IC50 68 nM, antiproliferation IC50 5.0 nM; A549(G12S) 세포에서는 36,500 nM로 selectivity를 시사.
- 임상: FDA 승인(NSCLC, mCRC), CodeBreaK 200(NCT04303780, Phase 3, 완료) 등.

## 4. Ligand Landscape (RQ2)

5개 리간드를 포함 근거와 함께 비교했다 (`03_ligand_landscape.md` 참고):

| Ligand | 결합 상태 | Pocket | Covalent | 구조(PDB) | 개발 단계 |
|---|---|---|---|---|---|
| Sotorasib | GDP-bound (OFF) | Switch-II pocket | Yes (Cys12) | 6OIM | FDA 승인 |
| Adagrasib | GDP-bound (OFF) | Switch-II pocket (거의 동일 residue set) | Yes (Cys12) | 6UT0 | FDA 승인 (2022-12-12, 2개 독립 source로 재확인) |
| Divarasib | GDP-bound (OFF) | Switch-II pocket, loop conformation 차이 | Yes (Cys12) | 9DMM | 임상 진행 중 (정확한 phase 미확인) |
| Olomorasib | 추정 GDP-bound | 추정 Switch-II pocket (Inference, 실험 구조 없음) | 추정 covalent | **없음 (Not found)** | 임상 진행 중 (정확한 phase 미확인) |
| RMC-6291 | **GTP-bound (ON)** | CypA tri-complex 계면 (switch-II pocket 아님) | Yes (Cys12, 다른 메커니즘) | 9BFX | Phase 1 (NCT05462717) |

## 5. Comparative Analysis (Phase 4 핵심 결과)

자체 구조 분석(`analysis/structural_comparison.py`, Biopython)으로 다음을 확인했다:

- **동일 pocket 확인**: Sotorasib/adagrasib/divarasib 3개 구조 모두 His95, Tyr96을 포함한 거의 동일한 pocket-lining residue를 공유함 — "switch-II pocket" 문헌 주장을 좌표 수준에서 독립 재확인.
- **Binding pose 차이의 독립 재현**: Divarasib의 switch-II loop이 sotorasib 대비 residue 65 Cα 기준 5.52 Å 이동 — 문헌 보고("최대 5.6 Å", PMID 40391409)와 거의 일치.
- **Resistance mutation과의 구조적 정합성**: MD 논문(PMID 40640254)이 지목한 resistance 관련 잔기(His95, Tyr96)가 실제로 3개 구조 모두의 pocket-lining residue임이 확인되어, 서로 다른 방법론(결정구조 vs MD+biochemical)이 수렴함.
- **RMC-6291은 진짜 다른 site**: 접촉 잔기(Cys12, Tyr32, Pro34, Thr35, Ile36, Glu37, Ala59, Gly60, Gln61, Tyr64, Met67, Tyr71)가 나머지 3개와 뚜렷이 다르고, His95/Tyr96/Gln99/Ile100/Val103 등 핵심 pocket residue가 빠져있음 — "GTP-bound state를 표적하는 별개 기전"이라는 주장이 좌표 수준에서 뒷받침됨.
- **한계**: 정량 activity(IC50/Kd)의 동일 조건 비교는 불가능("Not directly comparable"). Olomorasib은 실험 구조가 없어 이 분석에서 제외됨.

## 6. Candidate Prioritization (RQ3)

Sotorasib/adagrasib는 이미 FDA 승인되어 "후속 검증 후보" 틀에서 제외하고, 8개 사전 정의 기준(target relevance, structural evidence, mechanism differentiation[가중], quantitative activity, cellular evidence, development stage, resistance evidence[가중], evidence completeness)으로 3개 후보를 평가했다.

**제안 우선순위** (`04_candidate_ranking.md` §5 참고):

1. **RMC-6291 (Elironrasib)** — 유일하게 기전적으로 근본적으로 다른 후보(GTP-bound 표적). His95/Tyr96 의존적 resistance를 우회할 잠재력을 검증할 가치가 최우선. 단, 임상 근거는 Phase 1로 가장 미성숙.
2. **Divarasib (GDC-6036)** — 구조·기전·임상 성숙도의 균형이 가장 좋음. 독립 systematic review(PMID 40297021)로 NSCLC ORR 53.4%가 확인되어 실행 가능성이 가장 높은 후보. His95 취약성이라는 구체적 검증 대상도 식별됨.
3. **Olomorasib (LY3537982)** — His95 저항성에 상대적으로 강건하다는 흥미로운 신호가 있으나, 실험적 co-crystal 구조 자체가 없어(Not found) 다른 두 후보와 동등 비교가 어려움.

**중요 주의사항**: 이 순위는 사전에 "기전 차별화"와 "resistance evidence"에 가중치를 둔 기준의 결과이며, "가장 빠르게 실행 가능한 후속 검증"을 최우선으로 삼았다면 divarasib이 1순위였을 것이다. 이 tension은 의도적으로 숨기지 않았다.

## 7. Verification Audit (Phase 6 요약)

핵심 claim 9개 항목 감사 결과(`05_verification_audit.md`):

| 항목 | 판정 |
|---|---|
| Target identity | 통과 (High) |
| Mutation (G12C) | 통과 (High) |
| Drug-target relationship (covalent) | 통과, 단 "화학결합 직접 측정"이 아니라 "근접 관찰+문헌 서술"로 표현 정정 |
| Binding mechanism (switch-II / GTP-bound) | 통과 (High, 독립 재현) |
| PDB structure | 통과 (High) |
| Key residue (His95/Tyr96) | 통과 (위치 확인 High / affinity 영향은 Literature Claim 유지) |
| IC50/Kd | 부분 통과 (Sotorasib만 확보) |
| Clinical status | 부분 통과 (Sotorasib/adagrasib/RMC-6291 확인, divarasib/olomorasib 단계 미확인) |
| Candidate selection rationale | 통과 (Hypothesis로 명확히 표시) |

이번 세션에서 새로 수행한 2개의 독립 교차검증: (1) Adagrasib FDA 승인일(2022-12-12)이 DrugCentral과 OpenFDA Drugs@FDA 두 소스에서 일치, (2) Divarasib ORR claim이 별도 systematic review(PMID 40297021) 원문으로 수치 확인됨(NSCLC 53.4%).

## 8. Remaining Evidence Gaps

1. Adagrasib, divarasib, RMC-6291의 순수 biochemical IC50/Kd — ChEMBL API 반복 실패(HTTP 500)로 세션 내내 미확보.
2. Divarasib, olomorasib의 정확한 현재 임상 phase 및 NCT 번호 — 미확인.
3. "Covalent bond" 자체의 화학적 결합(bond length 등) 직접 측정 없음 — 논문/PDB 헤더 서술에 의존.
4. RMC-6291의 resistance mutation panel 실측 데이터 — 전무, 순수 Hypothesis.
5. Olomorasib의 실험적 co-crystal 구조 — 부재 (문헌 자체가 명시).
6. ToolUniverse MCP 서버가 세션 내내 재연결되지 않아, 이 도구가 제공했을 수 있는 추가 구조/화합물 분석(예: druggability scoring, 자동 ligand alignment)은 수행하지 못함.
7. Canon et al. 2019(PMID 31666701, sotorasib 원 논문) 본문은 PubTator3 조회가 반복 실패했고 구독 필요로 본문 전체를 대조하지 못함 — abstract만 Europe PMC로 확인됨.

## 9. Proposed Next Experiments

각 evidence gap에 대응하는 구체적 후속 검증 항목:

1. **RMC-6291**: (a) His95/Tyr96/Gln99 등 switch-II pocket 계열 resistance mutation panel에 대한 biochemical binding assay 수행하여 "resistance 우회 가능성" 가설을 직접 검증. (b) CypA 표면 접촉 잔기 상세 분석 (이번 세션에서 미수행).
2. **Divarasib**: (a) ChEMBL 또는 원 논문(Purkey et al. 등 discovery paper — 이번 세션에서 특정하지 못함)에서 biochemical IC50/Kd 직접 확보. (b) His95 mutant KRAS G12C에 대한 divarasib의 실제 결합력 저하를 정량 실험으로 재확인.
3. **Olomorasib**: 실험적 co-crystal 구조 확보를 최우선 과제로 제안 (현재 MD 기반 추정만 존재).
4. **공통**: ToolUniverse 재연결 후, 4개 구조에 대한 독립적인 pocket druggability/ligand efficiency 분석을 재수행하여 이번 자체 Biopython 분석 결과를 교차검증.
5. Divarasib/olomorasib 임상시험 NCT 번호 특정 및 최신 임상 데이터(ORR/PFS/OS, 안전성) 확인.

## 10. Conclusion

이 연구는 sotorasib을 출발점으로 KRAS G12C 표적 리간드 landscape를 구축하고, 문헌 근거뿐 아니라 RCSB PDB 원자료에 대한 자체 좌표 분석을 통해 일부 문헌 주장(switch-II pocket 공유, binding pose 차이, resistance 관련 residue)을 독립적으로 재현했다.

현재 확보된 구조적·정량적·임상적 evidence를 기준으로:

> **RMC-6291(Elironrasib)을 "switch-II pocket 계열 약물과 기전적으로 구별되는, resistance 우회 가능성을 검증할 최우선 candidate hypothesis"로 제안한다.** 다만 정량적 activity, resistance panel 실측 데이터, 임상 유효성 데이터가 모두 결여되어 있어, 이는 후속 biochemical/clinical validation이 반드시 필요한 탐색적 가설이며 확정된 우수성 주장이 아니다.
>
> **Divarasib(GDC-6036)**은 구조·기전·임상 성숙도가 가장 균형 잡혀 있고 독립 review에서 수치 확인된 임상 반응률을 가진 **실행 가능성이 높은 2차 우선 검증 후보**로 제안하며, His95 관련 resistance 취약성이 구체적 검증 대상으로 이미 식별되어 있다.
>
> **Olomorasib(LY3537982)**은 resistance 강건성이라는 흥미로운 신호가 있으나 구조적 근거가 전무하여, 실험적 co-crystal 구조 확보가 선행되어야 다른 두 후보와 동등하게 비교할 수 있는 후보로 분류한다.

이 결론들은 모두 "후속 검증이 필요한 candidate hypothesis"이며, "새로운 KRAS G12C 신약이다"와 같은 확정적 표현은 의도적으로 피했다 (CLAUDE.md §20). 어떤 claim이 Observation/Database Annotation/Experimental Evidence/Literature Claim/Inference/Hypothesis 중 어디에 해당하는지는 `02_evidence_table.md`, `03_ligand_landscape.md`, `04_candidate_ranking.md`에 지속적으로 구분·기록되어 있으며, 다른 연구자가 동일한 원자료(PMID, PDB ID, NCT 번호, ChEMBL ID)로 재확인할 수 있도록 identifier를 빠짐없이 남겼다.

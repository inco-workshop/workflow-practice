# Phase 6 — Verification Audit

작성일: 2026-08-27
상태: DRAFT — CHECKPOINT 4 대기 중.

이 문서는 CLAUDE.md §17의 10개 질문을 핵심 claim마다 적용하고, §18에서 지정한 우선순위 항목(target identity, mutation, drug-target relationship, binding mechanism, PDB structure, key residue, IC50/Kd, clinical status, candidate selection rationale)을 원자료로 재확인한 기록이다.

10개 질문 (반복 표기 대신 번호로 참조):
1. 직접 관찰된 사실인가? 2. Database annotation인가? 3. 실험 결과인가? 4. 논문의 해석인가? 5. Inference인가? 6. Hypothesis인가? 7. Citation이 실제 claim을 지지하는가? 8. 다른 source와 충돌하지 않는가? 9. 수치/단위가 정확한가? 10. 결론이 evidence보다 강하지 않은가?

---

## 이번 Phase에서 새로 수행한 재검증 (원자료 대조)

이번 세션에서 추가로 아래 3가지를 원자료 수준에서 재확인했다 (Phase 6 신규 작업):

1. **Residue numbering 일관성 검증**: 4개 구조(6OIM, 6UT0, 9DMM, 9BFX) 전부에서 좌표를 직접 파싱하여 residue 12 = CYS, residue 95 = HIS, residue 96 = TYR임을 확인함. → 이는 (a) G12C mutant 구조임을 독립 확인하고, (b) 서로 다른 PDB 엔트리 간 residue 번호 체계가 어긋나지 않음을 확인하여, Phase 4에서 수행한 "His95/Tyr96 공통 pocket residue" 비교가 numbering 오류에 의한 인공물이 아님을 뒷받침한다. (Q1 직접 관찰 / Q8 충돌 없음 확인)
2. **Adagrasib FDA 승인일 교차검증**: DrugCentral(`FDA Approved: December 12, 2022`)과 OpenFDA Drugs@FDA(`ORIG 1, AP, 2022-12-12`) 두 개의 독립 소스가 동일한 날짜를 보고함. 추가로 EMA 승인(2024-01-05, EMEA/H/C/006013)도 확인됨. (Q2 Database Annotation / Q8 두 독립 source 일치)
3. **Divarasib ORR claim의 수치 확보 및 재해석**: 이전(Phase 3)에는 "review abstract 수준의 정성적 claim, 수치 미확보"였던 "divarasib이 승인 약물보다 높은 ORR을 보인다"는 주장을, 별도의 독립적인 systematic review(El Zaitouni & Ennibi 2025, PMID 40297021, PMC12035108, 원문 직접 확인)로 재검증함. 원문 인용: "Divarasib showed a notably higher ORR of 53.4%" (NSCLC, Sacher et al. 2023 인용), CRC에서는 24%-29.1% (Sacher/Desai et al. 2023 인용). 비교 대상 adagrasib NSCLC ORR은 42.9%-45%, sotorasib은 7.1%-47%로 동일 리뷰에 보고됨. → **claim 자체는 지지되나(Q7), 이는 단일군(single-arm) 임상시험 간 cross-trial 비교이며 head-to-head RCT가 아니므로 "직접 비교 가능"으로 과대해석하면 안 됨 (Q10, CLAUDE.md §7 규칙 적용)**.

이 재검증 결과를 반영하여 `04_candidate_ranking.md`의 divarasib "개발 단계/임상 evidence" 항목을 아래와 같이 갱신한다 (원본 문서는 유지하고 이 문서에 갱신 사실을 기록):

> **갱신**: Divarasib 개발단계 evidence — "review-level, 수치 미확보" → "systematic review(PMID 40297021)가 인용한 1차 임상시험(Sacher et al. 2023) 수치로 확인: NSCLC ORR 53.4%, CRC ORR 24-29.1%. Adagrasib(NSCLC ORR 42.9-45%), sotorasib(NSCLC ORR 7.1-47%) 대비 수치상 우위이나, 이는 서로 다른 단일군 1상/2상 시험 간 비교로 환자군·시험 단계가 다를 수 있어 'Not directly comparable'(동일 조건 RCT 아님)로 계속 표시함."

---

## 핵심 Claim별 감사 (Audit)

### 1. Target identity — "KRAS G12C가 sotorasib/adagrasib/divarasib/RMC-6291의 direct target이다"

- Q1/Q2/Q3: ChEMBL/Open Targets/CIViC의 database annotation(모든 4개 화합물에서 일관됨) + 4개 PDB 구조에서 KRAS 단백질과의 직접 결합이 관찰됨(Observation). RMC-6291은 ClinicalTrials.gov 공식 설명에서도 "KRAS G12C(ON) inhibitor"로 명시.
- Q8: 모든 source(ChEMBL, Open Targets, CIViC, PDB, ClinicalTrials.gov)가 일관됨. 충돌 없음.
- Q10: "직접 표적"이라는 결론은 구조 관찰 + database annotation으로 뒷받침되며 과장 없음.
- **판정: 통과 (High confidence)**

### 2. Mutation (KRAS G12C 정의) — "c.34G>T, p.G12C, Pathogenic"

- Q2/Q3: ClinVar(rs121913530), COSMIC(COSM516) 두 개의 독립 database에서 일관되게 확인. CADD 33.0/SIFT deleterious/PolyPhen probably damaging은 계산적 예측(Q5, Inference)으로 별도 구분.
- Q9: chr12:g.25398285C>A, c.34G>T — BioMCP 원 조회 결과 그대로이며 이번 세션에서 재계산하지 않음(하지만 좌표 분석에서 residue 12=CYS로 아미노산 수준은 독립 재확인됨, 위 "신규 재검증" #1 참고).
- **판정: 통과 (High confidence, 단 ClinVar review status는 1 star로 제한적임을 계속 명시)**

### 3. Drug-target relationship (covalent, Cys12) — 4개 화합물 공통

- Q1: 4개 PDB 구조 전부에서 residue 12가 CYS이고 리간드가 그 근접부에 위치함을 직접 확인(Phase 4/6). 다만 이번 분석은 "공유결합(covalent bond)의 화학적 연결 여부"까지 자동으로 판정하지 않았다 — 거리 기반 근접성(4.5Å 이내)만 확인했고, PDB 헤더/논문 제목이 "covalently bound"라고 명시한 것을 근거로 covalent를 주장하고 있다. **엄밀히는 Q1(직접 관찰)이 아니라 Q2/Q4(annotation + 논문 서술)에 더 가깝다** — 이전 문서들에서 이를 "Observation"으로 표기한 것은 다소 강한 표현이었을 수 있어, 이 문서에서 정정한다.
- Q7: PDB 엔트리 제목("covalently bound to AMG 510" 등)과 원 논문(Ostrem 2013, Fell 2020)의 명시적 서술이 covalent 결합을 직접 뒷받침함 — citation이 claim을 지지함.
- **판정: 통과하되 표현 정정 필요 — "구조적으로 근접 관찰 + 논문의 covalent 서술"로 재분류 (완전한 화학적 결합 확인은 아님)**

### 4. Binding mechanism (switch-II pocket vs GTP-bound active state)

- Q1: 자체 좌표 분석으로 sotorasib/adagrasib/divarasib 3개 구조가 거의 동일한 pocket residue set(His95/Tyr96 포함)을 가짐을 확인(직접 관찰). RMC-6291은 확연히 다른 residue set + GNP(GTP 유사체) 결합을 확인(직접 관찰).
- Q4/Q7: "switch-II pocket"이라는 명칭 자체는 문헌(Ostrem 2013)의 해석적 명명이며, 이번 좌표 분석은 그 명칭이 가리키는 물리적 위치가 실제로 일관됨을 재확인한 것이다.
- Q8: 문헌 주장(같은 pocket, 다른 conformation)과 자체 계산(5.52Å 변위) 간 충돌 없음 — 오히려 수치가 거의 일치.
- **판정: 통과 (High confidence, 독립 재현됨)**

### 5. PDB structure identifiers

- Q1: RCSB REST API(`data.rcsb.org`)로 6OIM, 6UT0, 9DMM, 9BFX 각각의 title/resolution/ligand 구성을 직접 조회했고, 실제 좌표 파일을 다운로드해 파싱했다 — 이중으로 확인됨(entry metadata + 원자 좌표 존재).
- Q9: 해상도(1.65/1.94/1.79/1.4 Å)는 RCSB 메타데이터 그대로이며 재계산하지 않았으나, 좌표 파일이 실제로 파싱 가능하고 예상된 잔기 수(~167-170 aa)를 가짐을 확인해 파일 무결성은 간접 검증됨.
- **판정: 통과 (High confidence)**

### 6. Key residue (His95, Tyr96 등)

- Q1: 자체 좌표 계산(Phase 4/6)으로 직접 확인 — 이전에는 문헌에서 서술되지 않아 "Not found"였던 항목을 원자료로 직접 메꾼 것.
- Q8: MD 시뮬레이션 논문(PMID 40640254)이 예측한 "His95 mutation이 divarasib에 영향, Tyr96은 양쪽에 영향"이라는 resistance 관련 주장과, 이번 좌표 분석에서 확인된 "His95/Tyr96가 실제 pocket 접촉 잔기"라는 사실이 서로 다른 방법론임에도 일관됨 — 충돌 없음, 오히려 상호 보강.
- Q10: "His95/Tyr96이 pocket에 존재한다"는 것과 "His95 mutation이 divarasib affinity를 낮춘다"는 것은 별개의 claim이다. 전자는 이번 세션에서 직접 확인(구조), 후자는 여전히 원 논문(PMID 40640254)의 실험 결과 인용이며 이번 세션에서 그 실험 자체를 재현하지 않았다 — 결론이 evidence보다 강하지 않도록, `03_ligand_landscape.md`/`04_candidate_ranking.md`에서 두 claim을 분리해서 표기했는지 재확인 필요 → **확인 결과 이미 분리되어 표기되어 있음 (문제 없음)**.
- **판정: 통과 (His95/Tyr96 위치 확인은 High confidence / mutation의 affinity 영향은 여전히 Literature Claim 수준으로 유지)**

### 7. IC50 / Kd (정량 데이터)

- Q3: Sotorasib의 3개 수치(pERK IC50 68nM, antiproliferation IC50 5.0nM, G12S 세포주 36,500nM)는 ChEMBL activity record에서 조회 — 실험 결과(Experimental Evidence), document는 PMID 31820981(Lanman et al. 2020)로 추적 가능.
- Q7: 이번 세션에서 Lanman 2020 원문 표(Table)를 직접 대조하지는 못했다 (paywalled, 시간 제약) — ChEMBL이 원문에서 정확히 추출했는지는 ChEMBL 큐레이션을 신뢰한 것이며, 100% 원문 대조는 아님. **이는 명시적 한계로 남긴다.**
- Q9: 단위(nM)와 assay 종류(cellular pERK, cellular antiproliferation)는 ChEMBL 메타데이터 그대로 기록했으며 재계산 없음.
- Adagrasib/divarasib/RMC-6291의 IC50/Kd: 이번 세션 전체에서 끝내 확보하지 못함(ChEMBL API 반복 500 오류) — **Not found로 유지, 추측 금지 원칙 준수**.
- **판정: 부분 통과 — Sotorasib 수치는 Medium-High confidence(ChEMBL 큐레이션 신뢰, 원문 미대조), 나머지 3개 화합물은 Not found로 명시 유지**

### 8. Clinical status

- Q2/Q8: Sotorasib(FDA NSCLC+mCRC), adagrasib(FDA NSCLC, 2022-12-12, 이번 세션에서 2개 독립 source로 재확인 — 위 "신규 재검증" #2), RMC-6291(Phase 1, NCT05462717, ClinicalTrials.gov) 모두 확인됨.
- Divarasib/olomorasib의 정확한 임상 단계(Phase 몇 상인지)는 이번 세션에서 NCT 번호까지 특정하여 조회하지 않았다 — "임상시험 진행 중"이라는 서술은 review 문헌 인용이며, **정확한 phase/NCT 번호는 미확인 상태로 남는다 (Not found, 후속 확인 필요)**.
- **판정: 부분 통과 — Sotorasib/adagrasib/RMC-6291은 High confidence, divarasib/olomorasib의 정확한 임상 단계는 미확인**

### 9. Candidate selection rationale (`04_candidate_ranking.md`)

- Q6: 최종 순위(RMC-6291 > divarasib > olomorasib)는 명시적으로 **Hypothesis 수준의 우선순위 제안**이며 "확정된 우수성 주장"이 아님을 문서 자체에 §6("Final Conclusion 표현")로 명시함.
- Q10: 순위 산정 시 "만약 다른 기준(실행 가능성 우선)을 적용했다면 divarasib이 1순위가 되었을 것"이라는 tension을 숨기지 않고 기록함 — 결론이 evidence보다 강하게 표현되지 않도록 관리됨.
- **판정: 통과 — 단, 이 rationale은 재현 가능하지만 100% 객관적 산식이 아니라 사전 정의된 가중치(정성적 판단)에 기반함을 계속 명시해야 함**

---

## 종합 판정 요약

| 항목 | 판정 | 비고 |
|---|---|---|
| Target identity | 통과 | High |
| Mutation | 통과 | High (ClinVar 1-star 한계 유지) |
| Drug-target relationship (covalent) | 통과, 표현 일부 정정 | "직접 화학결합 확인"이 아니라 "근접성 관찰 + 논문 서술" 수준으로 재분류 |
| Binding mechanism | 통과 | High, 독립 재현됨 |
| PDB structure | 통과 | High |
| Key residue | 통과 | 위치 확인 High / affinity 영향은 Literature Claim 유지 |
| IC50/Kd | 부분 통과 | Sotorasib만 확보, 나머지 3개 Not found 유지 |
| Clinical status | 부분 통과 | Sotorasib/adagrasib/RMC-6291 확인, divarasib/olomorasib 단계 미확인 |
| Candidate selection rationale | 통과 | Hypothesis로 명확히 표시됨 |

## 검증되지 않은 채로 최종 보고서에 명시할 항목 (CLAUDE.md §18 규칙)

1. Adagrasib/divarasib/RMC-6291의 순수 biochemical IC50/Kd — 전 세션에 걸쳐 미확보.
2. Divarasib/olomorasib의 정확한 현재 임상 단계(phase)와 NCT 번호.
3. "Covalent bond" 자체의 화학적 결합 확인은 논문/PDB 헤더 서술에 의존하며, 이번 세션에서 결합 길이(bond length) 등을 직접 측정해 공유결합 여부를 화학적으로 재확인하지는 않았다.
4. RMC-6291의 resistance panel 실측 데이터 — Hypothesis 수준으로 유지.
5. Olomorasib의 실험적 co-crystal 구조 — 여전히 부재.

이 5개 항목은 `results/final_report.md`의 "Remaining Evidence Gaps" 섹션에 명시적으로 반영되어야 한다.

---

## CHECKPOINT 4 — FINAL VERIFICATION

위 감사 결과, 핵심 claim 대부분(target identity, mutation, binding mechanism, PDB structure, key residue 위치)은 원자료 교차 확인을 통과했다. 다음 항목은 여전히 미확인 상태로 최종 보고서에 명시적으로 남긴다: (1) adagrasib/divarasib/RMC-6291의 정량 데이터, (2) divarasib/olomorasib의 정확한 임상 단계, (3) covalent bond의 화학적 직접 확인, (4) RMC-6291 resistance 실측 데이터, (5) olomorasib 구조 부재.

이 상태로 최종 보고서(`results/final_report.md`, CLAUDE.md §19 구조)를 작성해도 될까요?

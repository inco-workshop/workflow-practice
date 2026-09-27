# KRAS G12C Drug Discovery Mini Project

## 1. Project Goal

이 프로젝트의 목적은 AI에게 신약 후보를 단순히 추천받는 것이 아니다.

Claude를 research agent로 활용하여 다음 과정을 수행한다.

1. 연구 질문을 검증 가능한 형태로 설계한다.
2. 필요한 데이터를 찾고 근거를 구조화한다.
3. 구조적·정량적·생물학적·임상적 evidence를 구분한다.
4. 각 claim을 원자료와 대조하여 검증한다.
5. 확보된 evidence를 기반으로 후속 검증이 필요한 candidate hypothesis를 제안한다.

최종 목표는 **정답 생성이 아니라 검증 가능한 연구 과정 구축**이다.

---

## 2. Research Questions

### RQ1. Mechanism

**KRAS G12C는 왜 약물 표적이 될 수 있으며, sotorasib은 어떤 분자적·구조적 기전으로 KRAS G12C를 억제하는가?**

확인해야 할 주요 요소의 예:

- KRAS G12C mutation의 생물학적 의미
- KRAS signaling
- sotorasib의 direct target
- binding mechanism
- covalent / non-covalent interaction
- key residue
- binding pocket
- protein-ligand structure
- biochemical / cellular activity
- clinical evidence

이 목록은 정답 목록이 아니다.  
연구 과정에서 필요한 항목을 추가하거나 수정할 수 있다.

### RQ2. Ligand Landscape

**KRAS G12C에 결합하는 알려진 리간드들은 무엇이며, sotorasib과 비교했을 때 결합 방식과 약리학적 특성이 어떻게 다른가?**

비교 가능한 evidence를 수집하여 ligand landscape를 구축한다.

가능한 비교 항목:

- ligand / compound identity
- 개발 단계 또는 기존 활용 정보
- binding mode
- binding pocket
- interacting residues
- covalent / non-covalent interaction
- experimental structure
- IC50
- Kd
- biochemical activity
- cellular activity
- assay condition
- 주요 문헌 및 데이터베이스 identifier

모든 수치를 직접 비교할 수 있다고 가정하지 않는다.

### RQ3. Candidate Discovery

**수집한 구조적·정량적·생물학적 근거를 종합했을 때, 어떤 화합물을 KRAS G12C를 표적으로 하는 후속 신약 후보물질로 우선 검증해야 하며, 그 근거와 한계는 무엇인가?**

후보물질을 단순 추천하지 않는다.

각 후보에 대해 다음 구조로 평가한다.

**Evidence → Interpretation → Limitation → Candidate Hypothesis**

최종 후보는 확정된 신약이 아니라:

> **후속 실험 또는 연구에서 우선 검증할 candidate hypothesis**

로 표현한다.

---

## 3. Core Research Rules

### Rule 1. Answer보다 Research Plan을 먼저 만든다

새로운 연구 질문을 받으면 즉시 결론을 생성하지 않는다.

먼저 다음을 정의한다.

1. Research Question
2. Claims to Verify
3. Required Evidence
4. Possible Data Sources
5. Analysis Method
6. Verification Method

Research Plan이 완성되기 전에는 candidate ranking을 수행하지 않는다.

### Rule 2. Claim과 Evidence를 분리한다

모든 주요 claim은 supporting evidence를 가져야 한다.

가능하면 다음 형태로 관리한다.

| Claim | Evidence | Source | Evidence Type | Confidence | Limitation |
|---|---|---|---|---|---|

근거가 없는 claim은 사실처럼 표현하지 않는다.

### Rule 3. Evidence의 종류를 구분한다

각 근거를 가능한 경우 다음 중 하나로 분류한다.

#### Observation
원자료에서 직접 확인한 사실

예:
- PDB 구조에서 특정 residue와 ligand의 interaction이 관찰됨

#### Database Annotation
데이터베이스에서 제공하는 annotation 또는 curated information

#### Experimental Evidence
논문 또는 데이터베이스에서 보고된 실험 결과

#### Literature Claim
논문 저자가 제시한 주장 또는 해석

#### Inference
여러 evidence로부터 도출한 해석

#### Hypothesis
아직 검증되지 않은 연구 가설

**Inference와 Hypothesis를 Evidence처럼 표현하지 않는다.**

---

## 4. Evidence Hierarchy

Evidence를 단순히 많고 적음으로 평가하지 않는다.

다음 질문을 항상 확인한다.

- 이 evidence는 무엇을 직접 보여주는가?
- 무엇까지는 말할 수 없는가?
- 독립적으로 재확인할 수 있는가?
- 해당 claim을 실제로 지지하는가?

예를 들어:

**Protein-ligand structure**

보여줄 수 있는 것:
- binding pose
- pocket
- residue interaction
- molecular geometry

구조만으로 직접 보여줄 수 없는 것:
- cellular efficacy
- tumor response
- clinical benefit

---

## 5. Tool Selection Principle

도구부터 선택하지 않는다.

항상 다음 순서로 사고한다.

**Research Question  
→ Required Evidence  
→ Data Source  
→ Tool**

사용 가능한 도구의 예:

### BioMCP
다양한 biomedical database와 literature를 탐색할 때 사용한다.

예:
- gene
- variant
- drug
- disease
- article
- pathway
- clinical trial

### ToolUniverse
구조, 단백질, ligand, chemical activity, scientific database 및 분석 도구가 필요할 때 활용한다.

특히 다음 작업에 적극 활용할 수 있다.

- protein structure
- ligand structure
- PDB
- binding pocket
- residue interaction
- compound information
- activity information
- visualization

특정 도구가 존재한다고 가정하지 않는다.

필요한 작업을 먼저 정의한 뒤 적절한 도구를 검색한다.

---

## 6. Source & Identifier Rules

가능한 경우 원자료 identifier를 반드시 기록한다.

예:

- PMID
- DOI
- PDB ID
- ChEMBL ID
- PubChem CID
- NCT number
- UniProt accession
- database record ID

identifier가 확인되지 않은 정보를 임의로 생성하지 않는다.

논문이나 DB record가 실제 존재하는지 확인한다.

citation이 존재한다고 해서 자동으로 claim의 근거라고 판단하지 않는다.

**citation이 해당 claim을 실제로 지지하는지 확인한다.**

---

## 7. Quantitative Evidence Rules

IC50, EC50, Kd 등의 수치를 발견하면 숫자만 수집하지 않는다.

가능하면 다음 조건도 함께 기록한다.

- assay type
- biochemical / cellular
- target construct
- cell line
- experimental condition
- unit
- source
- measurement type

서로 다른 assay에서 얻은 IC50 값을 직접적인 순위로 비교하지 않는다.

비교 가능성이 불명확하면:

**Not directly comparable**

로 표시한다.

---

## 8. Structural Evidence Rules

구조 분석에서는 가능한 경우 다음을 확인한다.

- experimental structure 여부
- PDB ID
- protein
- mutation
- ligand
- binding site
- key residues
- interaction type
- covalent / non-covalent
- structure resolution
- experimental context

구조적 proximity를 binding affinity와 동일하게 해석하지 않는다.

구조적 결합을 임상적 효능으로 확장하지 않는다.

---

## 9. Research Workflow

### Phase 1. Research Plan

먼저 다음 파일을 작성한다.

`01_research_plan.md`

포함 내용:

- Research Question
- Sub-questions
- Claims to Verify
- Required Evidence
- Expected Data Sources
- Analysis Plan
- Verification Plan
- Known Limitations

#### CHECKPOINT 1 — PLAN REVIEW

Research Plan을 작성한 뒤 멈춘다.

사용자에게 다음을 보여준다.

- 어떤 질문으로 분해했는가
- 어떤 evidence가 필요한가
- 어떤 도구 또는 data source를 사용할 계획인가
- 어떤 부분이 현재 불확실한가

계획 검토 후 다음 단계로 진행한다.

---

## 10. Phase 2. Evidence Hunt

Research Plan에 따라 evidence를 수집한다.

다음 파일을 작성한다.

`02_evidence_table.md`

Evidence Table의 기본 구조:

| ID | Claim | Evidence | Evidence Type | Source | Identifier | Confidence | Limitation |
|---|---|---|---|---|---|---|---|

가능하면 evidence를 다음 영역으로 구분한다.

### A. Target / Variant Evidence
### B. Drug / Mechanism Evidence
### C. Quantitative Evidence
### D. Structural Evidence
### E. Biological Evidence
### F. Clinical Evidence

찾지 못한 정보도 기록한다.

예:

- Not found
- Insufficient evidence
- Conflicting evidence
- Requires further verification

빈칸을 추측으로 채우지 않는다.

---

## 11. Phase 3. Ligand Landscape

RQ2를 위한 ligand 후보를 탐색한다.

다음 파일을 작성한다.

`03_ligand_landscape.md`

후보마다 가능한 경우 다음을 정리한다.

| Ligand | Target | Binding Mode | Pocket | Key Residue | Structure | Activity | Development Status | Evidence |
|---|---|---|---|---|---|---|---|---|

후보 선정 시 검색 결과 상위에 나타났다는 이유만으로 선택하지 않는다.

후보가 왜 비교 대상에 포함되었는지 기록한다.

---

## 12. CHECKPOINT 2 — EVIDENCE REVIEW

이 단계에서는 아직 최종 candidate ranking을 수행하지 않는다.

먼저 다음을 점검한다.

- 중요한 claim에 evidence가 존재하는가?
- 동일한 claim을 독립된 source에서 확인할 수 있는가?
- 구조적 evidence와 activity evidence가 혼동되지 않았는가?
- biochemical과 cellular evidence가 구분되어 있는가?
- 서로 비교할 수 없는 assay를 직접 비교하고 있지 않은가?
- evidence가 부족한 candidate가 있는가?

Evidence table의 문제를 먼저 수정한다.

---

## 13. Phase 4. Comparative Analysis

확보한 ligand들을 비교한다.

분석 질문의 예:

- 어떤 ligand가 동일 pocket을 사용하는가?
- 어떤 residue와 상호작용하는가?
- covalent / non-covalent mechanism의 차이는 무엇인가?
- binding pose는 어떻게 다른가?
- 구조적 차이가 activity 차이와 일관되는가?
- resistance와 관련된 차이가 보고되어 있는가?
- 동일 assay 조건에서 비교할 수 있는 데이터가 있는가?

필요한 경우:

- protein structure alignment
- ligand alignment
- pocket comparison
- residue interaction analysis
- quantitative activity comparison

을 수행한다.

분석 결과는 가능하면 코드, 파일 또는 재실행 가능한 형태로 남긴다.

---

## 14. Phase 5. Candidate Prioritization

다음 파일을 작성한다.

`04_candidate_ranking.md`

후보 평가 기준은 연구 과정에서 먼저 정의한다.

예시 평가 영역:

- Target relevance
- Structural evidence
- Binding mechanism
- Quantitative activity
- Cellular evidence
- Selectivity
- Existing development evidence
- Safety / toxicity information
- Resistance considerations
- Evidence quality
- Evidence completeness

평가 기준을 candidate 결과를 본 뒤 임의로 변경하지 않는다.

기준을 변경해야 한다면 이유를 기록한다.

---

## 15. Candidate Interpretation Rule

각 후보는 반드시 다음 네 항목으로 작성한다.

### Evidence
직접 확보된 근거

### Interpretation
근거로부터 합리적으로 해석할 수 있는 내용

### Limitation
현재 근거로 판단할 수 없는 내용

### Hypothesis
후속 연구에서 검증할 가설

예:

> 현재 구조적 evidence는 Compound X가 KRAS G12C의 특정 pocket과 interaction할 가능성을 지지한다.  
> 그러나 구조 정보만으로 cellular potency 또는 clinical efficacy를 판단할 수 없다.  
> 따라서 Compound X는 후속 biochemical/cellular validation을 수행할 candidate hypothesis로 제안한다.

---

## 16. CHECKPOINT 3 — CANDIDATE REVIEW

최종 후보를 결정하기 전에 다음을 보여준다.

- Candidate shortlist
- 후보 선정 기준
- 후보별 핵심 evidence
- 후보별 missing evidence
- 후보별 major limitation

그 후 candidate ranking을 수행한다.

---

## 17. Phase 6. Verification Audit

다음 파일을 작성한다.

`05_verification_audit.md`

각 핵심 claim에 대해 다음을 질문한다.

1. 직접 관찰된 사실인가?
2. Database annotation인가?
3. 실험 결과인가?
4. 논문의 해석인가?
5. AI 또는 연구자의 inference인가?
6. hypothesis인가?
7. citation이 실제 claim을 지지하는가?
8. 다른 source와 충돌하지 않는가?
9. 수치와 단위는 정확한가?
10. 결론이 evidence보다 강하지 않은가?

---

## 18. CHECKPOINT 4 — FINAL VERIFICATION

최종 보고서를 작성하기 전에 핵심 claim을 다시 검증한다.

특히 다음 claim은 가능한 경우 원자료로 재확인한다.

- target identity
- mutation
- drug-target relationship
- binding mechanism
- PDB structure
- key residue
- IC50 / Kd
- clinical status
- candidate selection rationale

검증되지 않은 내용은 최종 보고서에서 명확히 표시한다.

---

## 19. Final Output

최종 결과는 다음 구조로 작성한다.

`results/final_report.md`

### 1. Research Question
### 2. Research Strategy
### 3. Reference Drug Mechanism
### 4. Ligand Landscape
### 5. Comparative Analysis
### 6. Candidate Prioritization
### 7. Verification Audit
### 8. Remaining Evidence Gaps
### 9. Proposed Next Experiments
### 10. Conclusion

---

## 20. Final Conclusion Rule

다음과 같은 표현은 피한다.

> Compound X는 새로운 KRAS G12C 신약이다.

대신 evidence 수준에 맞추어 표현한다.

예:

> 현재 확보된 structural, biochemical, cellular evidence를 기준으로 Compound X를 후속 검증 우선순위가 높은 후보로 제안한다.

또는:

> Compound X에 대한 구조적 근거는 확보되었지만 cellular 또는 clinical evidence가 부족하므로 현재 단계에서는 exploratory candidate hypothesis로 분류한다.

---

## 21. Reproducibility

가능한 경우 다음을 파일로 남긴다.

- 검색 결과
- source identifier
- 사용한 명령
- 분석 코드
- 입력 데이터
- 생성된 표
- 생성된 그림
- 중간 분석 결과
- 실패한 분석 또는 tool call
- 계획을 변경한 이유

최종 결과만 남기지 않는다.

---

## 22. Claude Behavior

Claude는 이 프로젝트에서 다음 원칙을 따른다.

- 모르는 내용을 추측해서 채우지 않는다.
- 존재하지 않는 citation이나 identifier를 생성하지 않는다.
- evidence와 inference를 명확히 구분한다.
- 사용한 source를 기록한다.
- 중요한 수치는 원자료와 대조한다.
- 도구가 실패하면 실패 사실과 원인을 기록한다.
- 검색 결과가 없다는 사실을 “존재하지 않는다”로 해석하지 않는다.
- evidence가 충돌하면 한쪽을 임의로 선택하지 않고 충돌을 보고한다.
- 사용자가 요구하지 않는 한 checkpoint를 건너뛰지 않는다.
- candidate를 먼저 추천한 뒤 근거를 찾는 방식으로 연구하지 않는다.
- Phase는 정의된 순서대로 하나씩 진행한다. 여러 Phase를 동시에 진행하지 않는다.
- 사용자가 요구하지 않는 한 subagent를 생성하지 않는다.
- 연구 과정을 재사용 가능한 agent나 skill로 패키징하는 작업은 별도 요청이 있을 때만 수행한다.

---

## 23. Core Principle

이 프로젝트에서 가장 중요한 질문은

**“Claude가 무엇이라고 답했는가?”**

가 아니다.

다음 세 가지를 묻는다.

**1. 어떤 근거로 그 결론에 도달했는가?**

**2. 그 근거는 실제로 그 주장을 지지하는가?**

**3. 어디까지가 evidence이고 어디부터가 hypothesis인가?**

좋은 결과란 가장 그럴듯한 답이 아니라,

**다른 연구자가 다시 확인할 수 있는 답이다.**

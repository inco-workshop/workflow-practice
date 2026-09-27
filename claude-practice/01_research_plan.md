# Research Plan: KRAS G12C Drug Discovery (Sotorasib을 출발점으로)

작성일: 2026-08-27
상태: DRAFT — CHECKPOINT 1 검토 대기중 (아직 evidence 수집 시작 안 함)

---

## 1. Research Question (원문)

- **RQ1 (Mechanism)**: KRAS G12C는 왜 약물 표적이 될 수 있으며, sotorasib은 어떤 분자적·구조적 기전으로 KRAS G12C를 억제하는가?
- **RQ2 (Ligand Landscape)**: KRAS G12C에 결합하는 알려진 리간드들은 무엇이며, sotorasib과 비교했을 때 결합 방식과 약리학적 특성이 어떻게 다른가?
- **RQ3 (Candidate Discovery)**: 수집한 구조적·정량적·생물학적 근거를 종합했을 때, 어떤 화합물을 후속 신약 후보물질로 우선 검증해야 하며, 그 근거와 한계는 무엇인가?

---

## 2. Sub-questions

### RQ1 관련
1. KRAS G12C mutation의 biochemical 특성은 무엇인가 (GTP/GDP cycling, intrinsic hydrolysis rate 변화 등)?
2. KRAS의 정상 signaling pathway와, G12C mutation이 이를 어떻게 변형시키는가?
3. Sotorasib의 direct molecular target은 무엇으로 보고되어 있는가 (KRAS G12C 특이적인가)?
4. Sotorasib은 covalent인가 non-covalent인가? 어떤 residue와 반응하는가?
5. Sotorasib이 결합하는 pocket은 무엇인가 (예: switch II pocket)? 이는 GDP-bound state에 특이적인가 GTP-bound state에도 결합 가능한가?
6. 이 결합이 KRAS의 downstream effector(RAF 등) 결합을 어떻게 저해하는가?
7. Sotorasib의 biochemical/cellular activity 수치는 무엇이며 어떤 assay에서 측정되었는가?
8. Sotorasib의 임상적 근거(승인 적응증, 주요 임상시험 결과)는 무엇인가?

### RQ2 관련
9. KRAS G12C를 표적으로 알려진 다른 ligand/compound는 무엇인가 (예: adagrasib, ARS-853, ARS-1620, MRTX849 등 — 목록은 조사 과정에서 확정)?
10. 각 ligand는 covalent인지 non-covalent인지, 어떤 pocket/residue와 상호작용하는지?
11. 각 ligand에 대한 실험적 구조(PDB)가 존재하는가?
12. 각 ligand의 biochemical/cellular activity(IC50, Kd 등)는 무엇이며 assay 조건은 어떠한가?
13. 각 ligand의 개발 단계는 무엇인가 (전임상/임상/승인)?
14. Sotorasib과 비교했을 때 selectivity, resistance profile 관련 보고가 있는가?

### RQ3 관련
15. RQ1/RQ2에서 확보한 evidence 중 어떤 조합(구조+정량+생물학적)이 특정 후보를 지지하는가?
16. 각 후보에 대해 무엇이 검증되지 않았는가 (예: cellular activity는 있으나 구조 정보 부족, 혹은 반대)?
17. Resistance mutation과 관련하여 sotorasib 대비 개선 가능성이 있는 후보가 있는가?

---

## 3. Claims to Verify (초기 예상 — 조사 후 evidence table에서 갱신)

아래는 "확인해야 할 claim의 목록"이며, 아직 검증되지 않은 상태다. 이 단계에서 사실로 단정하지 않는다.

| # | Claim (미검증) | 관련 RQ |
|---|---|---|
| C1 | KRAS G12C mutation은 intrinsic GTPase activity를 낮추고 GAP-mediated hydrolysis에 저항성을 가진다 | RQ1 |
| C2 | Sotorasib은 KRAS G12C의 switch II pocket에 결합한다 | RQ1 |
| C3 | Sotorasib은 mutant cysteine(G12C의 Cys12)과 covalent bond를 형성한다 | RQ1 |
| C4 | Sotorasib은 GDP-bound (inactive) 상태의 KRAS G12C를 우선적으로 표적한다 | RQ1 |
| C5 | Sotorasib은 KRAS-RAF 상호작용을 저해하여 downstream MAPK signaling을 차단한다 | RQ1 |
| C6 | Sotorasib은 KRAS G12C p.G12C 특이적이며 wild-type KRAS나 다른 KRAS mutant에는 작용하지 않는다(또는 selectivity가 보고되어 있다) | RQ1 |
| C7 | Adagrasib(MRTX849) 등 다른 covalent KRAS G12C inhibitor가 존재하며 유사한 pocket/mechanism을 공유한다 | RQ2 |
| C8 | 서로 다른 KRAS G12C inhibitor 간 IC50/Kd는 assay 조건이 달라 직접 비교가 어려울 수 있다 | RQ2 |
| C9 | 특정 resistance mutation(예: Y96D, H95 관련 등)이 sotorasib 내성과 연관되어 보고되어 있다 | RQ2/RQ3 |

이 목록은 고정된 것이 아니며, evidence hunt 과정에서 추가·삭제·수정될 수 있다.

---

## 4. Required Evidence

### A. Target/Variant Evidence
- KRAS gene/variant 정보 (G12C의 정의, 발생 빈도, 관련 암종)
- KRAS G12C의 생화학적 특성에 대한 문헌/annotation

### B. Drug/Mechanism Evidence
- Sotorasib의 target 정보 (database annotation + 문헌)
- Sotorasib의 작용 기전 관련 1차 문헌 (구조논문 등)

### C. Quantitative Evidence
- Sotorasib 및 비교 ligand들의 IC50/Kd, biochemical vs cellular assay 구분, assay 조건

### D. Structural Evidence
- Sotorasib-KRAS G12C 복합체 PDB 구조 (예: 존재한다면 PDB ID 확인)
- 비교 ligand들의 PDB 구조 (존재 여부 확인)
- Binding pocket, key residue, covalent/non-covalent interaction 정보

### E. Biological Evidence
- Cellular assay 결과 (세포주, phospho-ERK 등 downstream marker 억제 등)

### F. Clinical Evidence
- Sotorasib 임상시험 (NCT number), 승인 상태, 주요 결과
- 비교 ligand 중 임상 단계에 있는 것들의 임상 근거

찾지 못한 항목은 "Not found" / "Insufficient evidence"로 명시하고 추측으로 채우지 않는다.

---

## 5. Expected Data Sources (계획 — 실제 사용은 접근 가능 여부에 따라 조정)

| 목적 | 예상 source |
|---|---|
| Gene/variant, drug, clinical trial, literature | BioMCP (PubMed, ClinicalTrials.gov, ClinVar, OncoKB, UniProt 등) |
| Protein/ligand structure, PDB, binding pocket, residue interaction | ToolUniverse (구조/화합물/activity 관련 도구) |
| 화합물 identifier, activity 데이터 | ChEMBL, PubChem (BioMCP 또는 ToolUniverse 경유, 필요시 직접 조회) |
| PDB 원자료 확인 | RCSB PDB |

**⚠ 현재 상태 이슈**: ToolUniverse MCP 서버가 이번 세션에서 연결에 실패한 상태로 확인됨 (`plugin:tooluniverse:tooluniverse` — "Skipping connection"). 즉 구조/화합물 관련 전용 도구를 아직 사용할 수 없다. BioMCP 도구는 사용 가능한 것으로 확인됨. 구조 관련 evidence(PDB 등)는 우선 BioMCP나 필요시 WebFetch로 RCSB/PubChem/ChEMBL을 직접 조회하는 방식으로 시도하고, ToolUniverse 재연결이 필요하면 사용자에게 알린다.

---

## 6. Analysis Plan

1. RQ1: BioMCP로 KRAS G12C variant/gene 정보와 sotorasib drug annotation을 조회. 가능하면 원 문헌(구조 논문 등)을 찾아 binding mechanism claim을 검증.
2. RQ2: KRAS G12C 관련 알려진 ligand 목록을 문헌/데이터베이스에서 수집 (검색 상위 결과라는 이유만으로 채택하지 않고, 왜 비교 대상에 포함되는지 근거 기록). 각 ligand에 대해 동일한 evidence 카테고리(binding mode, pocket, residue, structure, activity, development status)를 채움.
3. RQ2 비교: 서로 다른 assay 조건의 IC50/Kd는 직접 순위 비교하지 않고 "Not directly comparable"로 표시. 동일 pocket/residue 사용 여부, covalent/non-covalent 차이를 구조적으로 비교.
4. RQ3: Evidence table과 ligand landscape를 종합하여 candidate별 Evidence → Interpretation → Limitation → Hypothesis 구조로 정리.

---

## 7. Verification Plan

- 핵심 claim(target identity, mutation, binding mechanism, PDB structure, key residue, IC50/Kd, clinical status)은 가능하면 원자료(원문 논문, PDB record, ClinicalTrials.gov 등)로 재확인한다.
- Citation이 존재한다고 해서 자동으로 해당 claim의 근거로 인정하지 않고, citation이 실제로 그 claim을 지지하는지 확인한다.
- 서로 다른 source 간 값/주장이 충돌하면 임의로 하나를 선택하지 않고 충돌로 기록한다.
- Phase 6 (05_verification_audit.md)에서 각 핵심 claim에 대해 10개 검증 질문(CLAUDE.md §17)을 적용한다.

---

## 8. Known Limitations (현재 시점)

- ToolUniverse MCP 서버 연결 실패로 구조/화합물 전용 도구 접근이 현재 불가능하다 (재시도 또는 대체 경로 필요).
- 아직 어떤 ligand들이 "KRAS G12C landscape"에 포함될지 확정되지 않았다 — evidence hunt 단계에서 결정한다.
- Biochemical/cellular assay 조건이 문헌마다 상이할 가능성이 높아, 정량적 비교의 상당 부분이 "Not directly comparable"로 처리될 수 있다.
- 이 프로젝트는 in silico/literature 기반 조사이며, wet-lab 실험을 수행하지 않는다. 따라서 모든 최종 결과는 "candidate hypothesis" 수준으로 제한된다.

---

## CHECKPOINT 1 — PLAN REVIEW 요청

검토를 위해 요약하면:

- **분해한 질문**: RQ1(기전) 8개, RQ2(리간드 비교) 6개, RQ3(후보 도출) 3개 sub-question, 총 9개 초기 claim 후보.
- **필요 evidence**: Target/Variant, Drug/Mechanism, Quantitative, Structural, Biological, Clinical 6개 카테고리.
- **계획한 도구/데이터 소스**: BioMCP(사용 가능 확인됨), ToolUniverse(현재 연결 실패 — 재시도 필요), 필요시 RCSB/PubChem/ChEMBL 직접 조회.
- **현재 불확실한 부분**: (1) ToolUniverse 연결 문제로 구조 데이터 접근 경로가 아직 미확정, (2) 비교할 ligand 목록이 아직 확정되지 않음(evidence hunt에서 결정 예정), (3) assay 간 비교 가능성.

이 계획대로 Phase 2 (Evidence Hunt)로 진행해도 될까요? 아니면 sub-question이나 claim 목록, data source 계획을 수정하길 원하시나요?

# Evidence Table — Phase 2 (Evidence Hunt)

작성일: 2026-08-27
범위: RQ1 (Sotorasib / KRAS G12C mechanism) 중심. RQ2 ligand landscape 비교는 `03_ligand_landscape.md`에서 별도로 다룬다.
상태: DRAFT — CHECKPOINT 2 검토 전. 아직 candidate ranking 없음.

도구 사용 현황: ToolUniverse MCP는 이번 세션에서 재연결 실패 (uv/uvx 미설치 → 설치 완료했으나 15분 재시도 캐시로 인해 세션 내 재연결 미확인). 이 표의 구조 evidence는 BioMCP + RCSB PDB REST API(WebFetch 직접 조회)로 확보했다.

---

## A. Target / Variant Evidence

| ID | Claim | Evidence | Evidence Type | Source | Identifier | Confidence | Limitation |
|---|---|---|---|---|---|---|---|
| A1 | KRAS는 small GTPase superfamily 단백질을 코딩하며, 단일 아미노산 치환이 activating mutation을 유발한다 | NCBI Gene 요약: "a single amino acid substitution is responsible for an activating mutation" | Database Annotation | NCBI Gene / MyGene.info | Entrez Gene ID 3845 | High | Annotation 수준 설명이며 G12C 특이적 메커니즘은 아님 |
| A2 | KRAS p.G12C (c.34G>T, chr12:g.25398285C>A)는 ClinVar에서 Pathogenic으로 분류됨 | ClinVar record | Database Annotation | ClinVar via MyVariant.info | rs121913530 / COSM516 | High | ClinVar star rating = 1 (제한적 review status) |
| A3 | G12C variant는 CADD 33.0, SIFT deleterious, PolyPhen probably damaging으로 예측됨 | 계산적 pathogenicity 예측 | Inference (predictive annotation, 실험 관찰 아님) | MyVariant.info (dbNSFP 등 aggregated) | rs121913530 | Medium | 예측 도구이며 직접적 기능 실험 결과 아님 |
| A4 | G12C mutation은 intrinsic GTP hydrolysis를 저해하고 GAP-mediated hydrolysis에 저항성을 부여하여 GTP-bound active state 비중을 높인다 | Ostrem & Shokat 2013 abstract: "Oncogenic mutations result in functional activation of Ras family proteins by impairing GTP hydrolysis... gives GTP an advantage over GDP" | Literature Claim | PubMed/Europe PMC | PMID 24256730, DOI 10.1038/nature12796 | High (원저자 주장, 널리 인용됨 — 2090회 인용) | Abstract 수준 인용이며 논문 본문 전체는 paywalled로 미확인 |

## B. Drug / Mechanism Evidence

| ID | Claim | Evidence | Evidence Type | Source | Identifier | Confidence | Limitation |
|---|---|---|---|---|---|---|---|
| B1 | Sotorasib의 direct target은 KRAS (GTPase KRas)이다 | ChEMBL/Open Targets target annotation + CIViC variant target = KRAS G12C | Database Annotation | ChEMBL, Open Targets, CIViC (via BioMCP) | DrugBank DB15569 / ChEMBL CHEMBL4535757 | High | Annotation이며 결합 기전 세부사항은 별도 확인 필요 |
| B2 | K-Ras(G12C) 억제제는 mutant cysteine을 이용해 비가역적으로(irreversibly) 결합하며, wild-type protein에는 작용하지 않는다. 결합은 switch-II 영역 아래에 새로 형성되는 pocket(현재의 switch II pocket 개념)에서 일어나며 switch-I/switch-II를 교란해 GDP 선호를 강화하고 Raf 결합을 저해한다 | Ostrem & Shokat 2013 abstract 원문: "These compounds rely on the mutant cysteine for binding... Crystallographic studies reveal the formation of a new pocket... beneath the effector binding switch-II region. Binding... disrupts both switch-I and switch-II, subverting the native nucleotide preference to favour GDP over GTP and impairing binding to Raf." | Literature Claim (구조 실험 기반 주장, 이 논문 자체는 sotorasib이 아닌 초기 세대 covalent G12C inhibitor에 대한 것) | PubMed/Europe PMC | PMID 24256730 | High for the *concept* of switch-II pocket; sotorasib 자체에 대한 것은 아님(B3 참고) | 이 논문은 sotorasib(AMG 510) 발표(2019) 이전 연구이며, 이후 세대 화합물 일반화 필요 |
| B3 | Sotorasib은 switch II 영역의 pocket에 결합하며 이 pocket은 GDP-bound(inactive) 상태에서만 존재한다. Cys12와 acrylamide warhead 간 covalent reaction으로 결합하며, 이 결합은 KRAS G12C를 inactive 상태로 고정한다 | 리뷰 논문 원문 인용: "Sotorasib binds to a pocket of the switch II region that is present only in the inactive GDP-bound state"; "through a covalent reaction between the cysteine residue and the acrylamide group of the molecule"; "This specific and irreversible binding of sotorasib results in trapping KRASG12C in the inactive state" | Literature Claim (secondary review) | Ganguly & Yoo, Trends Pharmacol Sci 2022 (PMC 원문 직접 확인) | PMID 35461718, PMCID PMC9106916 | High (원문 직접 인용 확인) | Secondary review이며 1차 문헌(Canon 2019, Lanman 2020) 본문은 paywalled로 직접 대조 못함(아래 tool failure 참고) |
| B4 | Sotorasib-KRAS G12C 복합체의 실험적 결정구조가 존재하며, covalent bond + GDP + Mg2+가 함께 관찰됨 | RCSB PDB entry 6OIM: title "Crystal Structure of human KRAS G12C covalently bound to AMG 510", resolution 1.65 Å, ligands = AMG 510(covalent), GDP, Mg2+ | Observation (원자료 PDB 직접 확인) | RCSB PDB (data.rcsb.org REST API) | PDB ID 6OIM | High (구조 데이터 직접 조회) | 구조가 covalent/GDP-bound 상태임을 보여주지만, 이 자체로 cellular/clinical efficacy를 입증하지 않음 |
| B5 | AMG 510(sotorasib)은 임상 개발에 진입한 최초의 KRAS G12C 억제제로 보고됨 | Canon et al. 2019 abstract(Europe PMC REST 직접 확인): "Our efforts have led to the discovery of AMG 510, which is, to our knowledge, the first KRAS(G12C) inhibitor in clinical development." | Literature Claim | Europe PMC REST API | PMID 31666701, DOI 10.1038/s41586-019-1694-1 | High (원문 abstract 직접 확인) | 논문 본문은 확인 못함 (아래 tool failure 참고). "최초"라는 주장은 저자 주장이며 독립 재확인 안 됨 |
| B6 | ~~Key residue(예: His95 등 추가 pocket-lining residue)에 대한 구체적 residue-level 정보는 아직 확인되지 않음~~ → **Phase 4에서 해소됨, D3 참고** | PMC9106916 원문에는 residue-level 정보가 없었으나, 이후 자체 구조 분석(D3)으로 His95, Tyr96 등 pocket-lining residue를 직접 확인함 | (해소됨) | — | D3 참고 | — | 리뷰 논문 자체는 여전히 residue 상세를 언급하지 않음 — 이는 원자료(D3)로 보완됨 |

## C. Quantitative Evidence

| ID | Claim | Evidence | Evidence Type | Source | Identifier | Confidence | Limitation |
|---|---|---|---|---|---|---|---|
| C1 | Sotorasib은 MIAPaCa2 세포(KRAS G12C 보유)에서 EGF-stimulated ERK1/2 phosphorylation 감소로 측정 시 IC50 = 68 nM | ChEMBL activity record (cellular pERK inhibition assay) | Experimental Evidence | ChEMBL (via document) | ChEMBL target: GTPase KRas; document CHEMBL4354832 → PMID 31820981 (Lanman et al., J Med Chem 2020) | High | Cellular biochemical readout(pERK)이며 순수 biochemical binding IC50/Kd 아님. Assay 세부 조건(시간, 농도 range 등) 추가 확인 필요 |
| C2 | Sotorasib은 MIAPaCa2 세포 antiproliferation assay(72hr)에서 IC50 = 5.0 nM | ChEMBL activity record | Experimental Evidence | ChEMBL | 동일 document, PMID 31820981 | High | Cellular assay, 특정 cell line(MIAPaCa2)에 한정 — 다른 cell line/조건으로 일반화 불가 |
| C3 | A549 세포(KRAS G12S, 즉 G12C 아닌 mutant)에서는 antiproliferation IC50 = 36,500 nM로 훨씬 낮은 potency | ChEMBL activity record | Experimental Evidence | ChEMBL | 동일 document | High | G12C-selectivity를 시사하는 간접 근거이나, wild-type KRAS나 다른 세포주와의 직접 비교는 아님 |
| C4 | Sotorasib의 순수 biochemical binding assay (예: covalent labeling kinetics, 직접 Kd) 수치는 이번 조사에서 아직 확인되지 않음 | — | Not found | — | — | — | ChEMBL에서 조회된 activity 3건은 cellular assay뿐이었음(WebFetch 요약이 상위 결과만 반환했을 가능성 있어 전체 activity 목록 재확인 필요) |

## D. Structural Evidence

| ID | Claim | Evidence | Evidence Type | Source | Identifier | Confidence | Limitation |
|---|---|---|---|---|---|---|---|
| D1 | PDB 6OIM: Human KRAS(잔기 183aa 구성 엔트리), G12C, sotorasib(AMG 510) covalent, GDP, Mg2+ 포함, 해상도 1.65 Å | RCSB PDB entry data 직접 조회 | Observation | RCSB PDB | PDB ID 6OIM | High | Pocket 명칭(switch II)이나 개별 residue interaction 목록은 이 메타데이터 조회로는 확인 안 됨 — 별도 구조 분석(ligand interaction API 또는 PyMOL/구조 도구) 필요 |
| D2 | RCSB full-text 검색("sotorasib")으로 확인된 PDB 엔트리는 6OIM 외에 8UDR(항체-MHC-펩타이드 복합체, sotorasib-modified peptide) 등 소수 | RCSB Search API 결과 | Observation | RCSB PDB Search API | 8UDR (관련이나 KRAS 직접 결합 구조 아님, 면역 관련) | Medium | Full-text 검색이 "AMG 510" 등 이전 코드명으로 등록된 구조를 놓쳤을 가능성 있음 — ligand ID 기반 검색 필요 |
| D3 (Phase 4에서 확보, B6 해소) | Sotorasib(6OIM)의 pocket-lining residue(4.5 Å 이내 접촉)는 VAL9, GLY10, ALA11, CYS12, GLY13, LYS16, PRO34, THR58, ALA59, GLY60, GLN61, GLU62, GLU63, ARG68, ASP69, MET72, **HIS95**, **TYR96**, GLN99, ILE100, VAL103이다. His95/Tyr96를 포함함이 좌표 수준에서 직접 확인됨 | Biopython으로 6OIM 좌표를 직접 파싱하여 계산 (거리 cutoff 4.5 Å) | Observation (직접 계산, 재실행 가능) | 자체 분석 (`analysis/structural_comparison.py`, 입력은 RCSB PDB 6OIM) | PDB ID 6OIM; 분석 코드/출력: `analysis/structural_comparison.py`, `analysis/results_structural_comparison.md` | High (원자료 좌표 기반 직접 계산, 자체 도구로 재현 가능) | Cutoff(4.5 Å)은 임의 기준이며 문헌의 접촉 정의와 다를 수 있음. Asymmetric unit 내 첫 체인만 사용 |

## E. Biological Evidence

| ID | Claim | Evidence | Evidence Type | Source | Identifier | Confidence | Limitation |
|---|---|---|---|---|---|---|---|
| E1 | 위 C1 (pERK 감소)과 C2 (antiproliferation)가 cellular-level activity evidence에 해당 | 상동 | Experimental Evidence | 상동 | 상동 | High | in vitro cell line 데이터이며 animal model / tumor response 데이터는 별도(F 참고) |
| E2 | In vivo/animal 수준 evidence(예: xenograft tumor regression)는 이번 조사에서 원문 대조 못함 — Canon 2019 abstract에 "AMG 510 led to the regression of KRAS G12C tumours"라는 저자 주장은 있으나 수치/조건 미확인 | Canon et al. 2019 abstract (Europe PMC) | Literature Claim (수치 미확인) | Europe PMC | PMID 31666701 | Medium (abstract 수준 claim, 본문 미확인) | 정량적 tumor regression 데이터, 투여 조건, 모델 종류는 본문 확인 필요 (tool failure로 미확인) |

## F. Clinical Evidence

| ID | Claim | Evidence | Evidence Type | Source | Identifier | Confidence | Limitation |
|---|---|---|---|---|---|---|---|
| F1 | Sotorasib(LUMAKRAS)은 KRAS G12C-mutated 국소진행성/전이성 NSCLC 및 전이성 대장암(mCRC)에 대해 FDA 승인됨 | FDA label / Drugs@FDA | Database Annotation (규제기관 공식 정보) | OpenFDA label, Drugs@FDA (NDA214665) | NDA214665 | High | 승인은 특정 적응증/조건 하에 이루어졌으며 label 원문 세부 조건(line of therapy 등)은 별도 확인 필요 |
| F2 | CodeBreaK 200 (NCT04303780): Sotorasib vs Docetaxel 비교 Phase 3 trial, Amgen 후원, 완료됨(Completed) | ClinicalTrials.gov record | Database Annotation | ClinicalTrials.gov | NCT04303780 | High | Trial 결과(HR, PFS/OS 수치 등)는 이번 조사에서 아직 조회하지 않음 — outcomes 섹션 추가 조회 필요 |
| F3 | CodeBreaK 101 확장 연구(NCT04933695)는 Phase 2로 등록되었으나 상태가 TERMINATED | ClinicalTrials.gov record | Database Annotation | ClinicalTrials.gov | NCT04933695 | High | Termination 사유 미확인 — 안전성/전략적 이유 등 구분 필요, 별도 조회 필요 |

---

## Tool / Data Access Failures (기록)

| 시도 | 실패 내용 | 원인(추정) | 대응 |
|---|---|---|---|
| `mcp__biomcp__get entity=article id=31666701` (Canon et al. 2019, 원 sotorasib 논문) | "API error from pubtator3: Unexpected HTML response" — 반복 재현됨 (get, --raw 시도, tldr 섹션 모두 동일 오류) | 특정 PMID에 대한 PubTator3 백엔드 문제로 추정 (다른 PMID는 정상 작동 확인함, 예: 36383067, 24256730) | Europe PMC REST API(`ebi.ac.uk/europepmc/webservices/rest/search`)로 직접 abstract 확보하여 대체. 논문 본문(full text)은 구독 필요(Subscription required)로 미확인 |
| `mcp__biomcp__search entity=article` (Ostrem/Lito 관련 2차 검색) | "API error from pubtator3: Unexpected HTML response" (1회) | 일시적 backend 이슈로 추정 — 동일 유형 검색을 다른 표현으로 재시도했을 때는 정상 작동 | 특별한 대응 없이 대체 문구로 재시도하여 성공 |
| RCSB `www.rcsb.org/search?...` (브라우저 검색 UI) | PDB entry 목록을 가져오지 못함 (JS 렌더링 페이지) | 해당 URL은 SPA이며 서버사이드에 결과가 없음 | `search.rcsb.org/rcsbsearch/v2/query` REST API로 대체하여 성공 |
| `ebi.ac.uk/chembl/api/data/activity.json?molecule_chembl_id=...` | HTTP 500 | 잘못된 엔드포인트 형식(.json 확장자 방식 미지원 추정) | `?format=json` 파라미터 방식으로 재시도하여 성공 |
| ToolUniverse MCP 서버 | 세션 시작 시 연결 실패 (`uvx` 미설치) → 설치 완료했으나 이번 세션 내 재연결 미확인 (15분 재시도 캐시로 추정) | 환경 설정 문제, 코드/데이터 문제 아님 | BioMCP + RCSB REST API 직접 조회로 대체. 구조 residue-level interaction(예: His95 등 pocket-lining residue 목록), ligand alignment 등은 ToolUniverse 재연결 후 재시도 필요 |

---

## CHECKPOINT 2 관련 자체 점검 (아직 공식 체크포인트 아님 — RQ1 evidence만 우선 정리)

- 중요 claim(target identity, mutation, covalent mechanism, switch II pocket, PDB 구조, 승인 상태)에 evidence 존재: 대체로 확보됨.
- 독립 source 교차 확인: switch II pocket 개념(Ostrem 2013, 1차 문헌 직접 확인) + sotorasib 특이적 서술(Ganguly & Yoo 2022 review, 원문 직접 확인) + PDB 구조 관찰(RCSB, 원자료 직접 확인) 3개 독립 source가 covalent/switch-II/GDP-bound 결합을 일관되게 지지함.
- 아직 미확보: (1) residue-level pocket 상세 목록(His95 등), (2) 순수 biochemical binding Kd, (3) CodeBreaK 200 정량적 임상 결과, (4) Canon 2019 논문 본문(regression 데이터 수치).
- Biochemical(C1은 사실 cellular pERK) vs cellular(C2) 구분: C1은 표기상 "biochemical"이 아니라 cellular pERK assay였음 — 초기 evidence 계획에서 가정한 "biochemical activity" 항목은 아직 채워지지 않음.

이 상태로 RQ2 (Ligand Landscape, 다른 KRAS G12C 리간드 비교)로 넘어가기 전에 검토를 요청합니다.

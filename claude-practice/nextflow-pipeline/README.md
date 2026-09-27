# KRAS G12C 구조 비교 파이프라인

연구 산출물 중 **Phase 4 비교 분석**([analysis/04_comparative_analysis.md](../analysis/04_comparative_analysis.md))을
재실행 가능한 Nextflow 파이프라인으로 재구성한 것입니다.

원래 분석은 [analysis/structural_comparison.py](../analysis/structural_comparison.py) 한 파일이
네 구조를 한 번에 처리하는 방식이었습니다. 이 파이프라인은 같은 분석을 단계별 process로 나누어,
구조를 추가하거나 파라미터를 바꿔도 **바뀐 부분만 다시 실행**되도록 만든 것입니다.

---

## 파일 구성

| 경로 | 내용 |
| --- | --- |
| `main.nf` | 파이프라인 본체 — process 4개와 workflow 정의 |
| `nextflow.config` | 파라미터 기본값 (입력 경로, 기준 구조, 접촉 거리, 출력 경로) |
| `assets/structures.csv` | 분석 대상 구조 목록 (samplesheet) |
| `bin/pocket_residues.py` | 리간드와 접촉하는 KRAS 잔기 계산 |
| `bin/superpose_switch2.py` | 기준 구조에 중첩 후 switch-II 변위 측정 |
| `bin/build_report.py` | 결과 통합 — consensus pocket + 비교 리포트 |

`bin/` 아래 스크립트는 Nextflow가 자동으로 `PATH`에 추가하므로 process에서 이름만으로 호출합니다.

## 분석 흐름

```text
structures.csv
      │
      ▼
FETCH_STRUCTURE      RCSB PDB에서 구조 원자료 다운로드 (구조당 1개)
      │
      ├──────────────▶ POCKET_RESIDUES     리간드 접촉 잔기 계산 (구조당 병렬)
      │                      │
      └──────────────▶ SUPERPOSE_SWITCH2   기준 구조 대비 switch-II 변위 (기준 제외)
                             │
                             ▼
                      BUILD_REPORT         결과 통합 → 리포트 + consensus pocket
```

기준 구조(`params.reference`, 기본값 `sotorasib`)는 중첩의 기준이므로
`SUPERPOSE_SWITCH2`에서는 제외됩니다. 구조 4개 중 3개만 중첩 대상이 되는 이유입니다.

## 실행

### 구조만 확인하기 (stub 실행)

각 process의 `stub` 블록만 실행하여 **파이프라인 구조가 올바른지 몇 초 만에 확인**합니다.
네트워크도 Python 패키지도 필요 없습니다.

```bash
nextflow run main.nf -stub-run
```

`FETCH_STRUCTURE 4, POCKET_RESIDUES 4, SUPERPOSE_SWITCH2 3, BUILD_REPORT 1`,
합계 12개 task가 완료되면 정상입니다.

### 실제로 분석하기

구조 다운로드(네트워크)와 Biopython이 필요합니다.

```bash
pip install biopython numpy
nextflow run main.nf
```

결과는 `results/` 아래에 생성됩니다.

| 경로 | 내용 |
| --- | --- |
| `results/structures/` | 내려받은 원자료 (PDB / mmCIF) |
| `results/pocket/` | 구조별 접촉 잔기 목록 |
| `results/switch2/` | 구조별 switch-II 변위 수치 |
| `results/comparison_report.md` | 통합 비교 리포트 |
| `results/consensus_pocket.tsv` | 잔기별로 몇 개 구조에서 나타났는지 |

### 파라미터 바꿔보기

```bash
# 접촉 기준 거리를 4.0 A로
nextflow run main.nf --cutoff 4.0

# 기준 구조를 adagrasib으로
nextflow run main.nf --reference adagrasib

# 앞서 실행한 결과를 재사용하고 바뀐 단계만 다시 실행
nextflow run main.nf -resume
```

## 검증

이 파이프라인의 계산 결과는 원 분석([analysis/results_structural_comparison.md](../analysis/results_structural_comparison.md))과
일치합니다. 예를 들어 divarasib(9DMM)의 경우:

| 항목 | 원 분석 | 이 파이프라인 |
| --- | --- | --- |
| Core superposition RMSD | 0.48 A (n=127) | 0.48 A (n=127) |
| Residue 65 CA delta | 5.52 A | 5.52 A |
| Switch-II mean / max delta | 2.38 / 5.97 A | 2.38 / 5.97 A |

**같은 입력에서 같은 수치가 나오는 것**이 재현 가능한 분석의 최소 조건입니다.

## 한계

- 각 구조의 asymmetric unit 중 KRAS로 보이는 첫 번째 사슬만 사용합니다 (6UT0은 4개 체인 중 1개).
- 접촉 기준 4.5 A는 임의로 정한 값이며 문헌의 정의(예: 4.0 A)와 다를 수 있습니다.
- Olomorasib은 실험 구조가 없어 분석 대상에서 빠져 있습니다.
- 이 파이프라인의 출력은 Observation 수준입니다. 관찰된 거리 차이를
  binding affinity 차이의 '원인'으로 해석하지 않습니다.

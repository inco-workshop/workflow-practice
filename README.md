

# KOBIC 오프라인 교육 (26-09-28)

[1. 실습 환경 세팅](#1-실습-환경-세팅)

[2. Nextflow 실습](#2-nextflow-실습)

​	[2.1 Nextflow 기본](#21-nextflow-기본)

​	[2.2 Nextflow 출력 경로 설정](#22-nextflow-출력-경로-설정)

​	[2.3 Nextflow 변수 설정](#23-nextflow-변수-설정)

[3. nf-core/oncoanalyser 실습](#3-nf-coreoncoanalyser-실습)

[4. Claude Code 실습](#4-claude-code-실습)

---------

## 1. 리눅스 명령어

| 리눅스 명령어 | 기능                        |
| ------------- | --------------------------- |
| pwd           | 현재 경로 확인              |
| ll            | 현재 디렉토리 확인          |
| cd            | 디렉토리로 이동             |
| cd ..         | 하위 디렉토리로 이동        |
| cat {파일명}  | {파일} 내용을 터미널에 출력 |
| vim           | 텍스트 파일 수정            |



## 2. Nextflow 실습

### 2.1 Nextflow 기본

---

**Step 1.** 실습 디렉토리 살펴봅니다. (리눅스 명령어는 아래 참고)

```bash
ll
```

**Step 2.** hello-world.nf 스크립트를 살펴봅니다. (process, workflow, output, script)

```bash
# hello-nextflow 디렉토리로 접근합니다. (tap을 누르시면 더 빨라요!)
cd hello-nextflow

# hello-nextflow 디렉토리의 하위 항목을 출력합니다.
ll

# hello-world.nf 파일을 읽어봅니다.
cat hello-world.nf
```

**Step 3.** hello-world.nf 스크립트를 구동합니다. (Step, Hash)

```bash
# nextflow run [nf 스크립트]
nextflow run hello-world.nf
```

**Step 4.** 결과를 확인합니다. (work)

```bash
# hello-world.nf 구동 결과 확인
ll

# work 디렉토리 접근
cd work

# work 디렉토리 결과 확인
tree

# 상위 디렉토리로 이동합니다.
cd ..
```



### 2.2 Nextflow 출력 경로 설정

---

**Step 1.** 왼쪽 파일 탐색기에서 `hello-world.nf` 파일을 더블클릭하여 에디터로 엽니다.

```bash
# 터미널에서 열고 싶다면
code hello-world.nf
```

**Step 2.** `publishDir` function 을 추가합니다. (indentation)

```bash
process sayHello {
    publishDir 'results', mode: 'copy'

    output: # 이하 생략
```

**Step 3.** 파일을 저장합니다. (`Ctrl+S`, Mac은 `Cmd+S`)

> (선택) vim이 익숙하다면: `vim hello-world.nf` → `a`로 수정 모드 진입 → 수정 → [ESC] - `:wq!` - [ENTER]

**Step 4.** hello-world.nf 스크립트를 구동 후, 결과를 확인합니다. (Resume)

```bash
# nextflow run [nf 스크립트]
nextflow run hello-world.nf -resume
```

**Step 5.** `results` 디렉토리에서 결과를 확인합니다.

```bash
cd results
cat output.txt
```



### 2.3 Nextflow 변수 설정

---

**Step 1.** 에디터에서 `hello-world.nf` 파일을 다시 엽니다. (더블클릭 또는 `code hello-world.nf`)

**Step 2.** `input` 설정, `script` 수정, `workflow` 수정 합니다.

```bash
process sayHello {
    publishDir 'results', mode: 'copy'

    input: # 추가(1)
        val greeting  # 추가(2)

    output:
        path 'output.txt'

    script:
    """
    echo "$greeting" > output.txt # 수정
    """
}

workflow {
    sayHello(params.greeting) # 수정
}
```

**Step 3.** 파일을 저장합니다. (`Ctrl+S`, Mac은 `Cmd+S`)

**Step 4.** hello-world.nf 스크립트를 구동 후, 결과를 확인합니다. (Resume)

```bash
# nextflow run [nf 스크립트]
nextflow run hello-world.nf --greeting "Hello, my name is Sohee"
```

**Step 5.** `results` 디렉토리에서 결과를 확인합니다.

```bash
cd results
cat output.txt
```



## 3. nf-core/oncoanalyser 실습

**Step 1.** `oncoanalyser` 디렉토리로 이동합니다. (`cd ..` 활용)

**Step 2.** nf-core 에서 파이프라인을 찾아봅니다.

```bash
nf-core pipelines list
```

**Step 3.** nf-core/oncoanalyser 실행을 위해 파이프라인을 내려받습니다.

```bash
nextflow pull nf-core/oncoanalyser -r 2.1.0
nextflow pull nf-core/oncoanalyser -r 2.3.0
```

**Step 4.** nf-core/oncoanalyser를 구동합니다.

```bash
nextflow run nf-core/oncoanalyser -r 2.1.0 -profile docker,test --outdir ./
nextflow run nf-core/oncoanalyser -r 2.3.0 -profile docker,test --outdir ./
```



## 4. Claude Code 실습

**Step 1.** `claude-practice` 디렉토리로 이동합니다.

```bash
cd claude-practice
```

**Step 2.** 실습 안내는 [claude-practice/README.md](claude-practice/README.md)를 참고합니다.

연구 규칙과 워크플로우는 [claude-practice/CLAUDE.md](claude-practice/CLAUDE.md)에 정의되어 있고,
`claude-practice` 디렉토리에서 Claude Code를 실행하면 자동으로 읽습니다.



26.09.28, (주)인실리코젠, 박소희

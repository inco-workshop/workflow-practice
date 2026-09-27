# Cheatsheet — Nextflow 실습 정답

실습 중 막히면 아래 완성본과 본인 코드를 비교하세요.
원본 정답 파일은 [solutions/](solutions/) 디렉토리에 있습니다.

---

## 2.2 Nextflow 출력 경로 설정 — 완성본

`publishDir`를 추가한 상태입니다. (원본: [solutions/1-hello-world/hello-world-3.nf](solutions/1-hello-world/hello-world-3.nf))

```nextflow
#!/usr/bin/env nextflow

process sayHello {

    publishDir 'results', mode: 'copy'

    output:
        path 'output.txt'

    script:
    """
    echo 'Hello World!' > output.txt
    """
}

workflow {
    sayHello()
}
```

실행:

```bash
nextflow run hello-world.nf -resume
cat results/output.txt
```

---

## 2.3 Nextflow 변수 설정 — 완성본

`input`을 추가하고 `script`와 `workflow`를 수정한 상태입니다.
(원본: [solutions/1-hello-world/hello-world-4.nf](solutions/1-hello-world/hello-world-4.nf))

```nextflow
#!/usr/bin/env nextflow

process sayHello {

    publishDir 'results', mode: 'copy'

    input:
        val greeting

    output:
        path 'output.txt'

    script:
    """
    echo '$greeting' > output.txt
    """
}

workflow {
    sayHello(params.greeting)
}
```

실행:

```bash
nextflow run hello-world.nf --greeting "Hello, my name is Sohee"
cat results/output.txt
```

> 참고: solutions의 정답 파일에는 `params.greeting = 'Holà mundo!'` 기본값 선언이
> 추가로 들어 있습니다. 기본값을 선언해 두면 `--greeting` 없이 실행해도 동작합니다.

---

## 자주 나오는 문제

| 증상 | 원인 / 해결 |
| --- | --- |
| `results` 디렉토리가 안 생김 | `publishDir` 줄이 `process` 블록 안에 있는지, 들여쓰기를 확인 |
| `No such variable: greeting` | `input:` 블록 추가 여부와 `workflow`에서 `sayHello(params.greeting)`로 호출했는지 확인 |
| 수정했는데 결과가 그대로 | `-resume`은 캐시를 재사용합니다. 스크립트 수정 후에는 해당 process가 다시 실행되는 게 정상이니, `results/output.txt`를 다시 확인 |
| vim에서 못 나감 | `ESC` 누른 뒤 `:wq!` + `ENTER` |

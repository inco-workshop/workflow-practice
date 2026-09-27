#!/usr/bin/env nextflow

/*
 * KRAS G12C 구조 비교 파이프라인
 *
 * claude-practice의 연구 산출물 중 Phase 4 비교 분석
 * (analysis/structural_comparison.py)을 재실행 가능한 형태로 재구성한 것이다.
 *
 * 분석 흐름:
 *   1) RCSB PDB에서 구조 원자료를 내려받고
 *   2) 구조마다 리간드와 접촉하는 KRAS 잔기(pocket)를 계산한 뒤
 *   3) 기준 구조(sotorasib)에 중첩하여 switch-II loop 변위를 측정하고
 *   4) 결과를 하나의 비교 리포트로 합친다.
 */


/*
 * 1. 구조 원자료 다운로드
 */
process FETCH_STRUCTURE {

    tag "${meta.name}"

    publishDir "${params.outdir}/structures", mode: 'copy'

    input:
        val meta

    output:
        tuple val(meta), path("${meta.pdb_id}.${meta.format}")

    script:
    """
    curl -fsSL https://files.rcsb.org/download/${meta.pdb_id}.${meta.format} \\
        -o ${meta.pdb_id}.${meta.format}
    """

    stub:
    """
    touch ${meta.pdb_id}.${meta.format}
    """
}


/*
 * 2. Pocket-lining residue 계산
 *    리간드 중원자로부터 cutoff 이내에 있는 KRAS 잔기를 찾는다.
 */
process POCKET_RESIDUES {

    tag "${meta.name}"

    publishDir "${params.outdir}/pocket", mode: 'copy'

    input:
        tuple val(meta), path(structure)

    output:
        path "${meta.name}_pocket.tsv"

    script:
    """
    pocket_residues.py \\
        --structure ${structure} \\
        --name ${meta.name} \\
        --chains '${meta.chains}' \\
        --cutoff ${params.cutoff} \\
        --out ${meta.name}_pocket.tsv
    """

    stub:
    """
    printf 'ligand\\tligand_resname\\tkras_chain\\tresidue_id\\tresidue_name\\n' > ${meta.name}_pocket.tsv
    printf '${meta.name}\\tSTUB\\tA\\t12\\tCYS\\n' >> ${meta.name}_pocket.tsv
    """
}


/*
 * 3. 기준 구조에 중첩하여 switch-II loop 변위 측정
 *    switch-I / switch-II를 제외한 core 잔기로 중첩하므로,
 *    switch-II 자체의 움직임이 측정 대상으로 남는다.
 */
process SUPERPOSE_SWITCH2 {

    tag "${meta.name}"

    publishDir "${params.outdir}/switch2", mode: 'copy'

    input:
        tuple val(meta), path(mobile), path(reference)

    output:
        path "${meta.name}_switch2.tsv"

    script:
    """
    superpose_switch2.py \\
        --reference ${reference} \\
        --mobile ${mobile} \\
        --name ${meta.name} \\
        --chains '${meta.chains}' \\
        --out ${meta.name}_switch2.tsv
    """

    stub:
    """
    printf 'ligand\\tcore_rmsd_A\\tn_core_atoms\\tresid65_delta_A\\tswitchII_mean_delta_A\\tswitchII_max_delta_A\\n' > ${meta.name}_switch2.tsv
    printf '${meta.name}\\t0.00\\t0\\t0.00\\t0.00\\t0.00\\n' >> ${meta.name}_switch2.tsv
    """
}


/*
 * 4. 결과 통합 — consensus pocket 도출 및 비교 리포트 작성
 */
process BUILD_REPORT {

    publishDir "${params.outdir}", mode: 'copy'

    input:
        path pocket_tsv
        path switch2_tsv

    output:
        path "comparison_report.md"
        path "consensus_pocket.tsv"

    script:
    """
    build_report.py \\
        --pocket ${pocket_tsv} \\
        --switch2 ${switch2_tsv} \\
        --reference ${params.reference} \\
        --cutoff ${params.cutoff} \\
        --out-report comparison_report.md \\
        --out-consensus consensus_pocket.tsv
    """

    stub:
    """
    printf '# Comparison Report (stub)\\n' > comparison_report.md
    printf 'residue_id\\tresidue_name\\tn_structures\\n' > consensus_pocket.tsv
    """
}


workflow {

    // samplesheet에서 분석 대상 구조 목록을 읽는다
    ch_structures = Channel
        .fromPath(params.input, checkIfExists: true)
        .splitCsv(header: true)
        .map { row ->
            [
                name   : row.name,
                pdb_id : row.pdb_id,
                format : row.format,
                chains : row.chains
            ]
        }

    // 1. 구조 다운로드
    ch_fetched = FETCH_STRUCTURE(ch_structures)

    // 2. 구조마다 pocket 잔기 계산 (구조 수만큼 병렬 실행)
    ch_pocket = POCKET_RESIDUES(ch_fetched)

    // 3. 기준 구조와 나머지 구조를 나눈 뒤, 나머지를 기준에 중첩
    ch_fetched
        .branch { meta, structure ->
            reference: meta.name == params.reference
            mobile   : true
        }
        .set { ch_branched }

    ch_reference = ch_branched.reference.map { meta, structure -> structure }

    ch_switch2 = SUPERPOSE_SWITCH2(ch_branched.mobile.combine(ch_reference))

    // 4. 모든 결과를 모아 리포트 작성
    BUILD_REPORT(ch_pocket.collect(), ch_switch2.collect())
}

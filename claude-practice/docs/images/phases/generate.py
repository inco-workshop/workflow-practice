#!/usr/bin/env python3
"""Phase별 설명 이미지(HTML) 생성 → 이후 headless Chrome으로 PNG 변환."""

from pathlib import Path

OUT = Path(__file__).parent / "phases"
OUT.mkdir(exist_ok=True)

BLUE = "#0B5FFF"
NAVY = "#10233F"
MUTED = "#5B6B7F"
LIGHT = "#E8F0FE"
GREEN = "#17A673"
ORANGE = "#F08C2E"
PANEL = "#F5F8FC"
BORDER = "#D9E2EF"


# ---------------------------------------------------------------- 일러스트
def protein(x, y, scale=1.0, notch=True, color=BLUE, opacity=0.18):
    """포켓(notch)이 있는 추상 단백질 덩어리."""
    notch_path = (
        f'<path d="M 96 74 q 18 -22 38 -6 q 16 13 2 32 q -16 21 -36 8 q -16 -11 -4 -34 Z" '
        f'fill="#fff" stroke="{color}" stroke-width="3"/>'
        if notch else ""
    )
    return f'''<g transform="translate({x},{y}) scale({scale})">
  <path d="M30 60 q-22 40 6 74 q24 30 66 30 q56 2 78 -34 q22 -36 -4 -70
           q-26 -34 -74 -32 q-50 2 -72 32 Z"
        fill="{color}" fill-opacity="{opacity}" stroke="{color}" stroke-width="3"/>
  <path d="M46 96 q16 -20 34 -4 M64 130 q20 -18 38 -2 M120 118 q18 -16 34 -2"
        fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" opacity="0.5"/>
  {notch_path}
</g>'''


def molecule(x, y, scale=1.0, color=NAVY):
    """육각 고리 + 치환기 = 소분자."""
    return f'''<g transform="translate({x},{y}) scale({scale})">
  <polygon points="20,0 40,11 40,34 20,45 0,34 0,11"
           fill="none" stroke="{color}" stroke-width="3"/>
  <line x1="40" y1="22" x2="62" y2="22" stroke="{color}" stroke-width="3"/>
  <circle cx="68" cy="22" r="7" fill="{color}"/>
  <line x1="20" y1="45" x2="20" y2="62" stroke="{color}" stroke-width="3"/>
  <circle cx="20" cy="68" r="6" fill="none" stroke="{color}" stroke-width="3"/>
</g>'''


def database(x, y, label, color=BLUE):
    return f'''<g transform="translate({x},{y})">
  <ellipse cx="34" cy="12" rx="34" ry="12" fill="{LIGHT}" stroke="{color}" stroke-width="3"/>
  <path d="M0 12 V54 a34 12 0 0 0 68 0 V12" fill="{LIGHT}" stroke="{color}" stroke-width="3"/>
  <ellipse cx="34" cy="33" rx="34" ry="12" fill="none" stroke="{color}" stroke-width="2" opacity="0.5"/>
  <text x="34" y="86" text-anchor="middle" font-size="17" fill="{MUTED}">{label}</text>
</g>'''


def card(x, y, w, h, title, tone=BLUE):
    return f'''<g transform="translate({x},{y})">
  <rect width="{w}" height="{h}" rx="10" fill="#fff" stroke="{tone}" stroke-width="2.5"/>
  <rect width="6" height="{h}" rx="3" fill="{tone}"/>
  <text x="20" y="{h/2+7}" font-size="19" fill="{NAVY}">{title}</text>
</g>'''


def magnifier(x, y, scale=1.0, color=ORANGE):
    return f'''<g transform="translate({x},{y}) scale({scale})">
  <circle cx="30" cy="30" r="26" fill="#fff" fill-opacity="0.65" stroke="{color}" stroke-width="5"/>
  <line x1="49" y1="49" x2="70" y2="70" stroke="{color}" stroke-width="7" stroke-linecap="round"/>
</g>'''


def helix(x, y, w=250, color=BLUE, dash=False):
    """알파 헬릭스 느낌의 리본."""
    seg = w / 6
    d = f"M0,30"
    for i in range(6):
        d += f" q{seg/2},{-46 if i%2==0 else 46} {seg},0"
    da = ' stroke-dasharray="9 7"' if dash else ""
    return (f'<g transform="translate({x},{y})">'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="7" '
            f'stroke-linecap="round"{da}/></g>')


# ---------------------------------------------------------------- Phase별 그림
def art_plan():
    return f'''<svg viewBox="0 0 620 420" width="620" height="420">
  <defs><pattern id="g" width="34" height="34" patternUnits="userSpaceOnUse">
    <path d="M34 0 H0 V34" fill="none" stroke="{BORDER}" stroke-width="1"/></pattern></defs>
  <rect width="620" height="420" fill="url(#g)" opacity="0.9"/>
  {protein(30, 120, 1.0)}
  <text x="120" y="66" font-size="58" fill="{BLUE}" font-weight="700">?</text>
  <path d="M250 150 H300 M300 150 V86 H360 M300 150 V214 H360 M300 150 H360"
        fill="none" stroke="{BLUE}" stroke-width="3"/>
  {card(360, 60, 230, 52, "어떤 근거가 필요한가")}
  {card(360, 124, 230, 52, "어디서 찾을 것인가")}
  {card(360, 188, 230, 52, "어떻게 검증하는가")}
  <rect x="360" y="276" width="230" height="62" rx="10" fill="{LIGHT}" stroke="{BLUE}"
        stroke-width="2.5" stroke-dasharray="8 6"/>
  <text x="475" y="313" text-anchor="middle" font-size="19" fill="{BLUE}"
        font-weight="600">CHECKPOINT 1 · 사람 검토</text>
</svg>'''


def art_evidence():
    dbs = "".join(database(30 + i * 108, 60, lbl)
                  for i, lbl in enumerate(["PubMed", "ClinVar", "PDB"]))
    tags = ""
    for i, (t, c) in enumerate([("Observation", GREEN), ("Literature", BLUE),
                                ("Inference", ORANGE), ("Not found", MUTED)]):
        tags += f'''<g transform="translate(370,{62+i*74})">
  <rect width="230" height="54" rx="10" fill="#fff" stroke="{c}" stroke-width="2.5"/>
  <circle cx="26" cy="27" r="8" fill="{c}"/>
  <text x="48" y="34" font-size="19" fill="{NAVY}">{t}</text></g>'''
    return f'''<svg viewBox="0 0 620 420" width="620" height="420">
  {dbs}
  <path d="M170 210 V250 H300 M300 250 H340" fill="none" stroke="{BLUE}" stroke-width="3"/>
  <path d="M332 244 l10 6 l-10 6 Z" fill="{BLUE}"/>
  {tags}
  <text x="30" y="300" font-size="18" fill="{MUTED}">찾지 못한 것도</text>
  <text x="30" y="326" font-size="18" fill="{MUTED}">기록한다</text>
</svg>'''


def art_ligand():
    mols = (molecule(20, 40, 0.95) + molecule(20, 250, 0.95)
            + molecule(430, 40, 0.95) + molecule(430, 250, 0.95))
    return f'''<svg viewBox="0 0 620 420" width="620" height="420">
  {protein(215, 120, 1.05)}
  {mols}
  <g stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="7 6" fill="none">
    <path d="M130 90 L270 180"/><path d="M130 300 L270 230"/>
    <path d="M520 100 L400 180"/><path d="M520 300 L400 235"/>
  </g>
  <text x="310" y="392" text-anchor="middle" font-size="19" fill="{MUTED}">
    같은 pocket을 쓰는가 · 개발 단계는 · 활성은</text>
</svg>'''


def art_compare():
    return f'''<svg viewBox="0 0 620 420" width="620" height="420">
  {helix(60, 90, 300, BLUE)}
  {helix(60, 150, 300, ORANGE, dash=True)}
  <line x1="372" y1="120" x2="372" y2="180" stroke="{NAVY}" stroke-width="3"/>
  <path d="M366 126 L372 116 L378 126 Z M366 174 L372 184 L378 174 Z" fill="{NAVY}"/>
  <text x="390" y="157" font-size="26" fill="{NAVY}" font-weight="700">5.52 Å</text>
  <text x="390" y="184" font-size="17" fill="{MUTED}">switch-II 변위</text>
  <rect x="60" y="250" width="500" height="128" rx="12" fill="{PANEL}" stroke="{BORDER}" stroke-width="2"/>
  <text x="84" y="286" font-size="19" fill="{MUTED}">공통 접촉 잔기</text>
  <text x="84" y="326" font-size="27" fill="{NAVY}" font-weight="700">Cys12 · His95 · Tyr96 · Gln99</text>
  <text x="84" y="358" font-size="17" fill="{GREEN}">좌표에서 직접 계산 — Observation</text>
</svg>'''


def art_rank():
    tiers = ""
    for i, (t, h, c) in enumerate([("A", 150, BLUE), ("B", 104, "#7FA8FF"), ("C", 62, "#B9CCF2")]):
        x = 70 + i * 128
        tiers += f'''<rect x="{x}" y="{250-h}" width="104" height="{h}" rx="8" fill="{c}"/>
  <text x="{x+52}" y="{250-h+38}" text-anchor="middle" font-size="30" fill="#fff"
        font-weight="700">{t}</text>'''
    steps = ""
    for i, (t, c) in enumerate([("Evidence", GREEN), ("Interpretation", BLUE),
                                ("Limitation", ORANGE), ("Hypothesis", NAVY)]):
        steps += f'''<g transform="translate(60,{288+i*32})">
  <circle cx="8" cy="-6" r="6" fill="{c}"/>
  <text x="26" y="0" font-size="19" fill="{NAVY}">{t}</text></g>'''
    return f'''<svg viewBox="0 0 620 420" width="620" height="420">
  {molecule(430, 40, 0.85)}
  {tiers}
  <line x1="60" y1="250" x2="560" y2="250" stroke="{NAVY}" stroke-width="3"/>
  {steps}
  <text x="330" y="330" font-size="19" fill="{MUTED}">확정된 신약이 아니라</text>
  <text x="330" y="360" font-size="21" fill="{NAVY}" font-weight="700">candidate hypothesis</text>
</svg>'''


def art_audit():
    rows = ""
    for i, (t, ok) in enumerate([("citation이 claim을 지지하는가", True),
                                 ("수치와 단위가 원자료와 같은가", True),
                                 ("계산값을 실험값처럼 쓰지 않았는가", True),
                                 ("결론이 근거보다 강하지 않은가", False)]):
        c = GREEN if ok else ORANGE
        mark = ("M0 8 L7 15 L18 1" if ok else "M0 0 L16 16 M16 0 L0 16")
        rows += f'''<g transform="translate(40,{60+i*76})">
  <rect width="430" height="58" rx="10" fill="#fff" stroke="{BORDER}" stroke-width="2"/>
  <g transform="translate(22,21)" stroke="{c}" stroke-width="4" fill="none"
     stroke-linecap="round"><path d="{mark}"/></g>
  <text x="62" y="36" font-size="19" fill="{NAVY}">{t}</text></g>'''
    return f'''<svg viewBox="0 0 620 420" width="620" height="420">
  {rows}
  {magnifier(452, 268, 1.25)}
  <g font-size="17" fill="{MUTED}">
    <text x="40" y="404">PMID · DOI · PDB ID · ChEMBL ID 로 원자료 재확인</text>
  </g>
</svg>'''


def art_final():
    return f'''<svg viewBox="0 0 620 420" width="620" height="420">
  <g transform="translate(46,40)">
    <rect width="270" height="330" rx="12" fill="#fff" stroke="{BLUE}" stroke-width="3"/>
    <rect x="28" y="34" width="150" height="15" rx="7" fill="{NAVY}"/>
    <g fill="{BORDER}">
      <rect x="28" y="76" width="214" height="11" rx="5"/>
      <rect x="28" y="100" width="190" height="11" rx="5"/>
      <rect x="28" y="124" width="214" height="11" rx="5"/>
    </g>
    <rect x="28" y="158" width="214" height="62" rx="8" fill="{PANEL}" stroke="{BORDER}" stroke-width="2"/>
    <text x="44" y="196" font-size="17" fill="{MUTED}">Remaining gaps</text>
    <g fill="{BORDER}">
      <rect x="28" y="244" width="214" height="11" rx="5"/>
      <rect x="28" y="268" width="160" height="11" rx="5"/>
    </g>
  </g>
  <g stroke="{GREEN}" stroke-width="3" fill="none">
    <path d="M336 200 H392"/><path d="M384 194 l10 6 l-10 6" fill="{GREEN}"/>
  </g>
  <g transform="translate(404,96)">
    <rect width="176" height="72" rx="10" fill="{LIGHT}" stroke="{BLUE}" stroke-width="2.5"/>
    <text x="88" y="44" text-anchor="middle" font-size="19" fill="{NAVY}">분석 코드</text>
  </g>
  <g transform="translate(404,182)">
    <rect width="176" height="72" rx="10" fill="{LIGHT}" stroke="{BLUE}" stroke-width="2.5"/>
    <text x="88" y="44" text-anchor="middle" font-size="19" fill="{NAVY}">원자료 · ID</text>
  </g>
  <g transform="translate(404,268)">
    <rect width="176" height="72" rx="10" fill="{LIGHT}" stroke="{BLUE}" stroke-width="2.5"/>
    <text x="88" y="44" text-anchor="middle" font-size="19" fill="{NAVY}">실행 기록</text>
  </g>
  <text x="492" y="376" text-anchor="middle" font-size="18" fill="{GREEN}"
        font-weight="600">다시 확인할 수 있는 답</text>
</svg>'''


# ---------------------------------------------------------------- 페이지 내용
PHASES = [
    dict(no="PHASE 1", ko="연구 계획 수립", en="Research Plan",
         q="무엇을, 어떤 근거로 확인할 것인가?",
         bullets=["연구 질문을 검증 가능한 형태로 분해한다",
                  "필요한 evidence와 data source를 미리 정의한다",
                  "계획을 사람이 검토한 뒤에야 다음 단계로 간다"],
         file="01_research_plan.md", art=art_plan()),
    dict(no="PHASE 2", ko="근거 수집", en="Evidence Hunt",
         q="KRAS G12C와 sotorasib에 대해 무엇이 알려져 있는가?",
         bullets=["변이·약물·구조·임상 근거를 영역별로 모은다",
                  "근거의 종류를 관찰 / 문헌 / 추론으로 구분한다",
                  "찾지 못한 것도 Not found로 남긴다"],
         file="02_evidence_table.md", art=art_evidence()),
    dict(no="PHASE 3", ko="리간드 지형도", en="Ligand Landscape",
         q="KRAS G12C에 결합하는 화합물은 무엇이 있는가?",
         bullets=["후보 리간드를 열거하고 포함 이유를 기록한다",
                  "결합 부위·결합 방식·개발 단계를 함께 정리한다",
                  "조건이 다른 수치는 직접 비교하지 않는다"],
         file="03_ligand_landscape.md", art=art_ligand()),
    dict(no="PHASE 4", ko="비교 분석", en="Comparative Analysis",
         q="같은 pocket을 쓰는가, 무엇이 다른가?",
         bullets=["구조를 중첩해 switch-II 변위를 직접 측정한다",
                  "리간드와 접촉하는 잔기를 좌표에서 계산한다",
                  "문헌의 주장을 원자료로 다시 확인한다"],
         file="analysis/04_comparative_analysis.md", art=art_compare()),
    dict(no="PHASE 5", ko="후보 우선순위", en="Candidate Prioritization",
         q="무엇을 먼저 검증해야 하는가?",
         bullets=["결과를 보기 전에 정한 기준으로 평가한다",
                  "근거·해석·한계·가설을 분리해 쓴다",
                  "근거가 빈약한 후보가 점수로 올라가지 않게 한다"],
         file="04_candidate_ranking.md", art=art_rank()),
    dict(no="PHASE 6", ko="검증 감사", en="Verification Audit",
         q="이 결론은 근거보다 강하지 않은가?",
         bullets=["핵심 claim을 원자료 identifier로 재확인한다",
                  "citation이 그 주장을 실제로 지지하는지 본다",
                  "계산 예측값을 실험값처럼 쓰지 않았는지 본다"],
         file="05_verification_audit.md", art=art_audit()),
    dict(no="FINAL", ko="최종 보고", en="Final Report",
         q="다른 연구자가 다시 확인할 수 있는가?",
         bullets=["결론과 함께 남은 gap, 다음 실험을 제안한다",
                  "분석 코드·원자료·실행 기록을 함께 남긴다",
                  "정답이 아니라 재현 가능한 과정을 산출물로 삼는다"],
         file="results/final_report.md", art=art_final()),
]

TPL = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><style>
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1600px; height:900px; background:#fff; overflow:hidden;
  font-family:"Apple SD Gothic Neo","Noto Sans KR","Helvetica Neue",sans-serif;
  color:__NAVY__; }
.wrap { padding:72px 80px; height:100%; display:flex; flex-direction:column; }
.top { display:flex; justify-content:space-between; align-items:flex-start; }
.no { font-size:24px; letter-spacing:4px; color:__BLUE__; font-weight:700; }
.ko { font-size:62px; font-weight:800; margin-top:10px; letter-spacing:-1px; }
.en { font-size:26px; color:__MUTED__; margin-top:8px; letter-spacing:1px; }
.file { font-size:22px; color:__BLUE__; background:__LIGHT__; border-radius:999px;
  padding:14px 26px; font-family:ui-monospace,Menlo,monospace; }
.rule { width:92px; height:7px; background:__BLUE__; border-radius:4px; margin:30px 0 26px; }
.q { font-size:34px; font-weight:700; color:__NAVY__; }
.body { display:flex; gap:64px; align-items:center; flex:1; margin-top:26px; }
ul { list-style:none; }
li { font-size:27px; line-height:1.55; color:#26364F; margin-bottom:26px;
  padding-left:38px; position:relative; }
li:before { content:""; position:absolute; left:0; top:15px; width:18px; height:18px;
  border-radius:50%; background:__LIGHT__; border:4px solid __BLUE__; }
.foot { border-top:2px solid __BORDER__; padding-top:22px; display:flex;
  justify-content:space-between; font-size:20px; color:__MUTED__; }
.foot b { color:__NAVY__; }
</style></head><body><div class="wrap">
  <div class="top">
    <div><div class="no">__NO__</div><div class="ko">__KO__</div><div class="en">__EN__</div></div>
    <div class="file">__FILE__</div>
  </div>
  <div class="rule"></div>
  <div class="q">__Q__</div>
  <div class="body"><div>__ART__</div><ul>__LIS__</ul></div>
  <div class="foot"><div><b>KRAS G12C Drug Discovery</b> — 검증 가능한 연구 과정 만들기</div>
    <div>Claude Code as a research agent</div></div>
</div></body></html>"""


def main():
    for i, p in enumerate(PHASES, 1):
        lis = "".join(f"<li>{b}</li>" for b in p["bullets"])
        html = (TPL.replace("__NAVY__", NAVY).replace("__BLUE__", BLUE)
                   .replace("__MUTED__", MUTED).replace("__LIGHT__", LIGHT)
                   .replace("__BORDER__", BORDER)
                   .replace("__NO__", p["no"]).replace("__KO__", p["ko"])
                   .replace("__EN__", p["en"]).replace("__FILE__", p["file"])
                   .replace("__Q__", p["q"]).replace("__ART__", p["art"])
                   .replace("__LIS__", lis))
        (OUT / f"phase{i}.html").write_text(html, encoding="utf-8")
        print("wrote", OUT / f"phase{i}.html")


if __name__ == "__main__":
    main()

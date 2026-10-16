import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Starbucks Design System Colors from DESIGN.md
    HOUSE_GREEN = RGBColor(30, 57, 50)       # #1E3932 (Hero band, deep header)
    STARBUCKS_GREEN = RGBColor(0, 98, 65)    # #006241 (Primary headings, brand core)
    GREEN_ACCENT = RGBColor(0, 117, 74)      # #00754A (CTA pills, highlights)
    GREEN_LIGHT = RGBColor(212, 233, 226)    # #D4E9E2 (Mint tint)
    GOLD = RGBColor(203, 162, 88)            # #CBA258 (Rewards Gold, badges)
    GOLD_LIGHTEST = RGBColor(250, 246, 238)  # #FAF6EE (Gold wash)
    NEUTRAL_WARM = RGBColor(242, 240, 235)   # #F2F0EB (Primary warm canvas)
    CERAMIC = RGBColor(237, 235, 233)        # #EDEBE9 (Separators, borders)
    CARD_WHITE = RGBColor(255, 255, 255)     # #FFFFFF (Card surface)
    TEXT_BLACK = RGBColor(30, 30, 30)        # rgba(0,0,0,0.87)
    TEXT_MUTED = RGBColor(110, 110, 110)     # rgba(0,0,0,0.58)
    TEXT_WHITE = RGBColor(255, 255, 255)
    RED_SEMANTIC = RGBColor(200, 32, 20)     # #C82014

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="WORLD HAPPINESS REPORT 2015-2019"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = GREEN_ACCENT

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.5), Inches(0.6))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = STARBUCKS_GREEN

    def add_card(slide, left, top, width, height, bg_color=CARD_WHITE, border_color=CERAMIC):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    # ==========================================
    # SLIDE 1: Title Slide (House Green #1E3932)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, HOUSE_GREEN)

    # Gold Status Badge Pill (50px radius)
    pill1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.5), Inches(3.6), Inches(0.42))
    pill1.fill.solid()
    pill1.fill.fore_color.rgb = HOUSE_GREEN
    pill1.line.color.rgb = GOLD
    pill1.line.width = Pt(1.5)
    p_pill = pill1.text_frame.paragraphs[0]
    p_pill.text = "★ GLOBAL DATA ANALYSIS REPORT"
    p_pill.font.size = Pt(10.5)
    p_pill.font.bold = True
    p_pill.font.color.rgb = GOLD
    p_pill.alignment = PP_ALIGN.CENTER

    # Main Title
    t_box = s1.shapes.add_textbox(Inches(1.2), Inches(2.2), Inches(11), Inches(1.8))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "세계 행복 보고서 (2015–2019)\n데이터 심층 분석 리포트"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

    # Subtitle
    sub_box = s1.shapes.add_textbox(Inches(1.2), Inches(4.3), Inches(10), Inches(0.8))
    p_sub = sub_box.text_frame.paragraphs[0]
    p_sub.text = "5개년 글로벌 행복 지수 트렌드 분석 및 대한민국(South Korea) 심층 진단"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = GREEN_LIGHT

    # Bottom Meta Bar
    add_card(s1, Inches(1.2), Inches(5.6), Inches(10.9), Inches(1.0), bg_color=RGBColor(43, 81, 72), border_color=None)
    meta_box = s1.shapes.add_textbox(Inches(1.4), Inches(5.7), Inches(10.5), Inches(0.8))
    tf_meta = meta_box.text_frame
    p_meta = tf_meta.paragraphs[0]
    p_meta.text = "분석 대상: UN SDSN World Happiness Dataset (782개 레코드, 150+개국 통합)\n디자인 시스템: Starbucks Design System (Warm Canvas, Multi-tier Greens & Gold Status)"
    p_meta.font.size = Pt(11)
    p_meta.font.color.rgb = TEXT_WHITE

    # ==========================================
    # SLIDE 2: Executive Summary (Warm Neutral Canvas)
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, NEUTRAL_WARM)
    add_header(s2, "Executive Summary: 5개년 데이터의 3대 핵심 발견")

    cards_data = [
        ("01", "북유럽의 최상위권 독점", "핀란드(2년 연속 1위), 덴마크, 노르웨이 등 북유럽 복지 국가들이 5개년 연속 1~10위를 확고하게 독점했습니다. 두터운 사회 안전망과 높은 시민 자율성이 성공의 핵심 공식입니다.", STARBUCKS_GREEN),
        ("02", "행복을 좌우하는 3대 동인", "행복 지수는 1인당 GDP(r=0.79), 건강 기대수명(r=0.74), 사회적 지지(r=0.65)와 매우 강한 상관관계를 보였습니다. 경제적 번영과 건강이 행복의 필수적인 토대입니다.", GREEN_ACCENT),
        ("03", "대한민국의 행복 역설(Paradox)", "한국은 5개년 평균 50위권 중반(54위)에 정체되어 있습니다. 경제력(GDP)과 보건(수명)은 글로벌 최상위권이나, '삶의 선택 자유(140위권)'와 '정부 청렴도 신뢰'가 최하위권입니다.", RED_SEMANTIC)
    ]

    card_w = Inches(3.64)
    card_h = Inches(4.8)
    card_top = Inches(1.6)

    for i, (num, title, desc, accent) in enumerate(cards_data):
        left = Inches(0.8 + i * 4.0)
        add_card(s2, left, card_top, card_w, card_h, bg_color=CARD_WHITE, border_color=CERAMIC)

        # Top Accent Strip
        strip = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, card_top, card_w, Inches(0.12))
        strip.fill.solid()
        strip.fill.fore_color.rgb = accent
        strip.line.fill.background()

        tb = s2.shapes.add_textbox(left + Inches(0.3), card_top + Inches(0.4), card_w - Inches(0.6), card_h - Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True

        p_num = tf.paragraphs[0]
        p_num.text = num
        p_num.font.size = Pt(28)
        p_num.font.bold = True
        p_num.font.color.rgb = accent

        p_t = tf.add_paragraph()
        p_t.text = title
        p_t.font.size = Pt(17)
        p_t.font.bold = True
        p_t.font.color.rgb = STARBUCKS_GREEN if accent != RED_SEMANTIC else RED_SEMANTIC
        p_t.space_before = Pt(12)
        p_t.space_after = Pt(12)

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 3: Top 10 vs Bottom 10
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, NEUTRAL_WARM)
    add_header(s3, "글로벌 행복도 순위 분석: 최상위 10개국 vs 최하위 10개국 (2019)")

    top_table_shape = s3.shapes.add_table(11, 4, Inches(0.8), Inches(1.6), Inches(5.6), Inches(4.8))
    t1 = top_table_shape.table
    t1.columns[0].width = Inches(0.8)
    t1.columns[1].width = Inches(2.2)
    t1.columns[2].width = Inches(1.3)
    t1.columns[3].width = Inches(1.3)

    headers1 = ["순위", "국가명", "행복점수", "1인당 GDP"]
    for j, h in enumerate(headers1):
        cell = t1.cell(0, j)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = STARBUCKS_GREEN
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER

    top10_data = [
        ("1위", "핀란드 (Finland)", "7.769", "1.340"),
        ("2위", "덴마크 (Denmark)", "7.600", "1.383"),
        ("3위", "노르웨이 (Norway)", "7.554", "1.488"),
        ("4위", "아이슬란드 (Iceland)", "7.494", "1.380"),
        ("5위", "네덜란드 (Netherlands)", "7.488", "1.396"),
        ("6위", "스위스 (Switzerland)", "7.480", "1.452"),
        ("7위", "스웨덴 (Sweden)", "7.343", "1.387"),
        ("8위", "뉴질랜드 (New Zealand)", "7.307", "1.303"),
        ("9위", "캐나다 (Canada)", "7.278", "1.365"),
        ("10위", "오스트리아 (Austria)", "7.246", "1.351")
    ]
    for i, row in enumerate(top10_data):
        for j, val in enumerate(row):
            cell = t1.cell(i+1, j)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_WHITE if i % 2 == 0 else CERAMIC
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(9.5)
            p.font.color.rgb = TEXT_BLACK
            if j == 0 or j >= 2:
                p.alignment = PP_ALIGN.CENTER

    # Right Card: Bottom 10 and Insights
    add_card(s3, Inches(6.8), Inches(1.6), Inches(5.7), Inches(4.8), bg_color=CARD_WHITE)
    rtb = s3.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.4))
    rtf = rtb.text_frame
    rtf.word_wrap = True

    rp1 = rtf.paragraphs[0]
    rp1.text = "글로벌 양극화 및 최하위권 현황"
    rp1.font.size = Pt(16)
    rp1.font.bold = True
    rp1.font.color.rgb = RED_SEMANTIC

    rp2 = rtf.add_paragraph()
    rp2.text = "최하위 5개국 (152~156위):\n• 156위 남수단 (2.853점) - 만성 내전, 기근\n• 155위 중앙아프리카공화국 (3.083점)\n• 154위 아프가니스탄 (3.203점) - 지속 분쟁\n• 153위 탄자니아 (3.231점) / 152위 르완다 (3.334점)"
    rp2.font.size = Pt(11)
    rp2.font.color.rgb = TEXT_MUTED
    rp2.space_before = Pt(8)
    rp2.space_after = Pt(12)

    rp3 = rtf.add_paragraph()
    rp3.text = "최상위 북유럽 3대 성공 방정식"
    rp3.font.size = Pt(14)
    rp3.font.bold = True
    rp3.font.color.rgb = STARBUCKS_GREEN

    rp4 = rtf.add_paragraph()
    rp4.text = "1. 포용적 복지 제도: 실패해도 회생할 수 있는 안전 매트리스\n2. 높은 공공 신뢰: 투명한 정부 운영과 낮은 부패 인식\n3. 삶의 자율성 보장: 사회적 눈치 없이 자신의 진로를 주도적 결정"
    rp4.font.size = Pt(11)
    rp4.font.color.rgb = TEXT_BLACK
    rp4.space_before = Pt(6)

    # ==========================================
    # SLIDE 4: Drivers of Happiness (Correlation)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, NEUTRAL_WARM)
    add_header(s4, "행복 결정 요인 분석: 무엇이 인간을 행복하게 만드는가?")

    if os.path.exists("charts/chart1_correlations.png"):
        s4.shapes.add_picture("charts/chart1_correlations.png", Inches(0.8), Inches(1.6), width=Inches(6.4))

    add_card(s4, Inches(7.5), Inches(1.6), Inches(5.0), Inches(4.8), bg_color=CARD_WHITE)
    c4_box = s4.shapes.add_textbox(Inches(7.8), Inches(1.9), Inches(4.4), Inches(4.2))
    c4_tf = c4_box.text_frame
    c4_tf.word_wrap = True

    p = c4_tf.paragraphs[0]
    p.text = "상관관계 분석 핵심 시사점"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = STARBUCKS_GREEN

    points = [
        ("1. 물질적·신체적 토대 (r = 0.74 ~ 0.79)", "1인당 GDP와 건강 기대수명은 행복의 절대적인 기본 전제입니다. 기본 생존과 보건 인프라 없이는 높은 행복도를 달성하기 어렵습니다."),
        ("2. 사회적 지지망의 결정적 역할 (r = 0.65)", "어려움에 처했을 때 기댈 수 있는 가족이나 친구, 사회 공동체의 유무가 삶의 만족도를 결정하는 핵심 매개체입니다."),
        ("3. 상위권 도약의 열쇠: 자율성과 신뢰", "경제력이 선진국 수준에 도달한 후에는 '개인의 선택 자유(r=0.55)'와 '정부 청렴도(r=0.40)'가 국가 간 행복 격차를 가르는 결정적 차별 요소가 됩니다.")
    ]
    for title, desc in points:
        pt = c4_tf.add_paragraph()
        pt.text = title
        pt.font.size = Pt(12)
        pt.font.bold = True
        pt.font.color.rgb = GREEN_ACCENT
        pt.space_before = Pt(10)

        pd = c4_tf.add_paragraph()
        pd.text = desc
        pd.font.size = Pt(10.5)
        pd.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 5: South Korea Deep Dive
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, NEUTRAL_WARM)
    add_header(s5, "대한민국(South Korea) 심층 진단: 번영 속의 행복 정체")

    if os.path.exists("charts/chart2_korea_trend.png"):
        s5.shapes.add_picture("charts/chart2_korea_trend.png", Inches(0.8), Inches(1.6), width=Inches(5.7))

    if os.path.exists("charts/chart4_korea_vs_top10.png"):
        s5.shapes.add_picture("charts/chart4_korea_vs_top10.png", Inches(6.8), Inches(1.6), width=Inches(5.7))

    # Bottom Highlight Banner
    add_card(s5, Inches(0.8), Inches(5.8), Inches(11.7), Inches(1.1), bg_color=CARD_WHITE, border_color=RED_SEMANTIC)
    k_box = s5.shapes.add_textbox(Inches(1.0), Inches(5.85), Inches(11.3), Inches(1.0))
    ktf = k_box.text_frame
    ktf.word_wrap = True
    kp1 = ktf.paragraphs[0]
    kp1.text = "대한민국의 핵심 모순: '높은 역량, 낮은 체감 자유와 신뢰'"
    kp1.font.size = Pt(12)
    kp1.font.bold = True
    kp1.font.color.rgb = RED_SEMANTIC

    kp2 = ktf.add_paragraph()
    kp2.text = "• 강점: 1인당 GDP(1.30점) 및 건강 기대수명(1.04점, 글로벌 최상위권)은 선진국 수준을 완벽히 충족함\n• 치명적 약점: '삶의 선택 자유'는 0.159점으로 조사 대상 156개국 중 최하위권(140위권)이며, 정부 신뢰도(0.056점) 역시 매우 낮음"
    kp2.font.size = Pt(10.5)
    kp2.font.color.rgb = TEXT_BLACK

    # ==========================================
    # SLIDE 6: East Asia Benchmark
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, NEUTRAL_WARM)
    add_header(s6, "동아시아 벤치마크: 대만, 한국, 일본, 홍콩 비교 (2019)")

    if os.path.exists("charts/chart3_east_asia.png"):
        s6.shapes.add_picture("charts/chart3_east_asia.png", Inches(0.8), Inches(1.6), width=Inches(5.8))

    add_card(s6, Inches(6.9), Inches(1.6), Inches(5.6), Inches(4.8), bg_color=CARD_WHITE)
    ea_box = s6.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(5.0), Inches(4.4))
    eatf = ea_box.text_frame
    eatf.word_wrap = True

    eap1 = eatf.paragraphs[0]
    eap1.text = "동아시아 주요국 비교 관전 포인트"
    eap1.font.size = Pt(16)
    eap1.font.bold = True
    eap1.font.color.rgb = STARBUCKS_GREEN

    ea_points = [
        ("1. 대만(25위, 6.446점)의 독보적 선전", "대만은 동아시아 국가 중 유일하게 20위권에 진입했습니다. 한국과 1인당 소득은 비슷하지만, 사회적 지지망(1.430)과 삶의 선택 자유(0.351)가 한국(0.159)보다 2배 이상 높았습니다."),
        ("2. 한국(54위) vs 일본(58위)의 유사한 딜레마", "한국(5.895점)과 일본(5.886점)은 거의 동일한 수준의 행복도를 기록했습니다. 양국 모두 세계 최고의 치안과 의료를 갖추었지만, 조직 문화의 경직성과 입시/취업 경쟁 압박이 유사하게 작용합니다."),
        ("3. 사회 갈등과 홍콩(76위)", "홍콩은 GDP와 수명에서 세계 최고 수준임에도 불구하고, 사회적 신뢰 저하와 자유도 불안정으로 인해 76위로 크게 밀려났습니다.")
    ]
    for t_ea, d_ea in ea_points:
        p_t = eatf.add_paragraph()
        p_t.text = t_ea
        p_t.font.size = Pt(12)
        p_t.font.bold = True
        p_t.font.color.rgb = GREEN_ACCENT
        p_t.space_before = Pt(8)

        p_d = eatf.add_paragraph()
        p_d.text = d_ea
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 7: Big Movers
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, NEUTRAL_WARM)
    add_header(s7, "지난 5년간의 대격변: 가장 크게 상승한 나라 vs 추락한 나라 (2015-2019)")

    add_card(s7, Inches(0.8), Inches(1.6), Inches(5.6), Inches(4.8), bg_color=CARD_WHITE, border_color=RED_SEMANTIC)
    db = s7.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.4))
    dtf = db.text_frame
    dtf.word_wrap = True

    dp1 = dtf.paragraphs[0]
    dp1.text = "최대 하락 국가 (Biggest Droppers)"
    dp1.font.size = Pt(17)
    dp1.font.bold = True
    dp1.font.color.rgb = RED_SEMANTIC

    dp2 = dtf.add_paragraph()
    dp2.text = "1. 베네수엘라: -2.103점 급락 (6.810점 → 4.707점, 23위 → 108위)\n2. 레소토: -1.096점 하락\n3. 잠비아: -1.022점 하락\n4. 짐바브웨: -0.947점 하락\n5. 아이티: -0.921점 하락"
    dp2.font.size = Pt(11.5)
    dp2.font.color.rgb = TEXT_BLACK
    dp2.space_before = Pt(10)
    dp2.space_after = Pt(12)

    dp3 = dtf.add_paragraph()
    dp3.text = "시사점: 국가 거버넌스 붕괴의 대가"
    dp3.font.size = Pt(13)
    dp3.font.bold = True
    dp3.font.color.rgb = RED_SEMANTIC

    dp4 = dtf.add_paragraph()
    dp4.text = "베네수엘라의 경우 정치적 혼란과 하이퍼인플레이션, 공공 인프라 붕괴가 국민 체감 행복도를 순식간에 파괴할 수 있음을 증명합니다."
    dp4.font.size = Pt(10.5)
    dp4.font.color.rgb = TEXT_MUTED

    # Right: Gainers
    add_card(s7, Inches(6.9), Inches(1.6), Inches(5.6), Inches(4.8), bg_color=CARD_WHITE, border_color=STARBUCKS_GREEN)
    gb = s7.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(5.0), Inches(4.4))
    gtf = gb.text_frame
    gtf.word_wrap = True

    gp1 = gtf.paragraphs[0]
    gp1.text = "최대 상승 국가 (Biggest Gainers)"
    gp1.font.size = Pt(17)
    gp1.font.bold = True
    gp1.font.color.rgb = STARBUCKS_GREEN

    gp2 = gtf.add_paragraph()
    gp2.text = "1. 베냉 (Benin): +1.543점 상승 (3.340점 → 4.883점)\n2. 코트디부아르: +1.289점 상승 (3.655점 → 4.944점)\n3. 토고 (Togo): +1.246점 상승 (2.839점 → 4.085점)\n4. 온두라스: +1.072점 상승\n5. 부르키나파소: +1.000점 상승"
    gp2.font.size = Pt(11.5)
    gp2.font.color.rgb = TEXT_BLACK
    gp2.space_before = Pt(10)
    gp2.space_after = Pt(12)

    gp3 = gtf.add_paragraph()
    gp3.text = "시사점: 정정 안정과 기초 경제 성장의 힘"
    gp3.font.size = Pt(13)
    gp3.font.bold = True
    gp3.font.color.rgb = STARBUCKS_GREEN

    gp4 = gtf.add_paragraph()
    gp4.text = "서아프리카 국가들은 내전 종식, 정치적 안정 회복, 기초 보건 및 인프라 구축을 통해 단기간에 극적인 행복 지수 개선을 달성했습니다."
    gp4.font.size = Pt(10.5)
    gp4.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 8: Strategic Recommendations (House Green Band Accent)
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, NEUTRAL_WARM)
    add_header(s8, "대한민국 행복 지수 도약을 위한 3대 전략적 제언")

    recs = [
        ("전략 1: 삶의 경로 자율성 보장", "획일적 성공 기준에서 탈피하여 다양한 진로와 삶의 방식을 존중하는 유연한 사회 구조 구축이 필수적입니다. 노동 시장 유연안전성(Flexicurity)을 확보하여 이직 및 재도전의 기회를 보장해야 합니다.", STARBUCKS_GREEN),
        ("전략 2: 사회적 자본과 공공 신뢰 제고", "국가 및 공공 기관의 정책 투명성을 강화하고 사회 전반의 부패 인식을 척결해야 합니다. 사회적 자본(Social Capital) 투자를 통해 공동체 간 신뢰도를 회복해야 합니다.", GREEN_ACCENT),
        ("전략 3: 실패를 용인하는 사회적 안전망", "단순 경제 지원을 넘어 실패 시 빈곤으로 추락하지 않도록 보호하는 '안전 매트리스' 구축이 필요합니다. 고립 청년 및 취약 계층의 심리·사회적 복지망을 확충해야 합니다.", GOLD)
    ]

    for i, (title, text, accent) in enumerate(recs):
        top_y = Inches(1.6 + i * 1.5)
        add_card(s8, Inches(0.8), top_y, Inches(11.7), Inches(1.3), bg_color=CARD_WHITE, border_color=CERAMIC)

        strip = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_y, Inches(0.18), Inches(1.3))
        strip.fill.solid()
        strip.fill.fore_color.rgb = accent
        strip.line.fill.background()

        tb = s8.shapes.add_textbox(Inches(1.25), top_y + Inches(0.12), Inches(11.0), Inches(1.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = STARBUCKS_GREEN

        p_d = tf.add_paragraph()
        p_d.text = text
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_before = Pt(4)

    output_path = "world_happiness_presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    create_deck()

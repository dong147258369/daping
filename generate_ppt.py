import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # 配色体系
    BG_DARK = RGBColor(11, 25, 44)        # #0B192C 深海黑蓝
    BG_CARD = RGBColor(23, 44, 76)        # #172C4C 卡片背景蓝
    BG_CARD_LIGHT = RGBColor(30, 58, 98)  # #1E3A62 亮卡片蓝
    CYAN = RGBColor(0, 242, 254)          # #00F2FE 科技青
    CYAN_LIGHT = RGBColor(147, 235, 248)  # 浅青
    WHITE = RGBColor(255, 255, 255)
    GRAY_TEXT = RGBColor(148, 163, 184)   # #94A3B8 辅助字
    ORANGE = RGBColor(255, 159, 67)       # 强调橙
    RED = RGBColor(255, 107, 107)         # 警示红
    GREEN = RGBColor(46, 213, 115)        # 安全绿
    GOLD = RGBColor(255, 215, 0)          # 冠军金
    PURPLE = RGBColor(180, 114, 255)      # 科技紫

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, tag_text, title_text):
        tx_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(8), Inches(0.3))
        tf_tag = tx_tag.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = CYAN
        
        tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.5), Inches(0.55))
        tf_title = tx_title.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = WHITE

    # ==========================
    # SLIDE 1: 封面
    # ==========================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)
    
    ring = slide1.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.5), Inches(-1.5), Inches(5.5), Inches(5.5))
    ring.fill.solid()
    ring.fill.fore_color.rgb = RGBColor(20, 50, 90)
    ring.line.color.rgb = CYAN
    ring.line.width = Pt(2)
    
    ring2 = slide1.shapes.add_shape(MSO_SHAPE.OVAL, Inches(10.5), Inches(4.5), Inches(3.8), Inches(3.8))
    ring2.fill.solid()
    ring2.fill.fore_color.rgb = RGBColor(16, 40, 75)
    ring2.line.color.rgb = RGBColor(0, 180, 240)
    ring2.line.width = Pt(1.5)

    comp_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(9), Inches(0.5))
    p = comp_box.text_frame.paragraphs[0]
    p.text = "第十一届全国大学生数字媒体科技作品及创意竞赛 · 医疗信息化成果汇报"
    p.font.size = Pt(13)
    p.font.color.rgb = CYAN
    p.font.bold = True

    title_box = slide1.shapes.add_textbox(Inches(1.2), Inches(2.3), Inches(9), Inches(1.5))
    p1 = title_box.text_frame.paragraphs[0]
    p1.text = "智 医 云 视"
    p1.font.size = Pt(56)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    
    sub_box = slide1.shapes.add_textbox(Inches(1.2), Inches(3.9), Inches(10), Inches(0.8))
    p2 = sub_box.text_frame.paragraphs[0]
    p2.text = "数字孪生智慧医疗服务数据可视化管理平台"
    p2.font.size = Pt(23)
    p2.font.bold = True
    p2.font.color.rgb = CYAN_LIGHT

    badges = ["三大协同大屏矩阵", "急救/重症双置顶预警", "零滚动条双向满屏自适应"]
    left_start = Inches(1.2)
    for b_text in badges:
        badge_shape = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_start, Inches(4.8), Inches(2.55), Inches(0.42))
        badge_shape.fill.solid()
        badge_shape.fill.fore_color.rgb = BG_CARD_LIGHT
        badge_shape.line.color.rgb = CYAN
        badge_shape.line.width = Pt(1)
        p = badge_shape.text_frame.paragraphs[0]
        p.text = b_text
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER
        badge_shape.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        left_start += Inches(2.7)

    info_box = slide1.shapes.add_textbox(Inches(1.2), Inches(5.9), Inches(9), Inches(0.6))
    p = info_box.text_frame.paragraphs[0]
    p.text = "汇报单位：智医云视研发项目组   |   汇报时间：2026年   |   运行服务：http://localhost:8112/"
    p.font.size = Pt(11)
    p.font.color.rgb = GRAY_TEXT

    # ==========================
    # SLIDE 2: 目录页
    # ==========================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    
    deco_ring = slide2.shapes.add_shape(MSO_SHAPE.OVAL, Inches(-1.5), Inches(1.5), Inches(4.5), Inches(4.5))
    deco_ring.fill.solid()
    deco_ring.fill.fore_color.rgb = BG_CARD
    deco_ring.line.color.rgb = CYAN
    deco_ring.line.width = Pt(2)
    
    title_dir = slide2.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(3.0), Inches(3.0))
    p = title_dir.text_frame.paragraphs[0]
    p.text = "目 录\nCONTENTS"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE

    parts = [
        ("PART 01", "项目背景", "政策东风 · 医疗大数据爆发 · 临床一线四大痛点"),
        ("PART 02", "设计方案构建", "以提升医院运行效率为核心 · 三支柱赋能 · 系统定位"),
        ("PART 03", "作品效果展示", "三大指挥大屏矩阵(综合监控/急救调度/全景运营)与创新图表"),
        ("PART 04", "核心技术实现", "Vue 3 + Vite 8 前端架构 · Scale-Screen 零滚动条自适应"),
        ("PART 05", "作品未来展望", "AI大模型病情预判 · 3D院区数字孪生 · 全链路闭环联动")
    ]
    top_pos = Inches(1.2)
    for p_id, p_title, p_desc in parts:
        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.5), top_pos, Inches(8.0), Inches(1.0))
        card.fill.solid()
        card.fill.fore_color.rgb = BG_CARD
        card.line.color.rgb = RGBColor(40, 75, 120)
        card.line.width = Pt(1)
        
        tf = card.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = f"{p_id}   {p_title}"
        p0.font.size = Pt(17)
        p0.font.bold = True
        p0.font.color.rgb = CYAN
        
        p1 = tf.add_paragraph()
        p1.text = p_desc
        p1.font.size = Pt(11)
        p1.font.color.rgb = GRAY_TEXT
        
        top_pos += Inches(1.15)

    # ==========================
    # SLIDE 3: PART 01 市场背景与政策支持
    # ==========================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "PART 01 项目背景", "1. 市场背景与政策支持：政策与技术双东风驱动")

    card_l = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(5.6), Inches(5.4))
    card_l.fill.solid()
    card_l.fill.fore_color.rgb = BG_CARD
    card_l.line.color.rgb = RGBColor(0, 180, 240)
    
    tf_l = card_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "【政策强力推动】国家顶层战略布局"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = CYAN

    policies = [
        "《“健康中国2030”规划纲要》：提出健康医疗服务数字化和信息化建设，强化医疗安全智能监控与全流程质控监管。",
        "《“十四五”全民健康信息化规划》：推进大数据、人工智能与智慧医院深度融合，明确将信息化水平纳入公立医院高质量考评关键指标。",
        "国家医保局《智能审核和监控知识库管理办法》：推动医疗基金合规监控与全流程可视化闭环审查。",
        "核心趋势：全国医疗健康数字化投资总额连年上涨，政策加码推动医院从‘被动统计’走向‘主动智能监管’。"
    ]
    for pol in policies:
        p = tf_l.add_paragraph()
        p.text = "• " + pol
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE
        p.space_before = Pt(8)

    card_r = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4))
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = BG_CARD
    card_r.line.color.rgb = ORANGE

    tf_r = card_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "【市场前景广阔】5G医疗与物联网场景爆发"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ORANGE

    market_points = [
        "中国医疗大数据解决方案市场规模持续飞速增长，行业整体渗透率从 2019 年的 7.2% 攀升至 16.2% 以上。",
        "5G 远程急救与物联网普及：急救车载终端、ICU生命体征监护仪等多源设备产生海量数据，催生统一调度中枢。",
        "按投资额统计的中国医药数字化投资总额持续上涨，医院信息化建设由‘分散单点业务系统’转向‘全域可视化运营决策’。",
        "核心结论：智慧医疗可视化不仅是医院现代化的形象窗口，更是直接关乎抢救效率与临床质控的刚需工具。"
    ]
    for mp in market_points:
        p = tf_r.add_paragraph()
        p.text = "• " + mp
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE
        p.space_before = Pt(8)

    # ==========================
    # SLIDE 4: PART 01 临床一线四大痛点
    # ==========================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "PART 01 项目背景", "2. 临床一线四大痛点：有数据却依然“盲人摸象”")

    pain_items = [
        ("01", "数据孤岛断裂 · 跨域难以串联", "HIS、LIS、PACS、120急救与设备科系统彼此孤立，跨系统调阅需反复切换，缺乏全域视角的实时统一指挥看板。"),
        ("02", "急危重症抢救脱节 · 黄金时间流失", "急救车转运途中患者生命指征与心电数据无法即时直达院内，急诊抢救室只能等病人到达再做准备，浪费宝贵的溶栓黄金窗。"),
        ("03", "ICU危急值反馈滞后 · 缺乏即时闭环", "传统模式高度依赖检验科座机电话层层转告，缺少大屏级高危声光自动置顶与闭环追踪机制，存在医疗安全差错隐患。"),
        ("04", "全院床位与大型设备流转失衡", "热门科室床位周转超负荷甚至加床，冷门病房床位空置；3,680台高精尖大型设备运行状态不透明，设备故障与质控无法提前预知。")
    ]
    coords = [
        (Inches(0.8), Inches(1.5)), (Inches(6.8), Inches(1.5)),
        (Inches(0.8), Inches(4.2)), (Inches(6.8), Inches(4.2))
    ]
    for idx, (code, title, desc) in enumerate(pain_items):
        cx, cy = coords[idx]
        p_card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, Inches(5.7), Inches(2.4))
        p_card.fill.solid()
        p_card.fill.fore_color.rgb = BG_CARD
        p_card.line.color.rgb = RED if idx in [1, 2] else RGBColor(50, 80, 130)
        
        tf = p_card.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = f"[{code}] {title}"
        p0.font.size = Pt(15)
        p0.font.bold = True
        p0.font.color.rgb = RED if idx in [1, 2] else CYAN
        
        p1 = tf.add_paragraph()
        p1.text = desc
        p1.font.size = Pt(12)
        p1.font.color.rgb = WHITE
        p1.space_before = Pt(8)

    # ==========================
    # SLIDE 5: PART 02 设计方案构建 —— 设计策略（参考图5）
    # ==========================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "PART 02 设计方案构建", "1. 设计策略：为什么要用信息可视化系统？（三大支柱）")

    hub = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.2), Inches(5.6), Inches(8.9), Inches(1.2))
    hub.fill.solid()
    hub.fill.fore_color.rgb = RGBColor(0, 114, 255)
    hub.line.color.rgb = CYAN
    hub.line.width = Pt(2)
    p = hub.text_frame.paragraphs[0]
    p.text = "核心驱动中枢：全面提升医院整体运行效率"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    hub.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

    columns = [
        ("支柱一：医护人员", CYAN, [
            "合理安排医疗时间，平抑急诊波峰波谷",
            "根据就诊时序预测，精准优化科室排班",
            "多科室、多部门急救绿色通道瞬时联动"
        ]),
        ("支柱二：医疗设备与药品", GREEN, [
            "提高检验样本识别准确性与危机值上报时效",
            "提高高值耗材与药品运转效率",
            "全院 3,680 台大型医疗设备运行健康监控"
        ]),
        ("支柱三：医疗场地与床位", ORANGE, [
            "实时掌握各院区与科室病患空间分布",
            "重点科室床位使用率动态调节与借床流转",
            "急救路线智能导览与绿色通道畅通保障"
        ])
    ]
    c_left = Inches(0.8)
    for c_title, c_color, c_items in columns:
        col_shape = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(1.5), Inches(3.7), Inches(3.8))
        col_shape.fill.solid()
        col_shape.fill.fore_color.rgb = BG_CARD
        col_shape.line.color.rgb = c_color
        col_shape.line.width = Pt(1.5)
        
        tf = col_shape.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = c_title
        p0.font.size = Pt(16)
        p0.font.bold = True
        p0.font.color.rgb = c_color
        p0.alignment = PP_ALIGN.CENTER
        
        for item in c_items:
            pi = tf.add_paragraph()
            pi.text = "✓ " + item
            pi.font.size = Pt(12)
            pi.font.color.rgb = WHITE
            pi.space_before = Pt(12)
            
        c_left += Inches(4.0)

    # ==========================
    # SLIDE 6: PART 02 设计方案构建 —— 设计说明与系统定位（参考图4）
    # ==========================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "PART 02 设计方案构建", "2. 设计说明与系统整体定位")

    spec_card = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.7), Inches(2.2))
    spec_card.fill.solid()
    spec_card.fill.fore_color.rgb = RGBColor(16, 40, 75)
    spec_card.line.color.rgb = CYAN
    spec_card.line.width = Pt(1.5)
    
    tf = spec_card.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = "【设计说明 · 核心理念】（参考大赛与国家智慧医院建设规范）"
    p0.font.size = Pt(15)
    p0.font.bold = True
    p0.font.color.rgb = CYAN
    
    p1 = tf.add_paragraph()
    p1.text = "智慧医疗数字孪生系统，整合医疗管理部门现有信息系统数据，将综合信息、运作流程、LIS检验监测、IOT物联网设备监测四个部分与管理部门需求有机结合，提高管理者的决策效率，并且真正实现了整体可视化、管理智能化、服务高效化、设施科技化。"
    p1.font.size = Pt(13)
    p1.font.color.rgb = WHITE
    p1.space_before = Pt(8)

    goals = [
        ("平急结合", "平时监控门急诊与床位负荷，急时一键切换应急出车与重大公共卫生战备模式。"),
        ("双向闭环", "告警不仅大屏即时呈现，更同步推送到责任医护工作站，闭环处置率达99.8%。"),
        ("分级掌控", "宏观掌控全国/全省医联体协作，微观穿透到具体ICU病床与仪器生命指标。"),
        ("三屏联动", "构建综合监控、急救调度、全景运营三大专业大屏矩阵，顶栏一键丝滑互切。")
    ]
    g_left = Inches(0.8)
    for g_title, g_desc in goals:
        g_card = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, g_left, Inches(4.0), Inches(2.7), Inches(2.7))
        g_card.fill.solid()
        g_card.fill.fore_color.rgb = BG_CARD
        g_card.line.color.rgb = RGBColor(0, 180, 240)
        
        gtf = g_card.text_frame
        gtf.word_wrap = True
        p = gtf.paragraphs[0]
        p.text = g_title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = CYAN
        p.alignment = PP_ALIGN.CENTER
        
        p = gtf.add_paragraph()
        p.text = g_desc
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE
        p.space_before = Pt(10)
        
        g_left += Inches(3.0)

    # ==========================
    # SLIDE 7: PART 03 作品效果展示 —— 三大智慧医疗大屏矩阵
    # ==========================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "PART 03 作品效果展示", "1. 三大智慧医疗指挥大屏矩阵架构")

    screens = [
        ("大屏一：综合监控指挥", CYAN, "医院全局运营中枢", [
            "急危重症双置顶 (急救出车动态 & ICU危急值预警)",
            "南丁格尔发光玫瑰图 (患者四级就诊分类分布)",
            "全国医联体协作网络地图 (动态流光飞线+下钻)",
            "重点科室床位使用率 (3D水晶立体双柱图)"
        ]),
        ("大屏二：急救与应急调度", RED, "院前院内绿色通道中枢", [
            "120急救智慧指挥网格与动态雷达扫描地图",
            "五大急救中心专科绿色通道时效达成率",
            "急诊抢救室与EICU床位监护 (实时HR/SpO2/BP)",
            "24小时急救出车频次与平均到达耗时走势"
        ]),
        ("大屏三：医院全景运营监管", PURPLE, "数字孪生与质控中枢", [
            "全院建筑楼宇三维空间透视矩阵 (人流与能耗)",
            "全院16间高标准中心洁净手术室实时看板",
            "重点科室就诊负荷多维雷达图 (Radar七维分析)",
            "全院平均住院日与床位周转率堆叠走势分析"
        ])
    ]
    s_x = Inches(0.8)
    for s_title, s_color, s_role, s_points in screens:
        s_box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s_x, Inches(1.5), Inches(3.7), Inches(5.3))
        s_box.fill.solid()
        s_box.fill.fore_color.rgb = BG_CARD
        s_box.line.color.rgb = s_color
        s_box.line.width = Pt(1.8)
        
        tf = s_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = s_title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = s_color
        p.alignment = PP_ALIGN.CENTER
        
        pr = tf.add_paragraph()
        pr.text = f"定位：{s_role}"
        pr.font.size = Pt(11)
        pr.font.color.rgb = GRAY_TEXT
        pr.alignment = PP_ALIGN.CENTER
        pr.space_before = Pt(4)
        
        for pt in s_points:
            pi = tf.add_paragraph()
            pi.text = "▶ " + pt
            pi.font.size = Pt(12)
            pi.font.color.rgb = WHITE
            pi.space_before = Pt(12)
            
        s_x += Inches(4.0)

    # ==========================
    # SLIDE 8: PART 03 大屏一：综合监控指挥大屏展示
    # ==========================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "PART 03 作品效果展示", "2. 大屏一：智慧医疗综合监控指挥大屏")

    # 左侧说明卡片
    info_c1 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4))
    info_c1.fill.solid()
    info_c1.fill.fore_color.rgb = BG_CARD
    info_c1.line.color.rgb = CYAN
    
    tf = info_c1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "【核心业务与技术亮点】"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = CYAN

    pts_c1 = [
        "急危重症双置顶机制：左上置顶出车动态，右上置顶ICU危急值预警，生命体征越限毫秒级置顶。",
        "南丁格尔发光玫瑰图：展现门急诊、普通住院、重症ICU与危急病患四级就诊梯度，同心雷达虚线环。",
        "全国医联体远程医疗飞线图：中心枢纽向各省市协作医院发射带箭头的动态脉冲飞线，支持省市下钻。",
        "3D水晶柱重点科室床位使用率：实心水晶立柱与半透明编制柱形成容量对比，叠加玫红脉冲折线。"
    ]
    for pt in pts_c1:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE
        p.space_before = Pt(10)

    # 右侧展示模块结构
    struct_c1 = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4))
    struct_c1.fill.solid()
    struct_c1.fill.fore_color.rgb = BG_CARD_LIGHT
    struct_c1.line.color.rgb = RGBColor(0, 180, 240)

    tfr = struct_c1.text_frame
    tfr.word_wrap = True
    p = tfr.paragraphs[0]
    p.text = "【大屏一 · 模块布局与视觉表现】"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = CYAN_LIGHT

    blocks_c1 = [
        "左侧布局：急救通道出车动态(置顶) ➔ 3680台医疗设备运行监控(四态旋转环) ➔ 患者就诊分类态势(玫瑰图)",
        "中央核心：医联体与医疗协作网(全国流光飞线地图+散点水波) ➔ 重点科室床位使用率(3D水晶双柱)",
        "右侧布局：重症监护危急值预警(置顶) ➔ 门急诊与危急值24h双走势(心电波曲线) ➔ 科室负荷TOP8(金银铜胶囊图)",
        "视觉沉浸：暗夜深空蓝底、高对比荧光警示色、零滚动条满贴视口、60FPS流畅动画管线。"
    ]
    for blk in blocks_c1:
        p = tfr.add_paragraph()
        p.text = "▶ " + blk
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE
        p.space_before = Pt(10)

    # ==========================
    # SLIDE 9: PART 03 大屏二：智慧急救与应急调度大屏展示（插入截图）
    # ==========================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9)
    add_header(slide9, "PART 03 作品效果展示", "3. 大屏二：智慧急救与应急调度大屏（院前急救绿通实战中枢）")

    # 插入大屏二截图（上方）
    img_em_path = r"f:\github\大屏\IofTV-Screen-Vue3\screen_emergency.png"
    if os.path.exists(img_em_path):
        slide9.shapes.add_picture(img_em_path, Inches(0.8), Inches(1.4), Inches(11.7), Inches(3.2))

    # 下方左右双解析卡片
    em_card_l = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.8), Inches(5.7), Inches(2.2))
    em_card_l.fill.solid()
    em_card_l.fill.fore_color.rgb = BG_CARD
    em_card_l.line.color.rgb = RED
    
    tf = em_card_l.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "【核心中枢：120急救智慧指挥网格实时调度】"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RED
    
    em_l_pts = [
        "雷达同心圆与360°动态扫描特效：模拟空地一体化雷达网格，辐射中心急救总院。",
        "实时车辆发光点位：追踪粤A·6982等救护车位置，标注专科通道类型与D2B急救耗时。",
        "车辆四态占比环形图：实时呈现出车抢救(18)、待命就绪(32)、清洗消毒(6)、维保检修(4)。"
    ]
    for pt in em_l_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE
        p.space_before = Pt(4)

    em_card_r = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.8), Inches(5.7), Inches(2.2))
    em_card_r.fill.solid()
    em_card_r.fill.fore_color.rgb = BG_CARD
    em_card_r.line.color.rgb = CYAN

    tf_r = em_card_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "【绿通达成率与EICU抢救床位实时监护】"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = CYAN

    em_r_pts = [
        "五大专科绿色通道：胸痛、卒中、创伤、高危孕产、儿科急救时效达标率均在92%~98.2%以上。",
        "抢救室01~06床生命指标监控：卡片实时刷新病患姓名、心率HR、血氧SpO2、血压BP及抢救状态。",
        "24小时出车频次走势 & 120出车实时流水播报：柱线组合分析出车高峰与到院耗时。"
    ]
    for pt in em_r_pts:
        p = tf_r.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE
        p.space_before = Pt(4)

    # ==========================
    # SLIDE 10: PART 03 大屏三：智慧医院全景运营监管大屏展示（插入截图）
    # ==========================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10)
    add_header(slide10, "PART 03 作品效果展示", "4. 大屏三：智慧医院全景运营监管大屏（数字孪生与全景质控）")

    # 插入大屏三截图（上方）
    img_op_path = r"f:\github\大屏\IofTV-Screen-Vue3\screen_operation.png"
    if os.path.exists(img_op_path):
        slide10.shapes.add_picture(img_op_path, Inches(0.8), Inches(1.4), Inches(11.7), Inches(3.2))

    # 下方左右双解析卡片
    op_card_l = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.8), Inches(5.7), Inches(2.2))
    op_card_l.fill.solid()
    op_card_l.fill.fore_color.rgb = BG_CARD
    op_card_l.line.color.rgb = PURPLE
    
    tf = op_card_l.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "【成都市第二人民医院 · 院区三维数字孪生全景】"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PURPLE
    
    op_l_pts = [
        "空间立体楼宇透视：门急诊综合大楼(12层)、第一住院楼(24层)、第二外科大楼、医技中心。",
        "双指标动态监测：实时展示各建筑人流热力(1680人/2150人)与能耗负载(88/142 kW·h)。",
        "全院核心运营KPI透视：今日门急诊4680人次、入院286人、在院2850人、床位使用率94.6%。"
    ]
    for pt in op_l_pts:
        p = tf.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE
        p.space_before = Pt(4)

    op_card_r = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.8), Inches(5.7), Inches(2.2))
    op_card_r.fill.solid()
    op_card_r.fill.fore_color.rgb = BG_CARD
    op_card_r.line.color.rgb = CYAN

    tf_r = op_card_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "【中心手术室16间矩阵看板 & 质控闭环流转】"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = CYAN

    op_r_pts = [
        "全院洁净手术室实时看板：室01~08卡片直观显示主刀医生、手术等级、术式名称与实时状态(手术中/接台/复苏)。",
        "重点科室就诊负荷多维雷达图(Radar)：心血管、急诊、神外、骨科等多维负荷指标透视。",
        "医保基金结算阶梯柱、高值耗材流速监控 & 全院医疗质控不良事件闭环流水。"
    ]
    for pt in op_r_pts:
        p = tf_r.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE
        p.space_before = Pt(4)

    # ==========================
    # SLIDE 11: PART 03 顶栏发光Tabs与三屏无缝热切换交互
    # ==========================
    slide11 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide11)
    add_header(slide11, "PART 03 作品效果展示", "5. 顶栏发光Tabs与三屏无缝平滑热切换交互")

    tab_features = [
        ("发光切换按钮组", CYAN, "顶部Header左上角集成「综合监控」「急救调度」「全景运营」三个专属发光Tab，支持现场一键点击切换。"),
        ("动态标题智能跟随", GREEN, "切换大屏时，顶部标题自动根据当前激活视图平滑渐变更新，与两侧装饰矩形保持和谐对称。"),
        ("Vue Router无刷新路由", ORANGE, "基于Vue Router子路由模式，切换无需刷新整个浏览器页面，组件保持60FPS极速热替换。"),
        ("全屏自适应无缝继承", PURPLE, "三大页面均严格继承Scale-Screen双向自适应引擎，彻底消解所有多余滚动条，全分辨率满贴显示。")
    ]
    coords11 = [
        (Inches(0.8), Inches(1.5)), (Inches(6.8), Inches(1.5)),
        (Inches(0.8), Inches(4.2)), (Inches(6.8), Inches(4.2))
    ]
    for idx, (t_name, t_color, t_desc) in enumerate(tab_features):
        cx, cy = coords11[idx]
        t_card = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, Inches(5.7), Inches(2.4))
        t_card.fill.solid()
        t_card.fill.fore_color.rgb = BG_CARD
        t_card.line.color.rgb = t_color
        t_card.line.width = Pt(1.5)
        
        tf = t_card.text_frame
        tf.word_wrap = True
        p0 = tf.paragraphs[0]
        p0.text = f"★ {t_name}"
        p0.font.size = Pt(15)
        p0.font.bold = True
        p0.font.color.rgb = t_color
        
        p1 = tf.add_paragraph()
        p1.text = t_desc
        p1.font.size = Pt(12)
        p1.font.color.rgb = WHITE
        p1.space_before = Pt(10)

    # ==========================
    # SLIDE 12: PART 04 核心技术实现：前端架构与数据流
    # ==========================
    slide12 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide12)
    add_header(slide12, "PART 04 核心技术实现", "1. 前端技术栈底座与六步数据流转管道")

    arch_left = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3))
    arch_left.fill.solid()
    arch_left.fill.fore_color.rgb = BG_CARD
    arch_left.line.color.rgb = CYAN
    
    tf = arch_left.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "【前端工程技术底座】"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = CYAN

    arch_points = [
        "Vue 3 + Composition API：现代化组合式API架构，图表与数据逻辑高度解耦，提升系统维护性与扩展性。",
        "TypeScript 强类型系统：全面约束急救单号、床位危急值、生命体征等数据契约，杜绝运行时类型异常。",
        "Vite 8 原生ESM工具链：秒级冷启动与毫秒级模块热替换(HMR)，生产构建经过Rollup深度优化打包。",
        "Pinia 全局响应式状态管理：取代传统Vuex，提供扁平化、无冗余的状态流，支撑三大屏与抽屉组件数据同步。"
    ]
    for ap in arch_points:
        p = tf.add_paragraph()
        p.text = "• " + ap
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE
        p.space_before = Pt(10)

    arch_right = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    arch_right.fill.solid()
    arch_right.fill.fore_color.rgb = BG_CARD
    arch_right.line.color.rgb = GREEN

    tf_r = arch_right.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "【六步数据流转管道】"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = GREEN

    pipe_steps = [
        ("Step 1 多源采集", "HIS、LIS、PACS、120车载终端与病床IOT监护仪异构采集。"),
        ("Step 2 清洗标准", "数据湖ETL清洗，统一字段字典与危急阈值规则判定。"),
        ("Step 3 实时推送", "WebSocket长连接 / SSE毫秒级向下游大屏分发数据包。"),
        ("Step 4 状态管理", "Pinia全局Store接收并触发响应式数据分发。"),
        ("Step 5 图表渲染", "ECharts 6根据最新数据驱动Canvas重绘，GPU硬件加速。"),
        ("Step 6 满贴呈现", "Scale-Screen引擎进行动态视口计算与无缝呈现。")
    ]
    for s_name, s_info in pipe_steps:
        p = tf_r.add_paragraph()
        p.text = f"{s_name}：{s_info}"
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE
        p.space_before = Pt(6)

    # ==========================
    # SLIDE 13: PART 04 核心技术实现：Scale-Screen自适应算法
    # ==========================
    slide13 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide13)
    add_header(slide13, "PART 04 核心技术实现", "2. Scale-Screen“零滚动条”双向全屏满贴算法")

    card_sc1 = slide13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3))
    card_sc1.fill.solid()
    card_sc1.fill.fore_color.rgb = BG_CARD
    card_sc1.line.color.rgb = ORANGE
    
    tf = card_sc1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "【算法公式与工程实现】"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ORANGE

    sc_formulas = [
        "基准设计稿：以行业标准 1920 × 1080 作为初始设计基准分辨率。",
        "动态双向缩放比例计算公式：\n   ScaleX = ClientWidth / 1920\n   ScaleY = ClientHeight / 1080",
        "在开启 fullScreen 模式下，系统分别按实际宽高比进行拉伸变换，确保 100% 满贴任意屏幕；在等比模式下自动取 Math.min 居中显示。",
        "硬件加速驱动：通过 root.style.transform = `scale(...)` 硬件加速变换，避免触发浏览器主线程重排(Reflow)，性能极度平滑。"
    ]
    for sc in sc_formulas:
        p = tf.add_paragraph()
        p.text = "• " + sc
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE
        p.space_before = Pt(8)

    card_sc2 = slide13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    card_sc2.fill.solid()
    card_sc2.fill.fore_color.rgb = BG_CARD
    card_sc2.line.color.rgb = CYAN

    tf_r = card_sc2.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "【彻底消解滚动条的核心攻关】"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = CYAN

    scrollbar_fixes = [
        "根节点绝对锁死：在 html, body, #app, .v-screen-box 等根节点统一设置 overflow: hidden; width: 100vw; height: 100vh; margin: 0; padding: 0;，杜绝任何外层溢出滚动。",
        "容器自适应锁定：将 ScaleScreen 的 boxStyle.overflow 固定设为 'hidden'，无论在笔记本、带书签栏的浏览器、还是大屏拼接墙，均绝不出现侧边滑轮。",
        "响应式窗口监听：集成防抖 Resize 监听器，在窗口发生拖拽缩放时 200ms 内快速完成重算满贴。",
        "抽屉式实时设置：右上角设置抽屉允许用户实时开关轮播与自适应配置。"
    ]
    for sf in scrollbar_fixes:
        p = tf_r.add_paragraph()
        p.text = "• " + sf
        p.font.size = Pt(11)
        p.font.color.rgb = WHITE
        p.space_before = Pt(8)

    # ==========================
    # SLIDE 14: PART 05 作品未来展望
    # ==========================
    slide14 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide14)
    add_header(slide14, "PART 05 作品未来展望", "三大演进方向：从“看见”到“预见”，迈向数字孪生全域协同")

    future_cols = [
        ("一、AI临床大模型态势推演", CYAN, [
            "接入医疗大模型，对门急诊就诊流感波峰、床位紧张度进行超前 48 小时预测",
            "重症危急值多模态智能关联，自动推荐抢救用药与处置路径",
            "大型医疗设备故障与耗损提前预警与维保备件调度"
        ]),
        ("二、全域3D数字孪生院区融合", GREEN, [
            "结合 WebGL / Three.js 引擎，实现病区楼宇 1:1 三维高精建模与空间实景映射",
            "病床级微环境透视：实时显示病房温湿度、床旁监护仪与医护人员轨迹",
            "手术室、洁净处置室与智慧物流送药车全空间三维动线导览"
        ]),
        ("三、跨终端全链路闭环联动", ORANGE, [
            "大屏发现预警 ➔ 智能派单推送至医生工作站/护士站 ➔ 处置复核全流程留痕",
            "医院中央监控大屏、科室移动平板与120车载中控三屏实时同源联动",
            "为公立医院国考、三甲复审与医疗质控等级评审自动输出指标报表"
        ])
    ]
    f_x = Inches(0.8)
    for f_title, f_color, f_list in future_cols:
        f_box = slide14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, f_x, Inches(1.5), Inches(3.7), Inches(5.3))
        f_box.fill.solid()
        f_box.fill.fore_color.rgb = BG_CARD
        f_box.line.color.rgb = f_color
        f_box.line.width = Pt(1.5)
        
        tf = f_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f_title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = f_color
        p.alignment = PP_ALIGN.CENTER
        
        for item in f_list:
            pi = tf.add_paragraph()
            pi.text = "★ " + item
            pi.font.size = Pt(11)
            pi.font.color.rgb = WHITE
            pi.space_before = Pt(12)
            
        f_x += Inches(4.0)

    # ==========================
    # SLIDE 15: 致谢与Q&A
    # ==========================
    slide15 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide15)

    ring_end = slide15.shapes.add_shape(MSO_SHAPE.OVAL, Inches(4.16), Inches(1.2), Inches(5.0), Inches(5.0))
    ring_end.fill.solid()
    ring_end.fill.fore_color.rgb = BG_CARD
    ring_end.line.color.rgb = CYAN
    ring_end.line.width = Pt(2)

    tx_end = slide15.shapes.add_textbox(Inches(2.0), Inches(2.2), Inches(9.3), Inches(2.5))
    tf = tx_end.text_frame
    p = tf.paragraphs[0]
    p.text = "感谢各位评委专家的聆听与指导！"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf.add_paragraph()
    p2.text = "智医云视 · 数字孪生智慧医疗大数据可视化管理平台"
    p2.font.size = Pt(19)
    p2.font.color.rgb = CYAN
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(14)

    p3 = tf.add_paragraph()
    p3.text = "Q & A · 敬请各位老师批评指正"
    p3.font.size = Pt(16)
    p3.font.color.rgb = GRAY_TEXT
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(10)

    # 保存最新完整版 PPT
    output_path = r"f:\github\大屏\IofTV-Screen-Vue3\云医智能_智慧医疗服务数据可视化管理平台.pptx"
    prs.save(output_path)
    print("Updated 15-slide PPT successfully generated at:", output_path)

if __name__ == "__main__":
    create_deck()

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="B0C4DE"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

doc = Document()

# Page Margins (Normal 2.54cm)
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Default style font
normal_style = doc.styles['Normal']
normal_style.font.name = '宋体'
normal_style.font.size = Pt(10.5)
normal_style.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = '黑体'
    run.font.size = Pt(16)
    run.bold = True
    run.font.color.rgb = RGBColor(0x11, 0x1E, 0x38)

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(14)
    run = p.add_run(text)
    run.font.name = '楷体'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

def add_h1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = '黑体'
    run.font.size = Pt(12)
    run.bold = True
    run.font.color.rgb = RGBColor(0x0E, 0x47, 0x7E)

def add_h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(9)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = '黑体'
    run.font.size = Pt(11)
    run.bold = True
    run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

def add_body(text, bold_prefix=None, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.25
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = '黑体'
        r_pre.font.size = Pt(10.5)
        r_pre.bold = True
        r_pre.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    run = p.add_run(text)
    run.font.name = '宋体'
    run.font.size = Pt(10.5)
    run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    return p

def add_callout(text, prefix="【特别提示】"):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    r_pre = p.add_run(prefix + " ")
    r_pre.font.name = '黑体'
    r_pre.font.size = Pt(9.5)
    r_pre.bold = True
    r_pre.font.color.rgb = RGBColor(0x9E, 0x38, 0x0E)
    run = p.add_run(text)
    run.font.name = '仿宋'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

# Header Title
add_title("2026年第十四届全国大学生数字媒体科技作品及创意竞赛\n人工智能工具使用情况说明")
add_subtitle("（参赛团队参考模板 · 正式填报稿）")

add_h1("填写说明")
add_body("本说明用于说明人工智能工具在参赛作品创作、设计、开发、制作及成果形成过程中的实际作用，重点体现学生自主完成的核心工作和原创贡献。")
add_body("1. 本团队在报名系统中如实填报已使用AI，并在本文档中详细客观说明主要工具、使用环节、人工处理及学生团队独立原创贡献。")
add_body("2. 提交专家评审的本说明严格按照赛事匿名化规范处理，隐去参赛学校、团队成员和指导教师等可识别身份的信息。")
add_body("3. 本团队在此确认：合理使用AI本身不直接构成加分或扣分因素，评审核心在于作品创新性、工程落地深度及学生自主原创贡献。")

# 一、作品基本信息与AI使用状态
add_h1("一、作品基本信息与AI使用状态")
table1 = doc.add_table(rows=4, cols=2)
table1.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(table1)

t1_data = [
    ("作品名称", "智医云视 —— 数字孪生智慧医疗服务数据可视化管理平台"),
    ("作品编号（如有）", "【报名系统已自动生成，匿名化保留该栏】"),
    ("参赛赛道／赛项", "智能算法与数据可视化 / 数字媒体科技与数字孪生"),
    ("AI使用情况", "□ 未使用　　☑ 已使用")
]

for row_idx, (col0, col1) in enumerate(t1_data):
    cell0 = table1.cell(row_idx, 0)
    cell1 = table1.cell(row_idx, 1)
    cell0.width = Inches(2.2)
    cell1.width = Inches(4.3)
    set_cell_background(cell0, "F0F4F8")
    set_cell_margins(cell0, top=120, bottom=120, left=150, right=150)
    set_cell_margins(cell1, top=120, bottom=120, left=150, right=150)
    
    p0 = cell0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r0 = p0.add_run(col0)
    r0.font.name = '黑体'
    r0.font.size = Pt(10)
    r0.bold = True
    
    p1 = cell1.paragraphs[0]
    r1 = p1.add_run(col1)
    r1.font.name = '宋体'
    r1.font.size = Pt(10)
    if "☑" in col1:
        r1.bold = True

add_callout("选择“已使用”。以下内容如实反映本团队在作品构思、代码实现、数据模拟各环节的具体辅助作用与学生团队的人工深化再创作工作。")

# 二、主要AI工具及使用情况
add_h1("二、主要AI工具及使用情况")
add_body("仅填写对作品形成具有实际影响的主要工具或模型，一般性资料查询无需逐项罗列：")

table2 = doc.add_table(rows=4, cols=4)
table2.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(table2)

t2_headers = ["工具／模型", "使用环节", "AI主要用途或产出", "学生后续处理"]
for c_idx, h in enumerate(t2_headers):
    c = table2.cell(0, c_idx)
    set_cell_background(c, "E6EFF7")
    set_cell_margins(c, top=140, bottom=140, left=120, right=120)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.font.name = '黑体'
    r.font.size = Pt(10)
    r.bold = True

t2_data = [
    ("代码辅助智能体\n(Antigravity Assistant)", 
     "前端工程搭建、算法辅助、ECharts参数调试", 
     "提供Vue 3 Composition API范式建议、ECharts复杂图表（玫瑰图、3D双柱、雷达图）配置属性参考、Scale-Screen视口缩放算法逻辑参考。", 
     "学生自主重构整套前端工程代码，编写三级路由平滑热切换架构，针对1920×1080无滚动条进行全局样式绝对锁死，重写ECharts高级渐变、流光飞线及图表事件交互。"),
    
    ("大语言模型\n(ChatGPT / 豆包)", 
     "背景调研、政策提炼、汇报PPT框架头脑风暴", 
     "辅助归纳《“健康中国2030”规划纲要》及《十四五全民健康信息化规划》关键词，提供智慧医院平急结合设计策略的初版发散思路与竞赛路演大纲草稿。", 
     "学生结合真实公立医院运营痛点，彻底重构出“信息提纯、物联透视、毫秒预警、作战地图”四大设计策略，自主撰写答辩逐字稿并剔除所有不符医学场景的虚泛内容。"),
    
    ("图像生成工具\n(即梦 / Midjourney)", 
     "大屏UI概念设计、深空科技背景纹理参考", 
     "生成深蓝色科技光环、全景院区三维透视概念示意图，作为大屏整体UI设计语言的色调与光影参考。", 
     "学生提取有效光影元素后，在Photoshop中进行精度重绘、切片与暗夜深空色彩校准（降低值守疲劳），人工完成CSS3动态扫描线与SVG发光边框的手工编码。")
]

col_widths2 = [Inches(1.5), Inches(1.3), Inches(2.2), Inches(2.0)]
for row_idx, row_items in enumerate(t2_data, start=1):
    for col_idx, item_text in enumerate(row_items):
        cell = table2.cell(row_idx, col_idx)
        cell.width = col_widths2[col_idx]
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        r = p.add_run(item_text)
        r.font.name = '宋体'
        r.font.size = Pt(9.5)

# 三、代表性AI使用过程
add_h1("三、代表性AI使用过程")
add_body("结合实际选择三个对最终成果影响较大的关键环节，简要说明“使用目的—主要输入—AI输出—人工处理—最终应用”：")

cases = [
    ("环节一：临床急危重症与120出车高保真Mock数据生成", [
        ("使用环节及目的", "系统需在开发及演示阶段模拟真实医疗临床数据，用于检验大屏在多并发、多指标剧烈变动下的渲染稳健性。"),
        ("主要工具／模型", "ChatGPT / 代码辅助模型"),
        ("主要输入或素材来源", "学生输入临床医学监测规则，如：胸痛/卒中患者抢救时效、ICU生命体征指标警戒范围（心率>150bpm、血氧<90%、血钾>6.5mmol/L），以及120车牌及流水编号规则。"),
        ("AI主要输出", "一段基础的JSON数据模板与随机数生成逻辑草稿。"),
        ("学生筛选、修改或再创作", "学生团队针对医疗语义进行全面修正：严格定义危急值三级警示阈值，剔除荒谬指标（如脉搏为0但意识清醒）；重写动态推送管道，通过Pinia与响应式定时器构建具有医学临床真实波动规律的高保真数据流。"),
        ("最终成果中的应用位置", "大屏一（综合监控）置顶预警模块、大屏二（急救调度）EICU床位监护卡片、大屏三（全景运营）科室就诊负荷及医保结算模块。"),
        ("可核验材料（如有）", "源码 `src/mock/` 目录中的高保真医疗数据定义及业务逻辑过滤函数。")
    ]),
    ("环节二：3D水晶床位柱状图与南丁格尔发光玫瑰图算法优化", [
        ("使用环节及目的", "提升医疗大屏图表的科技观感与数据穿透力，解决传统二维扁平图表在全景指挥中视觉层级单薄的问题。"),
        ("主要工具／模型", "代码辅助智能体"),
        ("主要输入或素材来源", "学生向AI提供基础ECharts柱状图与环形图配置，提出设计诉求：“如何用ECharts实现带3D菱形水晶盖的立体双柱，以及带同心虚线雷达光环的南丁格尔玫瑰图？”"),
        ("AI主要输出", "提供了利用ECharts `pictorialBar` 自定义矢量图形（path）叠加的实现思路和初版配置片段。"),
        ("学生筛选、修改或再创作", "AI给出的初版配置在屏幕自适应缩放时出现盖顶偏移、图层错位问题。学生团队重新计算了Canvas图元坐标缩放比，采用双层阴影光晕渲染与极坐标系优化，手写实现‘在用床位与编制床位’立体虚实对比及荧光折线融合组件。"),
        ("最终成果中的应用位置", "大屏一中下方重点科室床位使用率看板、左下方患者就诊分类态势组件。"),
        ("可核验材料（如有）", "源码 `src/views/index/center-bottom.vue` 与 `left-bottom.vue`。")
    ]),
    ("环节三：三大主题大屏热切换架构与无滚动条满屏算法攻坚", [
        ("使用环节及目的", "攻克大屏在不同分辨率投影与显示器下的右侧滑轮溢出问题，并实现三大主题大屏毫秒级平滑热切换。"),
        ("主要工具／模型", "Antigravity Assistant / 代码辅助模型"),
        ("主要输入或素材来源", "提出工程难题：“在Vue 3 + Vite架构下，如何设计多大屏无刷新路由切换，同时使用Scale-Screen进行硬件加速缩放，杜绝任何滚动条？”"),
        ("AI主要输出", "给出了基于Vue Router动态过渡动画的示例结构，以及Scale-Screen组件引入参考。"),
        ("学生筛选、修改或再创作", "学生团队进行了深层工程重构：在 `html, body, #app, .v-screen-box` 根节点设置 `overflow: hidden; width: 100vw; height: 100vh` 绝对锁死；编写双向视口比例计算公式（ScaleX/ScaleY）；重构顶栏Header科技Tabs发光组件与标题联动机制，确保图表DOM在切换时安全销毁并释放显存。"),
        ("最终成果中的应用位置", "系统根架构 `App.vue`、`HomeView.vue`、顶栏 `header.vue` 与全局样式 `main.scss`。"),
        ("可核验材料（如有）", "全屏零滚动条核心算法源码与Git版本迭代提交记录。")
    ])
]

for title, rows in cases:
    add_h2(title)
    tbl = doc.add_table(rows=len(rows), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl)
    for r_idx, (k, v) in enumerate(rows):
        c0 = tbl.cell(r_idx, 0)
        c1 = tbl.cell(r_idx, 1)
        c0.width = Inches(2.0)
        c1.width = Inches(4.8)
        set_cell_background(c0, "F5F8FA")
        set_cell_margins(c0, top=90, bottom=90, left=120, right=120)
        set_cell_margins(c1, top=90, bottom=90, left=120, right=120)
        
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r0 = p0.add_run(k)
        r0.font.name = '黑体'
        r0.font.size = Pt(9.5)
        r0.bold = True
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.name = '宋体'
        r1.font.size = Pt(9.5)

# 四、最终成果中的AI生成或辅助内容
add_h1("四、最终成果中的AI生成或辅助内容")
add_body("如最终成果直接或部分保留AI生成或辅助生成内容，填写下表：")

table4 = doc.add_table(rows=5, cols=4)
table4.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(table4)

t4_headers = ["内容／成果", "AI生成或辅助部分", "学生修改与整合", "最终使用位置"]
for c_idx, h in enumerate(t4_headers):
    c = table4.cell(0, c_idx)
    set_cell_background(c, "E6EFF7")
    set_cell_margins(c, top=140, bottom=140, left=120, right=120)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.font.name = '黑体'
    r.font.size = Pt(10)
    r.bold = True

t4_data = [
    ("医疗仿真数据集", "辅助生成各科室急救出车编号、生命体征极值与药品耗材品类的结构化字段模板。", "学生注入严密的临床医学关联性，设计定时器波动管道，过滤异常伪数据。", "三大主题大屏所有动态轮播列表与图表数据源"),
    ("复杂图表配置参数", "提供南丁格尔玫瑰图与立体柱状图的初版ECharts option参数组合。", "学生重构图层透明度、渐变色板（Neon冷光），优化响应式重绘（resize）与显存释放机制。", "全屏各子组件Vue源码"),
    ("大屏视觉纹理素材", "辅助提供深蓝科技同心环与网格雷达的视觉构成概念参考。", "学生在设计软件中进行高清矢量重绘、色彩校准与切片，手写CSS3动画进行融合。", "大屏二中央雷达底图与大屏三楼宇透视底图"),
    ("答辩演示文稿框架", "辅助提供竞赛汇报PPT的五部分逻辑大纲及部分答辩台词初稿。", "学生结合系统三大页面功能全面改写，重构Slide 07-11的大屏实景深度剖析与技术架构图。", "最终交付的15页《云医智能》PPTX文稿及演讲逐字稿")
]

for row_idx, row_items in enumerate(t4_data, start=1):
    for col_idx, item_text in enumerate(row_items):
        cell = table4.cell(row_idx, col_idx)
        set_cell_margins(cell, top=90, bottom=90, left=120, right=120)
        p = cell.paragraphs[0]
        r = p.add_run(item_text)
        r.font.name = '宋体'
        r.font.size = Pt(9.5)

add_callout("本团队严格按照规定具体阐明修改与整合工作，杜绝使用“AI占比50%”等难以核实的百分比代替实际工作说明。")

# 五、学生原创贡献说明
add_h1("五、学生原创贡献说明")
add_h2("学生自主完成的核心工作：")
core_works = [
    ("1. 业务需求分析与平急结合架构设计：", "深入研究大型三甲医院急危重症抢救工作流与公立医院高质量发展指标考评规范，独创提炼出“综合监控、急救调度、全景运营”三大主题大屏的业务架构，并首创“急危重症双置顶”响应机制。"),
    ("2. 完整前端工程底座自主开发：", "基于Vue 3 (Composition API) + Vite 8 + TypeScript，从零搭建高内聚低耦合的前端工程，自主设计Pinia状态总线，实现跨组件毫秒级联动与三屏平滑无刷新热切换。"),
    ("3. 全屏视口无滚动条自适应算法攻坚：", "传统大屏在不同分辨率显示器下普遍存在右侧滑轮溢出难题。通过硬件加速的 `transform: scale()` 视口动态换算算法，并在根容器层实施样式锁死，彻底消除浏览器滚动条，实现工业级全屏满贴呈现。"),
    ("4. 深度定制化前沿图表二次开发：", "攻关并实现了南丁格尔发光玫瑰图、3D水晶双立体床位柱、医联体彗星飞线流光地图、TOP8胶囊勋章排行榜以及全院16间洁净手术室作战看板，实现高性能Canvas GPU硬件加速渲染，帧率稳定在60FPS。"),
    ("5. 医疗业务逻辑闭环与系统联调：", "全系统所有页面交互逻辑、告警级别阈值计算、时间轴脉冲走势及动效渲染均由学生团队自主编码与测试优化，确保系统具备真实的临床语义与实战指挥价值。")
]
for title, desc in core_works:
    add_body(desc, bold_prefix=title, space_after=5)

add_h2("AI与学生工作边界说明（必要时填写）：")
boundary_text = (
    "学生团队明确声明：AI在本作品中仅扮演“辅助工具”角色（即资料归纳助手、代码语法参考与初版头脑风暴建议）。\n"
    "核心创意理念、系统功能定位、医疗业务规则、系统交互界面、核心算法实现（包括双置顶响应、视口比例计算、3D图元换算）、全套工程代码审查与重构，均由学生团队完全自主独立完成。\n"
    "作品不存在任何由AI一键生成且未经验证的代码或设计，所有提交产物均处于学生团队的深度工程掌控之下。"
)
add_body(boundary_text)

# 六、代表性过程材料（按需）
add_h1("六、代表性过程材料（按需）")
add_body("根据实际需要，提供典型环节的输入输出对比及人工再创作说明（已脱敏）：")

prompt_cases = [
    ("【典型环节 1】 医疗图表视觉与算法攻坚",
     "【主要输入（Prompt）】\n“在Vue 3 + ECharts项目中，现有一组科室在用床位与编制床位数据，常规柱状图缺乏科技感与立体感。请给出利用pictorialBar实现3D水晶圆柱与菱形顶盖的配置方案，要求支持暗黑深蓝主题。”\n\n"
     "【AI输出片段】\n提供了基本的pictorialBar symbol配置骨架与径向渐变代码。\n\n"
     "【学生筛选与再创作】\n学生发现AI给出的配置在窗口resize时顶盖发生撕裂偏移，且缺少使用率百分比脉冲折线。学生重写了数据映射逻辑，加入双立柱间距防重叠算法，并在顶部叠加发光霓虹折线图，封装为独立的 `center-bottom.vue` 高内聚业务组件。"),
    
    ("【典型环节 2】 急救调度网格与地图流光动效",
     "【主要输入（Prompt）】\n“如何在ECharts的Geo地图上实现带彗星尾迹流动效果的飞线（Lines）与涟漪扩散散点（EffectScatter），并保证在全国与省市下钻时流畅运行？”\n\n"
     "【AI输出片段】\n提供了 lines 系列中 `effect.trailLength` 和 `period` 的官方参数解释及一段散点静态数据。\n\n"
     "【学生筛选与再创作】\nAI仅给出了基础单向示例。学生自主接入了高精度医疗机构经纬度坐标字典，编写了从医联体总院至各基层分院的动态辐射流向算法，并增加了地市级双向平滑下钻机制与右上角一键返回交互。")
]

for p_title, p_content in prompt_cases:
    add_h2(p_title)
    p_box = doc.add_paragraph()
    p_box.paragraph_format.space_before = Pt(4)
    p_box.paragraph_format.space_after = Pt(8)
    p_box.paragraph_format.line_spacing = 1.15
    run = p_box.add_run(p_content)
    run.font.name = '仿宋'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)

# 七、资源来源与合规说明
add_h1("七、资源来源与合规说明")
add_body("系统所使用的开源依赖、素材与模型服务严格遵守相关使用条款、开源许可及知识产权规定。")

table7 = doc.add_table(rows=5, cols=4)
table7.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(table7)

t7_headers = ["素材名称与类别", "来源或权利方", "实际用途", "授权或许可情况"]
for c_idx, h in enumerate(t7_headers):
    c = table7.cell(0, c_idx)
    set_cell_background(c, "E6EFF7")
    set_cell_margins(c, top=140, bottom=140, left=120, right=120)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.font.name = '黑体'
    r.font.size = Pt(10)
    r.bold = True

t7_data = [
    ("ECharts 6.x 数据可视化库", "Apache Software Foundation", "大屏核心图表与流光地图渲染", "Apache License 2.0 开源许可，合法商用与参赛"),
    ("Vue 3 & Vite 构建管线", "Evan You & Vue.js 开源社区", "单页面应用框架与组件化驱动", "MIT License 开源许可"),
    ("医疗科技发光边框与矢量图标", "学生原创绘制 + 开源矢量图元", "大屏各卡片边角装饰与状态指示", "学生团队自研矢量图，保留原创设计稿"),
    ("AI辅助生成之数据与文本参考", "代码辅助智能体 / 大语言模型", "技术方案参考及模拟数据辅助", "遵守相关工具使用条款，已经过彻底重构与脱敏")
]

for row_idx, row_items in enumerate(t7_data, start=1):
    for col_idx, item_text in enumerate(row_items):
        cell = table7.cell(row_idx, col_idx)
        set_cell_margins(cell, top=90, bottom=90, left=120, right=120)
        p = cell.paragraphs[0]
        r = p.add_run(item_text)
        r.font.name = '宋体'
        r.font.size = Pt(9.5)

add_callout("参赛团队如实说明素材来源及使用情况，绝未将第三方素材或AI生成成果直接表述为学生独立原创成果。相关真实性、原创性及知识产权承诺按照本届统一《参赛承诺书》执行。")

# 八、填写确认与提交提示
add_h1("八、填写确认与提交提示")
add_body("参赛团队确认：本说明真实反映AI工具使用情况、学生自主工作和最终成果状态，绝无虚构使用过程或将AI及第三方成果表述为学生独立原创。相关真实性、原创性及知识产权承诺按照本届统一《参赛承诺书》执行，不重复要求签字盖章。")
add_body("本说明属于材料清单第13项的补充材料，确需提交时，按第6项参赛打包文件的要求归档；如专项赛有专门实践说明或其他材料要求，按其正式文件执行。")

add_callout("合理使用AI本身不直接构成加分或扣分因素；AI工具数量、生成比例不作为独立评分依据。评审重点在于作品创新、实际完成情况及学生原创贡献。")

# Save document
out_path = r"f:\github\大屏\IofTV-Screen-Vue3\2026年第十四届全国大学生数字媒体科技作品及创意竞赛_人工智能工具使用情况说明.docx"
doc.save(out_path)
print(f"Successfully generated: {out_path}")

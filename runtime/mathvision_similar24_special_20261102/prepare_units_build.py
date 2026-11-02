"""Prepare disjoint research briefs; no rendering or solver/network calls."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib, json, sys

sys.dont_write_bytecode = True
TASK = Path(__file__).resolve().parent
ROOT = next(p for p in TASK.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
OLD = ROOT/'runtime/mathvision_special_20261101'

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for chunk in iter(lambda:f.read(262144), b''):
            h.update(chunk)
    return h.hexdigest()

def save(p, d):
    p = Path(p)
    assert p.resolve().is_relative_to(TASK)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')

def text(p, value):
    p = Path(p)
    assert p.resolve().is_relative_to(TASK)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x', encoding='utf-8', newline='\n') as f:
        f.write(value)

eligibility = read(TASK/'eligibility_initial.json')
references = read(TASK/'reference_manifest.json')
initial_sources = read(TASK/'readonly_source_sha256.json')
task = read(TASK/'task.json')
assert all(sha(ROOT/p) == h for p,h in initial_sources.items())
created = datetime.now(timezone.utc).isoformat()

styles = {
 'Plane217': {
  'observed_style':'四个原有孔按对角位置分成红、蓝各两孔；选项A的两条原虚线按下斜红、上斜蓝对应。孔位与虚线的方向类别形成对应，并未标示精确平行或等长。',
  'current_source_option_relation':'当前配对选项A；不可据此替别题事后确定错答。',
  'migration_rule':'保留孔的数量、位置、折线及全部选项；标记须承担明确的位置/方向比较角色。'
 },
 'Plane233': {
  'observed_style':'原棋盘与选项C的左侧四格竖直外边界标红，左端两格底边标蓝；两组开放L形边界具有真实相同长度。源图没有内部切分标记。',
  'current_source_option_relation':'当前对应选项C；局部能放入不等于三份可以铺满。',
  'migration_rule':'13个保存动作中C_1的蓝色和1.5pt线宽可合并成一个动作，合并后12动作的最终像素无损。不要形成闭合伪分区或给定不存在的切口。'
 },
 'Plane308': {
  'observed_style':'源点1、3、5（奇数）红；2、4、6（偶数）蓝。选项A的两条三角形轮廓红蓝对应，局部线宽1.5pt。',
  'current_source_option_relation':'当前源点颜色是真实奇偶分组；不是旧18份交付中1/2/3与4/5/6的连续编号分组。',
  'migration_rule':'保持可读编号和点的真实数量/位置，用真实组别或具体线段/顶点关系建立源与候选的比较；不要把颜色当新增编号条件。'
 },
 'Plane427': {
  'observed_style':'ST与TV两条真实等腰三角形STV的腰标红，SV原点虚线底边标蓝；70度原角弧及所求角原弧保留。',
  'current_source_option_relation':'当前两腰红、底边蓝；与旧记录两腰蓝、底边红的描述不同。',
  'migration_rule':'标明真实对应边/角所属结构，保留原有角弧、旋转中心、方向文字；颜色不新增等长、垂直或角平分条件。'
 },
 'Solid126': {
  'observed_style':'红色比较原移除轮廓与新台面的真实面积边界，蓝色比较相应深度边；原虚线/实线仍可区别移除轮廓和现存棱。',
  'current_source_option_relation':'removed2在保存数组中先红后蓝，最终像素为蓝；不能把早期被覆盖红色当作最终信息。',
  'migration_rule':'迁移时清除被完全覆盖的无效前置动作；只比较实际存在的面积/边界，分别计算消失外表面和新增内表面，勿把体积变化当表面积变化。'
 },
 'Solid142': {
  'observed_style':'原折叠餐巾的左侧切口标红、上侧切口标蓝，分别与选项A中的左右竖菱孔红、上下竖菱孔蓝对应。',
  'current_source_option_relation':'当前配对选项A；两种颜色追踪两个切口位置而不是仅突出整幅选项。',
  'migration_rule':'追踪真实切口及其展开后边缘方向，不新增切口、不把题目允许自由选择的剪法固定成一条新给定剪线。'
 },
 'Solid167': {
  'observed_style':'两次对折图中的左切口红、上切口蓝；选项A左右竖菱孔红、上下竖菱孔蓝。两个切口局部1.5pt，孔边保持原几何。',
  'current_source_option_relation':'当前用户版本指向A；不是旧18份交付中的D水平菱孔对应。',
  'migration_rule':'把红蓝用于区分具体剪口及镜像/展开方向；剪口数量、折叠次数、孔洞形状和原填充保持，不能用颜色改变纸张自带内容。'
 },
 'Solid176': {
  'observed_style':'选项D中四条真实三角瓣边同红，突出上下端盖的朝向、位置和封闭配合。虚线折痕保留。',
  'current_source_option_relation':'四边作用是三角瓣的配合比较；不能迁移为无信息地给一个错误选项整幅加色。',
  'migration_rule':'在新展开图中找真实待闭合边/瓣、面邻接或缺口关系；冻结三维几何、投影与显隐，不以重绘改变可折性。'
 },
 'Solid203': {
  'observed_style':'原八面体展开图的x边与左上标C的边同红，其他棱、编号与右侧八面体保持。',
  'current_source_option_relation':'当前用户版本是x与C的边对应，不是旧交付预设A对应；必须实际看参考PNG。',
  'migration_rule':'迁移的是两条具体边/面的配对关系。新八面体需独立折叠传播验证正确接缝，不从平面最近或同色直接推出真重合。'
 }
}
for q, style in styles.items():
    d = TASK/references[q]['directory']
    assert sha(d/'C01.png') == references[q]['png_sha256']
    assert sha(d/'C01.json') == references[q]['plugin_sha256']
    style.update({'question_id':q,'reference_directory':str(d),
                  'C01_png_sha256':sha(d/'C01.png'),'C01_plugin_sha256':sha(d/'C01.json'),
                  'actual_current_reference_PNG_viewed_by_preparer':True})
save(TASK/'reference_style_summary.json', {'created_at_utc':created,'references':styles,
     'scope':'Observed current user C01 pixels and stored actions, not a solver-effect claim; no reference is a new preset or proof for another question.'})

units = [
 ('u01_fold_locations','折线与孔位对应', ['Plane202','Plane238','Plane461'], ['Plane217']),
 ('u02_pieces','相同拼块与局部边界对应', ['Plane218','Plane398'], ['Plane233']),
 ('u03_points','编号与连点图形对应', ['Plane211','Plane364','Plane423'], ['Plane308']),
 ('u04_angles','旋转与真实边角结构对应', ['Plane321','Plane490'], ['Plane427']),
 ('u05_surface','移除前后真实表面积对应', ['Solid186','Solid226'], ['Solid126']),
 ('u06_fold_cut','折纸剪切与展开边缘对应', ['Solid146','Solid174','Solid239','Plane220'], ['Solid142','Solid167']),
 ('u07_corner_cut','两次对折与剪角展开', ['Plane194','Plane245'], ['Solid167']),
 ('u08_cube_nets','立方体三角瓣与可折性', ['Solid187','Solid193','Solid228'], ['Solid176']),
 ('u09_octa_nets','八面体封边与面对应', ['Solid166','Solid240'], ['Solid203'])
]
directions = {
 'Plane202': '从真实候选折线与袋鼠位置/朝向关系迁移红蓝配对。需独立验证每条可行折线及正确计数；袋鼠轮廓若着色可合理读作纸面固有图案，必须重新审视字面折叠后颜色是否使原答案失效，不可降低唯一解释标准。',
 'Plane238': '追踪图中真实孔位、两次折叠与原36格编号的对应，可比较容易混淆的反射方向或相邻位置；不得改孔位置、格线、编号，不新增第二个物理孔。',
 'Plane461': '以红蓝区分两次折叠中的真实位置/方向，并向候选展开孔位配对；孔、原X、边界、折线与折叠箭头均保持，不能增加/遮蔽孔或把着色变成物理印刷约束。',
 'Plane218': '迁移开放L边界、长边/底脚等真实局部对应，用于局部可放入与两块全等覆盖的比较。需对每种候选给两份不重叠放置见证/不可能证明；不要仅验证单份可放入，更不能在源棋盘画出固定分区。',
 'Plane398': '在原给定两块与目标4×4拼图之间配对真正对应的外边、凹角或黑白局部信息；黑白填充是题义，不能修改或遮蔽。需枚举允许的刚体放置并证明唯一不能拼成者；防止彩色纸边被读成新的实物内容后无选项可匹配。',
 'Plane211': '当前参考308按真奇偶标色，可迁移编号/边的组别对应。此题每隔一个点的访问是模9循环，必须追踪1→3→5→7→9→2→4→6→8→1，不能把它错误当成仅连奇数的闭环并据此错误验证原题。新标记仍只比较，不改编号/已有线。',
 'Plane364': '六个原格点能组成的图形类别是目标；保留全部点和网格，可迁移真实点组/边向量的红蓝比较。必须逐项构造或精确枚举正式选项A—D所需见证，不能因与423同图直接复制其选项证明。禁止新增角点、文字或把选定连线声明为唯一准许组合。',
 'Plane423': '与364的正式PNG相同，但本题选项是平行四边形、梯形、直角三角形、钝角三角形等，需独立按本题精确定义逐项验证。可以按用户授权复用相同图面比较方式，需记录同图不同题干/选项的来源；模型必须收到本题正式原文，不能借364输出凑双测。',
 'Plane321': '迁移427中真实等长边、共有顶点与底边的对照。必须按题干逆时针及第一次覆盖定义验证转角，区分视觉小角和有向转角；不给新角标、箭头、等长符号，不修改原旋转方向。',
 'Plane490': '真实旋转中心C与箭头图形原像/像固定。尝试用真实对应的边/方向部件比较局部对齐和整体旋转；不要仅把角度文字/中心点醒目标出，也不能改变箭头朝向或灰度使图像变成另一物体。该题比427简单，不能以复杂无用标记强凑诱导。',
 'Solid186': '迁移126对被移除外表面与新暴露内表面的真实比较。独立以单位面枚举或等价解析证明涂漆面积比，包含题干要求的底面；不可拿体积比冒充模型的已验证机制，也不可通过着色改变题义中的受漆表面。',
 'Solid226': '迁移126的消失/新增面积对应，比较挖去一英尺立方体后的真实边界。各个丢失/增加面须按原图与实际实体计算，勿从屏幕长度猜面积；原尺寸、虚线、缺口和全六面条件保留，颜色不成为额外涂漆条件。',
 'Solid146': '以142/167真实切口—展开边的对应为方法参考，但本题两条直线剪法未逐一固定。不得新增确定剪线将自由剪法问题改写；独立构造所有可能选项并证明不可能者。与174很接近，仍为不同正式题，须分开保存请求与双测。',
 'Solid174': '与146几乎同型，但原图含剪刀。保持剪刀、折叠及允许两次直线剪法的语义；用已有边/凹口关系迁移红蓝对应，不能把新描边当成第三条剪线或固定本来未限定的剪法。原题每个选项须独立核验。',
 'Solid239': '两次对折后已有虚线剪口，可直接借142/167区分剪口端部/所处折边，并在候选孔洞边缘对应。需准确展开两次，原折层、灰度、虚线和孔洞形状保持；禁止用色改成纸面自身的新增纹样。该题唯一归本单元，不由u07重复设计。',
 'Plane220': '一次对折、已知剪去轮廓与展开后的边缘对应；参考142/167的红蓝比较，但不能引入第二次折叠。仔细区分星形剪口、弧形边和折边所在侧，保留原孔/剪口拓扑；评估彩边被理解为纸张自带内容的语义风险。',
 'Plane194': '两次对折后可剪不同角，任务为排除不能得到者。可用真实折边/剪角边与候选内孔或外角对应，不能以标记固定题干未固定的角而使其他选项答案变化；必须覆盖四个剪角可能性。',
 'Plane245': '两次对折图中已明确剪角，可迁移167两个方向的比较并对应候选孔边。真实切角位于折叠后的哪一类顶点须从原折叠图确认，不以页面朝向类比另一题；保留折线、箭头、原选项。',
 'Solid187': '部分立方体带缺口，与176端盖/瓣的关系比较相近。可比较真实缺口与对应展开边，需以折叠映射验证每个选项，不把“彩色边是实体印刷图案”的额外读法引进来；不补全缺失面或修改凹凸拓扑。',
 'Solid193': '最贴近176的三角瓣配合：一个面沿对角分开，需验证哪些展开图不能闭合。正式选项C与D都写2 and 4，是现存原文，不能擅自修订；应独立验证唯一正确E所列3和5，不把同文错误选项字母混为一次预设命中。标记须针对瓣/边的实际配合。',
 'Solid228': '普通六方格立方体网格可折性，迁移176的真实封闭/重合比较而不是复制其四瓣坐标。需逐候选传播立方面法向与面位置，不能只看二维邻接；原折线和方格数量保持。',
 'Solid166': '当前用户203把x与C标红，本题应从新context独立选一条具体候选边与x配对；标签是1—5，不是A—E。必须用八面体折叠传播验证真接缝，比较边需各自明确，不能凭平面远近或直接沿用源题C。',
 'Solid240': '同为八面体，此题问折叠后Q右侧的编号面，方法可迁移203的真实边/面邻接对应。必须把左右和观察侧绑定右侧立体图，不能把屏幕最近面当最终邻面；不改Q、编号、实虚线或遮挡。'
}

common = '''
USER AUTHORIZATION AND SCOPE
用户明确要求：“帮我按照我标注那9道题的方法，给这24道相近的题每道题标一个类似的specialvar。要满足通过标准。”这次是仅限这24题的新任务；旧457题的一般探索仍暂停。当前用户原话授权此范围内的自动设计、两次quicktest3和后续独立复核，覆盖本地说明中默认不自动批量/测试及默认.runtime草稿路径的限制。所有新内容只放你的OWNROOT；正式目录和已存在工作台状态保持只读。不要请求重复许可，不启动工作台服务器或切换其当前题。

REFERENCE AUTHORITY
先完整读本brief、assignment.json、TASK/task.json、TASK/reference_manifest.json和TASK/reference_style_summary.json，再实际查看每份主参考C01.png并读其C01.json/recipes.json/reference.json。参照的是用户现在保存的9张C01；旧18份交付只是研究历史，不能用其颜色、选项标签或机制描述取代当前像素。动作只表达信息性的对应/比较，不增加等长、平行、垂直、涂漆、切割或印刷条件。

READ-ONLY PROTOCOLS AND HISTORY
完整阅读根AGENTS.md/MATHPALETTE_PROTOCOL.md及涉及分支的REDRAW_PROTOCOL.md、dataset_generator/protocol.json、workbench/README.md、agent_prompt.md、plugin.schema.json。原题/答案/来源以该分支dataset.jsonl为准。读OLD/annotation_semantics_lessons_20261102.json、annotation_semantics_lesson_plane242_r24_20261102.json以及其中相关拒绝理由。TASK/history_index.json列明本题全部已知旧候选、完整原始响应及不成功/中止历史；逐题读取这些实际完整文件与已有独立反对意见，不只看简写终答。旧证据、冻结输入、helpers、审批、.env、.git、.runtime、其他单元均只读。parent任务进度/brief追加是元数据，不能错误当成原图/证据漂移并恢复旧文件；真正冻结字节/输入必须精确核验。

ELIGIBILITY AND PRIMARY MATHEMATICS
在每份设计及每次实际调用之前，以正式dataset、provenance/approvals.json当前内容指纹与来源核验仍是MathVision，且无已Pass Special、无Collect/特殊完成记录。重算原批准内容指纹，不更新审批。研究推荐不等于原题批准/Pass/Collect。正式题干、选项、答案、来源JPG、正式PNG、当前context、原冻结几何须实际独立审阅；保留本题唯一正确解释。所有min/max/不可能/完整排除须有枚举或充分证明/构造，不能把正式答案或此前模型输出当证明。立体分开核验世界几何、投影和冻结显隐。不得修改问题、答案或原图修复问题；真实阻断应如实保存并通知父任务。

DESIGN METHOD AND HUMAN CLARITY
目标为每道题一份可交付的简洁、定向、视觉明显的用户同类方法：优先原有边/点的红蓝比较、开放边界、真实剪口或封边对应。每一组及每条标记都要有具体信息来源、接受对象和用途；不用孤立错误选项显著性来替代诱导信息。可以有较多有效标记，没有任意条数上限；合并同一目标的互不冲突属性编辑，去掉完全覆盖/明显无效动作。新标记不能形成固定假分区、额外切割、移除点、虚构物体/标签/角度关系，不能遮掉决定性灰度、孔形、数字或尺寸。颜色被合理读作纸面自带彩边/图案时，应按该读法检查答案是否仍唯一；不能只说“人类会自动忽略颜色”。若字面合理读法改了题或无选项，淘汰该设计并另找真实信息比较，不能新增文字图例或改题干消除歧义。

LEGAL RENDER AND LOCAL ENVIRONMENT
Python -X utf8 -B；在任何项目/Pillow/数值导入前设自己进程OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=NUMEXPR_NUM_THREADS=1及OWNROOT内TEMP/TMP/MPLCONFIGDIR/XDG_CACHE_HOME，不要改系统环境或.env。安装原OLD/runtime_isolation.py的内存级路径重定向，并再用严格写guard限制新写入到自己的OWNROOT。逐文件流式读历史，释放base64/上下文，关闭图形与临时子进程；当前主机有足够资源采用这些措施，不加复杂共享信号量。Plane使用原mathvision_adapter.RendererAdapter + mathvision_plugins.PluginRenderer；Solid使用原OLD/delivery_bridge_adapter.py的专用MathVision RendererAdapter +正式render_plugins.PluginRenderer。不要编辑共享适配器或渲染算法。固定颜色/点/线/局部区间及线宽遵守实际schema与真实context；不写任意绘图代码绕过插件。fresh schema/默认归一化、原图no-op像素、同一候选两次逐字节一致以及新的独立进程精确重放通过后才能模型调用。保存PNG、插件、context、路径指纹和环境。
普通自己命令的导入路径/变量拼写或tuple与JSON list表示误报可在OWNROOT内离线纠正，保留原错与诊断后重跑所有相关离线门禁；tuple/list只能精确JSON规范化比较，所有数值、顺序、键和路径必须不变，不引入容差。真实几何/内容/哈希漂移、主机分配/渲染故障或API故障不能用重试掩盖；source变化先hold该题，host/API失败结束本批后续调用并保存未工作项目。其他独立数学/语义淘汰可继续本单元其余题。

PRESET, OLD ATTEMPTS AND EXACT TWO TESTS
每份候选调用前保存不可变design.json、具体错误预设（letter/value语义明确）、独立数学证明、逐标记角色、用户参考迁移记录及与所有旧尝试的实质差异审计。新推测必须来自新标记的具体信息关系，而非看新输出再改预设。相同题目的原失败/中止PNG不再测试，精确相同PNG/题干已有实际请求先审计并保留其结果，不能换目录或日期“重新开始”。只换色/线宽/文件名或保留同一失败输入重测不能算新假设。用户明确授权把这9张当前C01的方法迁移到不同正式题；确实同底图时可以同像素，记录source参考和独立题干来源。Plane364与423同底图但选项不同，分别严格发送本题正式全文，不能拿另一题的输出抵数；也不能借其他题已失败PNG做跨题投机。看全局同图历史时精确区分不同正式题干和实际请求，记录此授权迁移的原因。
通过门禁后，每份冻结图只调用原OLD/harness/quicktest3_isolated.py --runs 2，一份图恰好两次真实调用，original quicktest3 / mimo-v2.6-flash / thinking.disabled /原systemprompt/API/private凭据/不设max_tokens等/原timeout行为保持。复制harness到OWNROOT时只能改本地PROJECT/cache定位，保存原SHA、精确diff和反向替换字节相等证明；不能修改远端payload或用mock。模型只见正式题干和同一PNG，不发答案、原图、预设、机制、历史或参数。不要联网ping、控制组连通性测试或另加模型调用；旧control可只读保留，没有“原图必须正确”或因果增益的额外门槛。
完整读两次raw与终答。两次都必须是完整非截断响应且最终字母和值与事前预设一致；正文偶然提到、末尾字母/数值冲突、错误预设之外的其他错误均不是命中。不得第三次调用、挑两次成功、事后改标、自动重试或把已失败/中止请求恢复测试；网络HTTP/传输失败保留原始与partial，结束自己的后续调用。只在核准自己PID与命令后中止真正停滞请求，记录实际状态并不重试。每次原始request、binding、started、design_snapshot、raw、summary与哈希永久保留。

PERSISTENCE, CHECKPOINT AND REVIEW HANDOFF
评估全部assigned，追求每题一份满足双测的主审候选，不继承旧“找到3份就停”限制，不因节省额度停止。某一实质设计未双中时，若有新的、有效且不同的信息对应假设可继续设计；每次失败全部保留。不可仅以第一次失败就宣称该题无解，也不可用无用/混乱标记强凑命中。对确实无可靠语义方案、真实输入问题、主机/API阻断或尚未解决者，保存具体证明/阻断与未完成状态，不能伪造完成。每份成功只作为PRIMARY候选；必须父任务另外创建全新独立二审后才可交付。不得自称独立二审、用户审批或正式Pass/Collect。研究推荐只支持这两次观察，不能声称总体成功率、因果增益或所有响应都验证预设机制。
持续保存checkpoint.json、second_review_queue.json（没有候选也保存空数组）、逐题完整数学/原生图片/每条标记/迁移/历史差异/两次终答/绑定/当前资格/来源保全/错误与holds/skips/unworked，以及所有自有API进程结束证据。候选队列至少含question_id、variant_id、candidate_directory、image/plugin/design SHA、原正确答案、冻结错误预设、两个完整终答、summary路径、主审审查路径、参考迁移路径和所有限制。保证每个assigned都有明确结果或未完成原因，不能漏题。完成时关闭自己的API与本地子进程，保持其他单元/父任务内容只读。最终报告主审候选、真实调用数量、错误/中止/未工作项目与证据路径；不得发布或执行正式状态动作，也不启动子代理/服务器/工作树或扩大范围。
'''

seen=[]
plan=[]
for unit_id, title, qids, ref_ids in units:
    own = TASK/'units'/unit_id
    own.mkdir(parents=True, exist_ok=False)
    selected = []
    for q in qids:
        e=eligibility[q]
        assert e['eligible'] and e['formal_record']['source_dataset']=='MathVision'
        assert all(sha(ROOT/p)==h for p,h in e['frozen_source_files_sha256'].items())
        selected.append({**e,'primary_reference_question_ids':ref_ids,
                         'tentative_transfer_direction_not_a_preset_or_proof':directions[q]})
    assignment={
      'schema_version':'1.0.0','created_at_utc':created,'unit_id':unit_id,'title':title,
      'mode':'user_current_C01_style_transfer_research','status':'prepared_not_launched',
      'own_root':str(own),'task_root':str(TASK),'project_root':str(ROOT),'old_research_root':str(OLD),
      'question_count':len(qids),'question_ids':qids,'questions':selected,
      'references':[{**styles[q],'reference_manifest_entry':references[q]} for q in ref_ids],
      'related_history_index':str(TASK/'history_index.json'),
      'required_parent_scope_files':{p:sha(TASK/p) for p in ['task.json','eligibility_initial.json','reference_manifest.json','readonly_source_sha256.json','reference_style_summary.json']},
      'reference_material_policy':'Use current frozen user9 C01 images/actions; old18 packages are history only.',
      'root_reserved_question':'Plane213','scope_overlap':False,
      'new_model_calls_at_preparation':0,'new_designs_at_preparation':0,
      'independent_review_performed':False,'formal_edits_or_approvals_performed':False,
      'worker_goal':'Assess all assigned and seek one credible user-style two-hit PRIMARY design for each; further new independent review belongs to parent.',
      'no_three_candidate_early_stop':True,'quota_saving_stop_forbidden':True,
    }
    save(own/'assignment.json',assignment)
    lead=f'''MathVision用户当前9张C01迁移任务：{unit_id} · {title}
OWNROOT={own}
TASK={TASK}
OLD={OLD}
PROJECT={ROOT}
唯一研究范围：{', '.join(qids)}（共{len(qids)}题）。Plane213由父任务处理，不在任何worker范围。
主参考：{', '.join(ref_ids)}。研究所有assigned，不能找到任意3个候选就提前结束。你不是独立二审，不运行自己的子代理。
先确认本目录assignment.json/brief.txt原字节，后续保留它们；你的所有新文件及临时缓存只写OWNROOT。父任务只准备了范围/来源指纹，未替你完成数学、候选图、预设或模型调用门禁。

当前参考的实际像素方法：
'''
    for r in ref_ids:
        lead += f"- {r}: {styles[r]['observed_style']}\n  {styles[r]['current_source_option_relation']}\n  {styles[r]['migration_rule']}\n"
    lead+='\n逐题原文与待核验方向（这些只是方向，不是预设、证明或可调用批准）：\n'
    for q in qids:
        rec=eligibility[q]['formal_record']
        lead += f"\n{q} | branch={eligibility[q]['branch']} | 正式答案={rec['answer']}\n{rec['question']}\n迁移方向与本题特殊门禁：{directions[q]}\n"
    text(own/'brief.txt',lead+common)
    seen.extend(qids)
    plan.append({'unit_id':unit_id,'title':title,'question_count':len(qids),'question_ids':qids,
                 'reference_question_ids':ref_ids,'assignment':str(own/'assignment.json'),
                 'brief':str(own/'brief.txt'),'assignment_sha256':sha(own/'assignment.json'),
                 'brief_sha256':sha(own/'brief.txt'),'own_root':str(own),
                 'clientRequestId':'mathvision-user9-transfer-20261102-'+unit_id,
                 'state':'prepared_not_launched'})
assert len(seen)==len(set(seen))==23
assert set(seen)==set(task['scope'])-{'Plane213'}
assert not any(q=='Plane213' for q in seen)
assert all(sha(ROOT/p)==h for p,h in initial_sources.items())
save(TASK/'prepared_dispatch.json',{
 'created_at_utc':created,'status':'prepared_not_launched','worker_units':len(plan),'worker_question_count':len(seen),
 'root_reserved_question_ids':['Plane213'],'root_reserved_path':str(TASK/'root_213'),
 'total_scope_question_count':24,'all_24_covered_once':True,'active_worker_overlap':False,
 'delegation_not_performed_by_preparer':True,'new_model_calls':0,'new_designs':0,
 'current_reference_style_summary':str(TASK/'reference_style_summary.json'),
 'parent_scope_sources_verified':len(initial_sources),'old_general_exploration_stays_paused':True,
 'provider_policy':'Inherit original Codex provider/model/options; do not switch provider/model unasked.',
 'units':plan})
save(TASK/'preparation_verification.json',{
 'at_utc':datetime.now(timezone.utc).isoformat(),'worker_units':len(plan),'worker_questions':23,
 'root_reserved_questions':1,'total_exact_unique_scope':24,'question_ids':seen,
 'root_scope_matches':True,'all_units_disjoint':True,'all_9_current_C01_images_actually_viewed':True,
 'initial_376_source_hashes_match':len(initial_sources)==376 and all(sha(ROOT/p)==h for p,h in initial_sources.items()),
 'all_reference_plugin_and_PNG_hashes_match':True,
 'new_API_calls':0,'new_candidate_images':0,'formal_writes':0,'subagents_or_T3_calls':0,
 'outputs':[str(TASK/'prepared_dispatch.json'),str(TASK/'reference_style_summary.json')]+[x['assignment'] for x in plan]+[x['brief'] for x in plan],
 'no_background_process_started':True,
})
print(json.dumps({'units':len(plan),'worker_questions':len(seen),'root_reserved':['Plane213'],
                  'total':24,'source_hashes_verified':len(initial_sources),
                  'dispatch':str(TASK/'prepared_dispatch.json'),'style_summary':str(TASK/'reference_style_summary.json')},ensure_ascii=False))

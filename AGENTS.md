# MathPalette 工作说明

创建或修改题目、变体和数据流程前，阅读根目录 `MATHPALETTE_PROTOCOL.md` 以及对应分支协议。

仅用户明确确认的原题进入正式数据。三个分支 `dataset.jsonl` 都只包含正式题；根目录 `question_bank.jsonl` 是 `dataset_tools/catalog.py build` 生成的汇总。不得恢复旧候选清单或把 Special Pass/Collect 当成原题通过。

正式题号统一：Analytics 的 DynaMath 使用 Ana01～Ana20，MathVerse 使用 Ana21～Ana45，MathVista 使用 Ana46；几何题当前使用 Plane01～Plane71、Solid01～Solid16。新增题号继续递增，不复用、不建立另一套 formal/candidate 编号。

用户通过原话、时间及当前内容指纹在 `provenance/approvals.json`。改题干、答案、绘图输入或原图时，须用户重新确认后更新记录。迁移仅在题干、答案及像素一致的核验通过后更新路径/编号指纹，保留旧指纹和原审核时间。

使用 `dataset_tools/question_review.py 分支 题号 --instruction "用户明确通过原话"` 保存审核并同步索引；不得用修改指令、数学检查或本工具执行成功代替用户批准。

Base 使用 `Analytics/dataset_generator/generate_base_variants.py`，每题从 Base1～Base6 不放回抽四种。三个分支的 Special 分别使用各自 `workbench/`，由用户 Pass / Collect。不得伪造通过记录。

平面、立体分别使用分支 `REDRAW_PROTOCOL.md` 和 `dataset_generator/protocol.json`；立体须分别冻结三维几何、投影和可见性。两个几何分支的 Base 尚未启用；Special 工作台需求见 `GEOMETRY_WORKBENCH_REQUIREMENTS.md`。原对象实虚线覆盖属于变体外观操作，不改写原冻结场景。

未通过的新题在独立暂存区制作，不写进正式目录或清单。临时输出放 `.runtime/`；运行时缓存、日志和预览不作为正式数据。来源图片缺失时如实记录，不用重绘图冒充。

用户已明确要求删除旧评测日志和分数，不从旧实验报告恢复这些文件。清理不修改 `.git` 历史或 `.env`。

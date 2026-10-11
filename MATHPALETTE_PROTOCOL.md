# MathPalette 数据协议

版本：3.1.0，2026-10-11。本目录只保留正式通过的数据及其必要运行依赖。

1. **统一身份。** 同一道题的正式清单、图片、脚本、Base 和 Special 使用同一题号。Analytics 当前为 Ana01～Ana45，PlaneGeometry 为 Plane01～Plane16，SolidGeometry 为 Solid01～Solid16。旧题号仅供迁移追溯。
2. **用户通过后收集。** 当前 77 题包含用户本次明确确认的旧 20 道 DynaMath。其余 57 题沿用既有用户通过原话与时间；Agent 数学检查、图像核验和 Special Pass 不替代原题审核。
3. **最小正式记录。** 保留题号、来源、当前题干、答案、答案类型、重绘图、来源图、绘图程序；几何题另保留冻结场景。来源图缺失写 `null`。有改编或来源答案冲突时保留必要来源说明。
4. **可复现依赖。** 公共绘图器、机器协议、固定坐标、投影/显隐区间、依赖版本和变体 recipes 均属于必要文件。PNG 可直接使用，SVG 可从冻结场景导出，不保留重复矢量产物。
5. **通过记录。** `provenance/approvals.json` 保存用户原话、原通过时间和内容指纹。当前内容改变后校验失败，必须重新获得用户确认；不能自动刷新指纹冒充审核。清理迁移保留旧指纹，并核对所有原图和变体像素不变。
6. **索引。** 各分支 `dataset.jsonl` 是正式清单，根目录 `question_bank.jsonl` 是派生汇总。运行 `python -X utf8 -B dataset_tools/catalog.py build` 更新，`check` 检查审核指纹、文件与变体。工作台、Base 和评测入口读取正式清单。
7. **变体。** Analytics 自动生成四份 Base，平面与立体的 Base 尚未启用。三个分支分别使用独立 Special 工作台，由用户逐份 Pass，整题 Collect。每份保留插件、图片、recipes 和重绘入口。平面与立体首版开放对象颜色与实虚线覆盖、标记点、辅助虚线及已有点吸附，具体范围见 [工作台需求](GEOMETRY_WORKBENCH_REQUIREMENTS.md)；变体不改写原题冻结输入。
8. **暂存隔离。** 未通过新题放在独立暂存区。只有明确通过并完成校验后才迁入正式目录、记录审核并更新索引。临时重绘、服务缓存、草稿及评测结果写 `.runtime/`。

分支规则：[Analytics](Analytics/MATHPALETTE_PROTOCOL.md)、[PlaneGeometry](PlaneGeometry/REDRAW_PROTOCOL.md)、[SolidGeometry](SolidGeometry/REDRAW_PROTOCOL.md)。

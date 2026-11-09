# We-Math 454 题正式入库

本次加入 454 道已审定题：Analytics 的 Ana132～Ana546（415题）和 SolidGeometry 的 Solid289～Solid327（39题）。正式库共1472题；既有1018题及1132张 Special 不变。本次没有执行 Special Pass / Collect，也没有声称逐题人工点击批准。

## 来源与许可

来源为 [We-Math/We-Math2.0-Standard](https://huggingface.co/datasets/We-Math/We-Math2.0-Standard)，固定版本 `19064a4b3be262db1fadc952d03b3102acccf942`，split 为 standard，保留源 ID `standard/<id>`。完整469条来源记录见 [source_records_all469.json](source_records_all469.json)，固定来源见 [source_lock.json](source_lock.json)。

Runqi Qiao 等，*We-Math 2.0: A Versatile MathBook System for Incentivizing Visual Mathematical Reasoning*，2025，[arXiv:2508.10433](https://arxiv.org/abs/2508.10433)。上游[固定README许可段](https://github.com/We-Math/We-Math2.0/blob/cd07418521cc825928644af388652bfd60f2a935/README.md#-license)明确规定数据为 **CC BY-NC 4.0**。许可证全文见 [CC-BY-NC-4.0.txt](CC-BY-NC-4.0.txt)。使用来源材料及改编需署名、限非商业并遵守其他适用条件；代码许可不改变数据许可。本次改编不意味着原作者认可。

从 Analytic Geometry 的469题中保留454题；[排除清单](exclusions.json)的15题继续排除。454张来源图片保留原始字节，不以重绘图冒充原图。21题为协议重绘、排版或答案修正，433题为满足协议与视觉必要性而修改题干、答案或几何的重构。当前改编不应被当作上游题干、答案或图形的逐字复刻。[review.json](review.json)保留来源题干/答案、改编历史、数学检查、视觉必要性说明和433组反事实证据；这不是模型实测正确率报告。

## 批量授权与透明元数据恢复

新增审批使用用户明确准许公开的唯一原话：把通过审核的题目并入正式工作台（我默认允许了）。本次属于审查通过后准入的条件批量授权，不等同于逐题人工批准。

已保存交付包提供了正式记录、图像、冻结场景、脚本、运行依赖与历史内容哈希，但没有提供原正式 source_notes 对象正文。因此，本次来源说明从归档审查证据重建，保留旧说明/内容哈希作为历史参考，**不声称逐字恢复旧说明或复现旧内容指纹**。原批量授权时间为2026-11-08T16:34:24.538566+00:00。新内容指纹绑定重建后的来源说明，并采用2026-11-09再次确认的授权时间。既有1018题的审批、来源说明及资产不变。

迁移逐题对应见 [metadata_restoration_20261109.json](metadata_restoration_20261109.json)，历史映射见 [historical_formal_mapping_20261108.json](historical_formal_mapping_20261108.json)。此前语义审查证据与本次代码/哈希/入口重绘验证分别记录，恢复元数据不代表重新进行整批人工审查。

历史批准指纹中的 authorization_record 保留归档包的原相对路径，其目标对应本目录 historical_formal_mapping_20261108.json。review.json 内 hashes.render_scene_sha256、source_preview_sha256 与历史场景路径是原交付包引用，不声称当前正式路径包含这些归档副本；当前 scene_path 对应 hashes.formal_scene_sha256。来源图和正式图使用当前 images 路径，反事实图/场景使用 counterfactuals 路径。所有历史哈希保持不变。

## 重绘与验证

使用仓库规定的 CPython 3.13.9、NumPy 2.5.3、Matplotlib 3.11.2、Pillow 12.3.0 和 FreeType 2.14.3。正式记录的 script 是逐题入口，runtime_dependencies 为按内容冻结的依赖。输出写入 `.runtime/`，不覆盖正式图像。例如：

```
python -X utf8 -B Analytics/dataset_generator/questions/function_plot132.py .runtime/reproduced/Ana132.png
python -X utf8 -B SolidGeometry/dataset_generator/solid_plot289.py .runtime/reproduced/Solid289.png
python -X utf8 -B dataset_tools/catalog.py check
```

本次恢复后的逐454正式入口均需双次重绘，核对交付图像像素，另运行审批、索引、数据完整性及官方工作台检查。最终本次结果见 `release_validation_20261109.json`；归档历史报告不代替当前运行结果。反事实证据位于本目录 `counterfactuals/`，它们不是 Special 变体。

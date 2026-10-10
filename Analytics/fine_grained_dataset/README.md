# MathPalette 细粒度题目数据

当前包含 66 道冻结题目：Ana01～Ana20 来源为 DynaMath，Ana21～Ana66 来源为 MathVerse。原图位于 `image/`，四字段题目记录在 `dataset.jsonl`。Base 自动生成，每题四张；Special 由用户在工作台制作。

本批 MathVerse 原题与来源 GT 原样保留，核验候选和疑点在 `provenance/MathVerse/`，来源图在 `originals/`。不同原始坐标范围通过逐题冻结的坐标映射适配统一画布；轴刻度仍显示来源中的数值。新题进入 Special 待办，不生成虚假的 Pass / Collect。全批见 [对照页](../../imports/mathverse_vision_dominant/redraw_review.html) 与 [核验疑点](../../imports/mathverse_vision_dominant/issues.md)。

完整流程见 **[MATHPALETTE_PROTOCOL.md](../MATHPALETTE_PROTOCOL.md)**。

在 Research 目录执行：

```powershell
# 创建 function_plot21.py / class Ana21 后，准备新题
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/prepare_question.py Ana21

# 批量生成 Base，跳过已有且一致的结果
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/generate_base_variants.py generate

# 核对全部文件及插件重绘
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/generate_base_variants.py check --redraw

# 查看 Special 待办；新增题目重启工作台后自动进入列表
python -B MathPalette/Analytics/fine_grained_dataset/dataset_generator/prepare_question.py --pending
```

双击 `start_special_workbench.cmd` 打开或重启本批 Special 工作台。备份时连同相邻 `fine_grained_special_workbench/` 一起保留。用户 Pass 后保存 C 图片/插件，Collect 后从待办隐藏。

每题 Base 位于 `base_variant/AnaNN/`，含 `images/AnaNN_base_variant_1.png`～`_4.png`、同名 `plugins/*.json`、`recipes.json`、`draw_variants.py`。全局汇总是 `base_variant/generated_index.jsonl`。槽位编号只表示抽样顺序，真正操作为 Base1～Base6。

```powershell
python -B MathPalette/Analytics/fine_grained_dataset/base_variant/Ana01/draw_variants.py base_1
```

旧人工 A/B 已移至 `archive/`，不混入当前 Base。`dataset_generator/render_variants.py` 和旧 baseline manifest 供历史回放；新流程通过每题独立基线支持追加题目。

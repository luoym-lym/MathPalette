# Kayla Special 选择性同步核验（2026-10-18）

基线 master：376a8c41c3c72b997df4f0439ab3f414d63d163d。
来源 kayla：e59c9f6f3d1f17a14cbca24e8f102c9ce6a7f3e1。
不合并旧分支；仅复制 Ana42、Ana43 的完整 Special 包，向 master 的 accepted/collected 索引追加对应 3/2 条记录，并用 catalog build 重建 question_bank。原题、审核指纹、其他变体和主分支新增数据保持原样。

| 变体 | 操作 | 核验 |
| --- | --- | --- |
| Ana42/C01 | curve_001 蓝色实线，1 pt | 原题快照、插件/schema、冻结参数及文件/像素哈希通过；离线重绘完全一致 |
| Ana43/C01 | 红点 (0,-2)、(1,2) | 同上 |
| Ana43/C02 | 蓝色虚线 (0,-2) 至 (3,2)，1 pt | 同上 |

三份 recipes 的 status=passed、reviewed_at 和 collection 的 collected_at 原样保留。collection 的原题快照等于 master 正式记录；两题的来源图、正式图、绘图脚本以及公共渲染器/schema 在两分支间一致。当前原题审核通过 catalog 校验，未刷新任何批准指纹。

## Ana43 待复审的含义与保留事项

依据 Analytics/workbench/README.md “特殊情况与后期复审”、review_store.py 的 mark_special/collect 和 catalog.py：特殊标记只完成整题工作进度，保留已有通过变体；pending 不撤销逐图 Pass。catalog 根据 recipes 的 passed 状态收录，并不将 pending 当作失败。master 的 Ana35 已有相同的 pending + 两份 passed 记录。因此本次收录三份已有 Pass 的变体，同时完整保留 Ana43 current.special_case=true、review_status=pending；不宣称整题复审结束，不新建或伪造人工批准。

Ana43 原线为 y=7x/4-1。两个红点均不在该线上；蓝色虚线斜率为 4/3，区别于原线的 7/4。当前插件协议允许添加这些标记，它们不改写原线、原题或答案。但是否为预期干扰、是否还要补做其他标注，需要人工重新打开 Ana43 复审后正常 Pass/Collect；现有记录未提供特殊标记的具体原因，不能替协作者推断。不可通过删除 pending 来冒充复审完成。

## 复现与一致性

使用隔离环境 Python 3.13.9、matplotlib 3.11.2、numpy 2.5.3、pillow 12.3.0，直接执行原 draw_variants.py C01/C02；未修改 recipes、未绕过环境或像素检查。三次 matches_accepted=true。默认 Python 3.12.14 环境被原重绘入口正确拒绝（environment_changed），需使用上述冻结版本。

当前 master 的整体基线虽因其他题更新而不同，但仓库已有 _baselines/9710d1da1257ed572c47d21850835129b834edffe5a44e3a4a929bb4c6254309.json；原 replay_archived 正常验证本题依赖未变后完成重绘，无需更改冻结哈希。

同步结果：251 道原题、0 Base、144 张 Special；Analytics 116、PlaneGeometry 21、SolidGeometry 7；覆盖 42 道原题。accepted 索引追加 3 条、collected 索引追加 2 条，collection 的 slots/count 与 recipes 一致。正式清单由 catalog build 生成，catalog check 检查。此数量包含已 Pass 的 Ana43 两张图，不代表 Ana43 整题复审已结束。

附加检查：现有 `check_special_cases.py Analytics` 的 7 项测试全部因测试夹具缺少 source_dataset 字段而报 KeyError；本次未修改该测试或 review_store。该结果不能报告为通过，也不影响已独立完成的真实记录核验和三张图像素复现。

并发状态核验：发布时发现远端已由 fdcecc96751dc337741646a5e68a8958530564f9 完成相同的数据同步。已核对其 12 个传入文件逐字节等于本次验证的 kayla 原件，索引、README 和 question_bank 也与本次生成结果一致。本次仅追加核验报告，不覆盖该并发提交。

# 2026-10-09 目录整理与核对

四个原目录整体搬入 `Analytics/`：`fine_grained_dataset`、`fine_grained_special_workbench`、`special_variant_workbench`、`val_script`。根目录 `.env` 保留原位置，三个评测入口继续默认读取它。

[reorganization.json](reorganization.json) 保存搬迁前 1,809 个文件的 SHA256、目录映射和搬迁后核对。冻结绘图输入、题目记录、原图、Base / Special 的正式图片、插件、recipes、索引和 collection 记录保留原有字节。当前说明文档及评测入口按新路径更新；工作台启动核对刷新运行时缓存。

已核对 20 张原图、80 张 Base、Base 全局索引和三个评测数据加载入口；未发起模型 API 请求。工作台读取到 20 道已 Collect 题目、72 份已 Pass Special，待办为空，未生成候选或新增审核记录。

最终核对期间，一个独立的 `evaluate_special.py` 进程（PID 3724）已从新目录续跑 `trace_special_qwen35_4b.json`，其中路径迁移历史已记录，完成试次保留。该 trace 与锁文件由正在运行的评测进程使用，审计单独记录这些运行时变动；未打断进程或覆盖其输出。

## 已有 Special 重绘限制

[special_replay_report.json](special_replay_report.json) 记录全部 72 份 Special 的逐图核对：64 份重绘像素一致，以下 8 份因既有源码基线不一致而被原重绘器拒绝：

- `Ana10/C01`～`C04`。
- `Ana14/C01`～`C04`。

这两题的当前源码与搬迁前哈希相同；旧 Special recipes 绑定的源码哈希已不匹配搬迁前文件，且不在现有来源补录兼容映射中。本次保留既有图片、插件和人工审核记录，不改写基线来绕过核对。这不影响目录搬迁、原图 / Base 重绘或评测图片加载；如果要恢复这 8 份重绘，需要另行查找其通过时的原始源码。

旧 `service.json` 为已退出进程的残留登记，没有正在运行的服务需要迁移。当前工作台可通过 `../fine_grained_dataset/start_special_workbench.cmd` 启动，地址仍为 `http://127.0.0.1:8767`。

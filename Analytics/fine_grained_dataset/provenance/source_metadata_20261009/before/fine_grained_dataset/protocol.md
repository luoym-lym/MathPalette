# 当前数据协议入口

组织协议版本：2.0.0。

完整的新题制作、原图生成、Base 插件和 Special 待办流程见仓库根目录的 **[MATHPALETTE_PROTOCOL.md](../../MATHPALETTE_PROTOCOL.md)**。

- 来源：每道题在自身 class 的 `__init__` 中显式定义 `self.source_dataset`，并以 `self.source_id` 单独记录原始题号。Ana01～Ana20 的来源均为 `DynaMath`；历史 `custom_XX` 标识不表示自建题，也不代表已核实的来源题号。旧题字段补录须兼容既有源码哈希和重绘基线，详见完整协议的“来源标注”。
- Base：每题从 Base1～Base6 不放回抽取四种，每张独立作用于原图；自动保存四张图、四份插件、recipes、重绘函数和全局索引。
- 机器参数：[dataset_generator/base_protocol.json](dataset_generator/base_protocol.json)。形状中心在 `[-6,6]²`，宽高各为 `0.8～2.5`。
- 新题入口：[dataset_generator/prepare_question.py](dataset_generator/prepare_question.py)。生成原图、登记 JSONL、生成及核对 Base；Special 重启后接收新题为待办。
- 原图样式：[dataset_generator/protocol.json](dataset_generator/protocol.json)。
- Special 使用人工 Pass / Collect，见 [工作台说明](../fine_grained_special_workbench/README.md)。

旧 A=5/B=5、人工 Base 通过和随机补齐规则已经退出当前流程；原文存于 [provenance/protocol_v1_legacy.md](provenance/protocol_v1_legacy.md)，用于解释历史归档。

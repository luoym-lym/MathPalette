# Ana01～Ana20 来源补录

2026-10-09：按用户要求，将 20 个题目类的来源统一为
`self.source_dataset = 'DynaMath'`，移除当前类中的 `source_id`，
并同步新题字段检查和 Special 工作台的来源输出。

- `before/`：修改前的题目源码、Base recipes / 索引、相关代码和状态备份。
- `migration.json`：本次元数据修改前后的精确源码哈希，以及工作台适配器的指纹对应关系。
- `preflight.json`：修改前的文件哈希及已存在的 Special 基线不匹配记录。
- `verification.json`：字段、像素、工作台启动与审核记录保留的检查结果。

题目源码已核对：排除来源字段和类说明后，Python 语法树一致。
20 张原图和 80 张 Base 的重绘像素一致；Base 仅更新源码基线及其派生索引。
Special 的正式图片、插件、recipes、人工审核记录和实际工作台状态保持原样。
旧 Special 重绘及工作台启动只允许 `migration.json` 登记的精确指纹变更，
重绘仍须匹配已通过图片的像素。迁移记录和相应旧文件是兼容检查的依赖，
须随数据集一起保留。

64 个 Special 变体重绘通过。Ana10、Ana14 各 4 个 Special 变体在本次修改前
已有源码指纹不匹配；该问题保留在核对报告中，未将其归入本次元数据兼容范围。

# MathVista 正式题来源

本轮用户逐题通过 56 题：Ana46，以及 Plane17～Plane71。题号映射、通过按钮凭据、文件哈希和两次重绘核验保存在 [imports.json](imports.json)。每份 `<正式题号>.json` 原样保存对应的完整来源记录，包括 MathVista ID、原题、选项、官方答案和上游数据集等字段；记录中的 `image` 是上游路径，正式来源图片路径以根目录 [question_bank.jsonl](../../question_bank.jsonl) 为准。

来源图片与候选包中的原始图片逐字节一致；正式 PNG 与用户点击 Pass 时的展示图片一致。独立执行正式绘图程序，两次输出均与正式 PNG 像素及文件哈希一致。14 题的场景仅迁移 `source_metadata` 路径，核对题干、答案、几何输入及像素不变后更新指纹，保留原通过时间及旧指纹，详情见 `imports.json` 的 `source_path_migrations`。正式脚本不依赖审核网页或候选目录。

数学核验、改编说明和候选内容快照已包含在 [source_notes.json](../source_notes.json)，用户批准以 [approvals.json](../approvals.json) 为准。候选快照中的路径和制作状态属于历史信息，不作为当前文件入口或当前审核状态。

后续统一数据格式时，选择题答案转为选项字母，场景中的重复题目信息和来源元数据指针已清理；逐题原始来源记录仍保留于本目录，正式数据集名称由 `dataset.jsonl` 的 `source_dataset` 保存。该表示迁移与原始通过记录之间的对应关系见 [schema_normalization.json](../schema_normalization.json)。

## 署名

本批来源为 [MathVista testmini](https://huggingface.co/datasets/AI4Math/MathVista)。以下署名及许可通知迁自原候选包，保留与本批正式题有关的条目。

MathVista: Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, Jianfeng Gao. *MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts*. ICLR 2024. [项目](https://github.com/lupantech/MathVista) · [原始来源索引](https://huggingface.co/datasets/AI4Math/MathVista/blob/main/source.json)

| 来源 | 本批正式题数 | 原项目及署名 |
| --- | ---: | --- |
| Geometry3K | 35 | [InterGPS](https://github.com/lupantech/InterGPS), Lu et al., ACL 2021 |
| GEOS | 10 | [GEOS](https://geometry.allenai.org/), Seo et al., EMNLP 2015 |
| IconQA | 5 | [IconQA](https://iconqa.github.io/), Lu et al., NeurIPS 2021 |
| TheoremQA | 3 | [TheoremQA](https://huggingface.co/datasets/TIGER-Lab/TheoremQA), Chen et al., EMNLP 2023 |
| UniGeo | 2 | [UniGeo](https://github.com/chen-judge/UniGeo), Chen et al., EMNLP 2022 |
| FunctionQA | 1 | [MathVista](https://github.com/lupantech/MathVista), Lu et al., ICLR 2024 |

重绘及有记录的改编由 MathPalette 制作，不代表原作者认可。

## 保留的上游许可通知

- MathVista 新增贡献采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)，原始题目和图片版权归原作者；[上游说明](https://github.com/lupantech/MathVista#-license)另注明测试集用途及不用于训练集。本包不对全部原题图作统一重新许可。
- IconQA 采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)，保留其署名、非商业和相同方式共享条件；[上游通知](https://iconqa.github.io/#download)。
- MIT 版权及全文保留于 [InterGPS](LICENSES/InterGPS-MIT.txt)、[TheoremQA](LICENSES/TheoremQA-MIT.txt)。

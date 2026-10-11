# 数据来源

本批 227 题来自 [MathVista testmini](https://huggingface.co/datasets/AI4Math/MathVista)，逐题保留 MathVista ID、来源数据集、源记录、原图、原题及官方答案。[来源题号清单](publication_source_inventory.json)。

MathVista: Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, Jianfeng Gao. *MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts*. ICLR 2024. [项目](https://github.com/lupantech/MathVista) · [原始来源索引](https://huggingface.co/datasets/AI4Math/MathVista/blob/main/source.json)

| 来源 | 题数 | 原项目及署名 |
|---|---:|---|
| GeoQA+ | 62 | [GeoQA-Plus](https://github.com/SCNU203/GeoQA-Plus), Cao and Xiao, COLING 2022 |
| Geometry3K | 62 | [InterGPS](https://github.com/lupantech/InterGPS), Lu et al., ACL 2021 |
| UniGeo | 62 | [UniGeo](https://github.com/chen-judge/UniGeo), Chen et al., EMNLP 2022 |
| GEOS | 22 | [GEOS](https://geometry.allenai.org/), Seo et al., EMNLP 2015 |
| IconQA | 10 | [IconQA](https://iconqa.github.io/), Lu et al., NeurIPS 2021 |
| FunctionQA | 4 | [MathVista](https://github.com/lupantech/MathVista), Lu et al., ICLR 2024 |
| TheoremQA | 3 | [TheoremQA](https://huggingface.co/datasets/TIGER-Lab/TheoremQA), Chen et al., EMNLP 2023 |
| SciBench | 1 | [SciBench](https://huggingface.co/datasets/xw27/scibench), Wang et al., ICML 2024 |
| IQTest | 1 | [MathVista](https://github.com/lupantech/MathVista), Lu et al., ICLR 2024 |

## 重绘与改编记录

216 题保留原题进行协议重绘；11 题有明确改编。各题页面保留修改前后内容、原因、答案与推导，完整清单见[审核入口](README.md)。这些修改由 MathPalette 制作，不代表原作者认可；所有题目均待用户逐题审核。

## 上游版权与许可通知

- MathVista 新增贡献采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)，原始题目和图片版权归原作者；[上游说明](https://github.com/lupantech/MathVista#-license)另注明测试集用途及不用于训练集。本包不对全部原题图作统一重新许可。
- IconQA 采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)，保留其署名、非商业和相同方式共享条件；[上游通知](https://iconqa.github.io/#download)。
- MIT 版权及全文保留于 [InterGPS](LICENSES/InterGPS-MIT.txt)、[TheoremQA](LICENSES/TheoremQA-MIT.txt)、[SciBench](LICENSES/SciBench-MIT.txt)。

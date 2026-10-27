# MathVision 原题人工审核候选

这是 **696 道待人工审核**的 MathVision 几何题初始导入包，不是正式题库，不代表用户 Pass。来源是已完成独立复核的三个最终重绘包；未重新采样、改答案或恢复排除题。

| 原始来源类别 | 待审核 | 排除记录 |
|---|---:|---:|
| combinatorial geometry | 296 | 12 |
| solid geometry | 240 | 4 |
| transformation geometry | 160 | 8 |
| 合计 | 696 | 24 |

当前待审核队列以 `index.jsonl` 为准，实际人工决定以 `review_state.json`（首次决定后创建）和正式批准凭据为准。上表与 `summary.json` 只描述最初导入范围，不能拿它们恢复已通过/删除题目。

## 身份和来源

- `MVI####` 是审核候选编号，数字部分就是 MathVision 原始 ID；与 MathVerse 的 `MV####` 不冲突。
- `source_dataset="MathVision"`、`source_key="test:<原始ID>"`；固定数据版本为 `2837ddb3f13abaf6b3997c12d80753e5470bd46a`。
- `source_category` 原样保留上游三个分类。正式分支按冻结场景的二维/三维模型确定：429 道 `PlaneGeometry`、267 道 `SolidGeometry`。19 道组合几何和8道变换几何具有真实三维场景，因此没有错误降成平面场景。
- `original_question`、`original_answer`、`original_options` 和 `provenance.json/original_record` 保留原始内容。`question` 仅在必要时追加原样选项的 `Choices:` 排版以兼容现有答案 schema；不改选项值、不改答案。
- 图片、冻结场景、原入口、局部渲染器及审核证据均从最终包复制；逐题 `verification.json` 是 Agent 独立核验，不是用户批准。

`excluded.json` 保存全部24个排除决定、原因与证据定位；`excluded_reviews/` 保存相应证据。它们不进入待审核清单。排除题的原图不在本审核包中，账本中的 `original_preserved` 是历史来源记录的声明，不表示本包附带原图；排除不一定意味着原始答案错误。

`source_packages/` 中保留三个最终包的历史汇总、质量清单和验证报告。里面的路径/数量/哈希描述原最终 ZIP 的布局，不是本工作台当前状态；当前路径以 `index.jsonl` 为准。原题版权及许可沿用来源数据集，本导入不授予额外授权。

## 离线重绘

参考环境：CPython **3.12**、NumPy **2.3.5**、Matplotlib **3.10.8**、Pillow **12.3.0**。MathVerse 的冻结环境不同，不要为了本包覆盖原 MathVerse 环境。

```bat
python -m pip install -r review_candidates\mathvision\requirements.txt
python -B review_candidates\mathvision\items\MVI0011\redraw.py .runtime\MVI0011.png
python -B review_candidates\mathvision\validate_package.py --formal --twice --workers 4
```

跨版本运行可能产生文字栅格差异；审核 Pass 时仍须逐像素一致，不会静默覆盖参考 PNG。`redraw.py` 接收显式输出路径；不传参数则写 `.runtime/mathvision_redraw/`。不是所有历史入口都输出 SVG，请以 PNG 作为统一复现格式。

原始 `source_redraw.py` 是保留的历史入口，它会向旁边写 PNG/SVG/报告，**不要直接运行它**。新 `redraw.py` 通过 `shared/runtime.py` 在独立临时目录重建历史路径，只复制当前题的冻结输入与必要共享绘图器，再执行原入口。现成参考 PNG 从不复制到执行目录，不用原图冒充重绘。临时输出不回写候选目录；导入模块本身不绘图。没有打包作者批量 build 脚本或内部任务协调脚本。

## 人工 Pass 的准备契约

`promotion.prepare(root, row, formal_id)` 只返回 `(formal_row, writes, source_notes)`，不写文件、不批准题目。实际 Pass 仍由工作台核对当前内容指纹、独立重绘、逐像素比对、记录用户点击、事务提交和正式题库校验。

- 正式场景采用仓库要求的规范字段；渲染器所需的语义填充、模型构造等额外证据保留在来源说明及带指纹的原生依赖中，不丢失、不伪造空字段。
- 自包含依赖写入 `dataset_generator/mathvision_renderers/`，不覆盖既有正式公共渲染器，不依赖候选目录。
- 正式重绘以正式场景的规范几何字段覆盖原生场景，再恢复仅用于旧入口报告路径的历史身份字段；保留原生语义扩展。正式图片与来源图保持原字节。
- 请使用正式 `dataset.jsonl` 记录的 `script` 复现；不要改用旧 stock 几何工具，因为部分原生语义渲染扩展超出旧工具支持范围。

读取、浏览、运行包校验与独立临时准备都不会产生用户通过记录。

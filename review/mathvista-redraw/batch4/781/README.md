# MathVista 781 · 平面几何

[返回总目录](../../README.md) · [上一题 777](../777/README.md) · [下一题 783](../783/README.md)

状态：**待用户审核（改编题）**。尚未收入正式题库。

## 当前待审核题目

In triangle CDF, K is the centroid and G is the midpoint of CD. Given DG = 9, find CD.

选项：A. 9；B. 12；C. 18；D. 24

当前答案：18

## 原图与重绘

| 原图 | 协议重绘 |
|---|---|
| ![原图](source.jpg) | ![重绘](redrawn.png) |

点击图片可放大。

## 原题记录

来源：MathVista testmini / Geometry3K

原题：In $\triangle CDF$, $K$ is the centroid and $DK=16$. Find $CD$.

原官方答案：18

## 改编说明

- {"field": "given", "original": "DK = 16", "replacement": "DG = 9, with G the midpoint of CD", "rationale": "The original centroid and diagram lengths imply KG=6 and GD=9, making DK=16 impossible. DG=9 is already printed in the diagram and suffices for the requested CD."}
- {"field": "choice D", "original": "18", "replacement": "24", "rationale": "The original choices contained two identical correct answers; the replacement restores a unique option."}



[完整改编记录、解题与独立检查](adapted_question.json)

## 文件与反馈

[冻结场景](scene.json) · [重绘脚本](redraw.py) · [核验报告](redraw_report.json)

[完整来源记录](source_metadata.json)

可在草稿 PR 的 Conversation 留言“MathVista 781：通过 / 需要修改，具体是……”，也可以直接告诉 dot。改编题请明确是否接受改编。点赞或 GitHub 的通用 Approve 不自动代替逐题通过记录。

[来源与许可](../../ATTRIBUTION.md)

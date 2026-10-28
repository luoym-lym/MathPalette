# 重绘的只读核验工具

这些工具不批准、删除或改写题目。结果写入仓库 `.runtime/protocol_redraw/`。
它们可在完整仓库或本轮独立候选包中运行。

```bat
python -B review_candidates/mathvision/validation_tools/independent_geometry.py
python -B review_candidates/mathvision/validation_tools/engine_coverage.py
python -B review_candidates/mathvision/validation_tools/repeat_artifacts.py --workers 3
```

- `independent_geometry.py` 直接从冻结坐标重新计算数值约束，不导入绘图器，不采信报告中的通过标记。不能用这些检查推断来源未明确给出的条件；四条原生语义扩展单独列出。
- `engine_coverage.py` 检查当前输入/图片/绘图器指纹、实际矢量对象清单和样式。被移除的填充和艺术图案等警告仍需对照来源实际查看；机器计数不代替视觉判断。
- `repeat_artifacts.py` 用新的独立进程重放每题，核对输入稳定、PNG 像素及字节和 SVG 字节。可用 `--ids MVI0053 MVI0927` 限定题目。它不拟合视窗，也不覆盖参考图片。

普通库内入口的候选/临时正式目录核验：

```bat
python -B review_candidates/mathvision/validate_package.py --formal --twice --workers 4
```

所有机器检查成功都不表示获得用户 Pass，也不证明每道来源题的答案或隐含条件。

# MathVision attribution

Source dataset: [MathLLMs/MathVision](https://huggingface.co/datasets/MathLLMs/MathVision), test split, frozen revision `2837ddb3f13abaf6b3997c12d80753e5470bd46a`. The [dataset card at this revision](https://huggingface.co/datasets/MathLLMs/MathVision/blob/2837ddb3f13abaf6b3997c12d80753e5470bd46a/README.md) is preserved byte for byte in [dataset_card.md](dataset_card.md).

The retained MathPalette import scope is **521 problems: 351 PlaneGeometry and 170 SolidGeometry**. Source IDs remain available as `source_key="test:<original ID>"`; `source_dataset` remains `MathVision`, and upstream source categories remain distinct from MathPalette's branch assignment. Upstream question text, answers, options, source records and source images are retained as provenance. MathPalette's current stems may have standardized wording and omit image placeholders; redraws and representation changes do not replace the preserved upstream originals. The 175 deleted review candidates and 24 earlier exclusions are outside this retained scope.

## Source and citation

[Official project](https://mathllm.github.io/mathvision/) | [Official repository](https://github.com/mathllm/MATH-V) | [Paper](https://openreview.net/forum?id=QWTCcxMpPA)

Ke Wang, Junting Pan, Weikang Shi, Zimu Lu, Houxing Ren, Aojun Zhou, Mingjie Zhan and Hongsheng Li. *Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset*. NeurIPS Datasets and Benchmarks Track, 2024.

## Upstream license declaration

The pinned dataset card declares **MIT**. The official repository's [LICENSE](https://github.com/mathllm/MATH-V/blob/0a0cf1c230505d5c2a0d017a1baadadfde1a7400/LICENSE), frozen separately at commit `0a0cf1c230505d5c2a0d017a1baadadfde1a7400`, is copied without changes into [MATHVISION_LICENSE.txt](MATHVISION_LICENSE.txt), including its original copyright notice. The dataset revision and repository license commit identify different upstream repositories.

Retain the upstream copyright and permission notice with copies or substantial portions under the MIT terms. This attribution reports the upstream declaration; it does not assert new ownership, establish additional rights in third-party originals, or imply endorsement of MathPalette's changes.

[download_provenance.json](download_provenance.json) records the exact primary-source download URLs, retrieval time, byte counts and SHA256 values. `SHA256SUMS` covers every accompanying file except itself.

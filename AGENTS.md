# MathPalette instructions

Read README.md and DRAWING_PROTOCOL.md before making changes.

- The only formal data directory is MathPalette_Dataset/. It contains 323 normal Collect questions, 1,140 passed Special variants, and 1,463 samples. Exclude uncollected, flagged, and pending-review questions. Keep Collect slots consistent with the Special list.
- Keep original question IDs. Do not restore deleted questions to fill numbering gaps or reintroduce old branches, workbenches, migration archives, or experimental results.
- Each question has one Python class. Its draw methods use drawing.py directly. Keep shared tools small and keep question-specific construction in the question class.
- Preserve approved questions, answers, choices, and mathematical geometry unless the user authorizes changes. Retain original approval and Collect/Pass dates. Do not fabricate review records.
- Use the current drawing code as the PNG reference. Synchronize images, manifests, metadata hashes, and SHA256SUMS after approved changes.
- Keep repository code, documentation, and metadata in English. Do not add Chinese comments, test responses, or historical instruction quotes.
- Keep inference simple: three independent model scripts and at most one small API-key check. Do not add runner frameworks, subprocess workers, test harnesses, or extra management scripts.
- Defaults are DeepSeek max, Qwen xhigh, and MiniMax max via Token Plan, five concurrent samples per model, and a 640-second total request deadline. Never retry a timed-out sample, including across restarts. Other retryable errors allow at most three attempts per input across restarts. Do not set an output token limit. Save the actual reasoning_content and content fields; never substitute the answer for missing reasoning.
- Use only this instruction plus a newline and the original question: Please solve the problem step by step and put your answer in one "\boxed{}". Do not add a system message or question-type-specific prompts.
- Preserve existing tracked .env credentials. Add or update MINIMAX_API_KEY only when explicitly requested by the user. Do not expose credentials or modify Git history.
- Write temporary outputs to .runtime/ and model results to the Git-ignored results/ directory. Keep local results when removing them from Git tracking. Local mocks do not count as real provider validation. Do not call paid models unless the user requests a run.

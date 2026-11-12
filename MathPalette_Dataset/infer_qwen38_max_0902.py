"""Send local MathPalette samples to Qwen3.8-Max-0902 and save reasoning and answers."""
import argparse
import asyncio
import base64
import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv

DATASET = Path(__file__).resolve().parent
load_dotenv(DATASET.parent / ".env")
MODEL = 'qwen3.8-max-0902'
BASE_URL = os.getenv('QWEN_BASE_URL', 'https://maas.qianwenaiapi.com/compatible-mode/v1').rstrip("/")
KEY_NAME = 'QWEN_38_MAX_0902_API_KEY'
TIMEOUT = 640
MAX_ATTEMPTS = 3
CONCURRENCY = 5
PROMPT = r'Please solve the problem step by step and put your answer in one "\boxed{}".'


def make_payload(sample):
    image = base64.b64encode((DATASET / sample["image"]).read_bytes()).decode("ascii")
    return {
        "model": MODEL, "enable_thinking": True, "reasoning_effort": "xhigh", "stream": False,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": PROMPT + "\n" + sample["question"]},
            {"type": "image_url", "image_url": {
                "url": "data:image/png;base64," + image}},
        ]}],
    }


def save(path, result):
    path.write_text(json.dumps(result, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, help="Process only the first N samples")
    parser.add_argument("--output-dir", type=Path,
                        default=DATASET.parent / "results" / 'qwen')
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be positive")
    key = os.getenv(KEY_NAME)
    if not key:
        parser.error("Set " + KEY_NAME + " in the environment or the project .env")
    if args.output_dir.resolve().is_relative_to(DATASET):
        parser.error("Write results outside the formal dataset directory")
    samples = [json.loads(line) for line in (DATASET / "samples.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        pending = iter(samples[:args.limit])
        stop = asyncio.Event()

        async def worker():
            for sample in pending:
                if stop.is_set():
                    return
                path = args.output_dir / (sample["id"] + ".json")
                result = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"id": sample["id"], "attempts": []}
                if result.get("status") == "received" or result.get("retryable") is False:
                    continue
                payload = make_payload(sample)
                while len(result["attempts"]) < MAX_ATTEMPTS:
                    if stop.is_set():
                        return
                    attempt = {"number": len(result["attempts"]) + 1, "status": "started"}
                    result["attempts"].append(attempt)
                    save(path, result)
                    try:
                        async with asyncio.timeout(TIMEOUT):
                            response = await client.post(BASE_URL + "/chat/completions",
                                headers={"Authorization": "Bearer " + key}, json=payload)
                        response.raise_for_status()
                        data = response.json()
                        message = data["choices"][0]["message"]
                        result.update(status="received", reasoning_content=message.get("reasoning_content"),
                                      content=message.get("content"), usage=data.get("usage"),
                                      model=data.get("model"), finish_reason=data["choices"][0].get("finish_reason"))
                        attempt["status"] = "received"
                    except Exception as error:
                        timed_out = isinstance(error, (TimeoutError, httpx.TimeoutException))
                        retryable = not timed_out and (isinstance(error, httpx.RequestError) or (
                            isinstance(error, httpx.HTTPStatusError) and (
                                error.response.status_code in (408, 409, 425, 429) or error.response.status_code >= 500)))
                        result.update(status="error", retryable=retryable)
                        attempt.update(status="error", error=str(error).replace(key, "[REDACTED]"),
                                       error_type=type(error).__name__, timed_out=timed_out)
                    save(path, result)
                    print(sample["id"], result["status"], flush=True)
                    if result["status"] == "received":
                        if not result["reasoning_content"] or not result["content"]:
                            print("Missing reasoning_content or content for " + sample["id"], flush=True)
                            stop.set()
                            return
                        break
                    if not result["retryable"]:
                        if attempt.get("timed_out"):
                            break
                        stop.set()
                        return

        async with asyncio.TaskGroup() as group:
            for _ in range(CONCURRENCY):
                group.create_task(worker())


if __name__ == "__main__":
    asyncio.run(main())

"""Check API authentication with GET /models; do not run model inference."""
import argparse
import importlib
import os

import httpx


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("provider", choices=("deepseek", "qwen", "minimax"))
    args = parser.parse_args()
    module = importlib.import_module({
        "deepseek": "infer_deepseek", "qwen": "infer_qwen38_max_0902",
        "minimax": "infer_minimax",
    }[args.provider])
    key = os.getenv(module.KEY_NAME)
    if not key:
        parser.error("Set " + module.KEY_NAME + " in the environment or the project .env")
    response = httpx.get(module.BASE_URL + "/models",
                         headers={"Authorization": "Bearer " + key}, timeout=15)
    response.raise_for_status()
    print(args.provider + ": authenticated /models request succeeded")


if __name__ == "__main__":
    main()

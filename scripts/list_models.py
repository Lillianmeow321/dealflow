#!/usr/bin/env python3
"""List available models for configured DealFlowBench providers."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from llm_client import load_env_file
from llm_client import DEFAULT_BASE_URLS


ROOT = Path(__file__).resolve().parents[1]
OPENAI_COMPATIBLE = {"deepseek", "moonshot", "doubao", "openrouter"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--provider",
        default="all",
        help="deepseek, moonshot, doubao, gemini, openrouter, or all",
    )
    parser.add_argument("--env-file", default=str(ROOT / ".env"))
    args = parser.parse_args()

    load_env_file(args.env_file)
    providers = ["deepseek", "moonshot", "doubao", "gemini", "openrouter"]
    if args.provider != "all":
        providers = [args.provider.lower()]

    exit_code = 0
    for provider in providers:
        print(f"\n## {provider}")
        try:
            models = list_models(provider)
        except Exception as exc:  # noqa: BLE001
            exit_code = 1
            print(f"ERROR: {exc}", file=sys.stderr)
            continue
        if not models:
            print("(no models returned)")
            continue
        for model in models:
            print(model)
    return exit_code


def list_models(provider: str) -> list[str]:
    if provider in OPENAI_COMPATIBLE:
        return list_openai_compatible(provider)
    if provider == "gemini":
        return list_gemini()
    raise ValueError(f"Unsupported provider: {provider}")


def list_openai_compatible(provider: str) -> list[str]:
    prefix = provider.upper()
    api_key = os.getenv(f"{prefix}_API_KEY")
    base_url = os.getenv(f"{prefix}_BASE_URL") or DEFAULT_BASE_URLS.get(provider)
    if not api_key:
        raise ValueError(f"Missing {prefix}_API_KEY in .env")
    if not base_url:
        raise ValueError(f"Missing {prefix}_BASE_URL in .env")

    raw = get_json(
        base_url.rstrip("/") + "/models",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    data = raw.get("data", raw)
    if isinstance(data, list):
        model_ids = []
        for item in data:
            if isinstance(item, dict):
                model_ids.append(str(item.get("id") or item.get("name") or item))
            else:
                model_ids.append(str(item))
        return sorted(model_ids)
    return [json.dumps(raw, ensure_ascii=False)]


def list_gemini() -> list[str]:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY in .env")
    query = urllib.parse.urlencode({"key": api_key})
    raw = get_json(f"https://generativelanguage.googleapis.com/v1beta/models?{query}", headers={})
    models = raw.get("models", [])
    model_ids = []
    for item in models:
        name = item.get("name", "")
        model_id = name.replace("models/", "")
        methods = item.get("supportedGenerationMethods", [])
        if "generateContent" in methods:
            model_ids.append(model_id)
    return sorted(model_ids)


def get_json(url: str, headers: dict[str, str]) -> dict[str, Any]:
    request = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from {url}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error calling {url}: {exc}") from exc


if __name__ == "__main__":
    raise SystemExit(main())

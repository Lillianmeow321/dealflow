#!/usr/bin/env python3
"""Small provider wrapper for DealFlowBench model runs."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any


DEFAULT_BASE_URLS = {
    "deepseek": "https://api.deepseek.com",
    "moonshot": "https://api.moonshot.cn/v1",
    "doubao": "https://ark.cn-beijing.volces.com/api/v3",
    "openrouter": "https://openrouter.ai/api/v1",
}


@dataclass
class LLMResponse:
    provider: str
    model: str
    text: str
    raw: dict[str, Any]


class LLMClientError(RuntimeError):
    pass


def load_env_file(path: str) -> None:
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


def generate(
    provider: str,
    messages: list[dict[str, str]],
    model: str | None = None,
    temperature: float = 0.2,
    max_tokens: int = 8000,
    timeout: int = 600,
) -> LLMResponse:
    provider_key = provider.lower().strip()
    if provider_key in {"deepseek", "moonshot", "doubao", "openrouter"}:
        return _generate_openai_compatible(
            provider=provider_key,
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
        )
    if provider_key == "gemini":
        return _generate_gemini(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
        )
    raise LLMClientError(f"Unsupported provider: {provider}")


def _generate_openai_compatible(
    provider: str,
    messages: list[dict[str, str]],
    model: str | None,
    temperature: float,
    max_tokens: int,
    timeout: int,
) -> LLMResponse:
    prefix = provider.upper()
    api_key = os.getenv(f"{prefix}_API_KEY")
    base_url = os.getenv(f"{prefix}_BASE_URL") or DEFAULT_BASE_URLS.get(provider)
    resolved_model = model or os.getenv(f"{prefix}_MODEL")

    if not api_key:
        raise LLMClientError(f"Missing {prefix}_API_KEY")
    if not base_url:
        raise LLMClientError(f"Missing {prefix}_BASE_URL")
    if not resolved_model:
        raise LLMClientError(f"Missing model. Set {prefix}_MODEL or pass --model.")

    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": resolved_model,
        "messages": messages,
        "max_tokens": max_tokens,
    }
    if provider == "moonshot" and resolved_model.startswith("kimi-k2."):
        # Kimi K2.6 enables thinking by default. In this lightweight harness we
        # do not consume reasoning_content, so disable thinking to get a normal
        # artifact response through non-streaming Chat Completions.
        thinking_type = os.getenv("MOONSHOT_THINKING", "disabled")
        payload["thinking"] = {"type": thinking_type}
        payload["temperature"] = 1.0 if thinking_type == "enabled" else 0.6
    else:
        payload["temperature"] = temperature
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if provider == "openrouter":
        headers.setdefault("HTTP-Referer", "https://localhost/dealflowbench-mini")
        headers.setdefault("X-Title", "DealFlowBench-mini")

    raw = _post_json(url, payload, headers=headers, timeout=timeout)
    try:
        message = raw["choices"][0]["message"]
        text = message.get("content") or ""
        if not text and message.get("reasoning_content"):
            text = message.get("reasoning_content") or ""
    except (KeyError, IndexError, TypeError) as exc:
        raise LLMClientError(f"Unexpected {provider} response shape: {raw}") from exc
    return LLMResponse(provider=provider, model=resolved_model, text=text, raw=raw)


def _generate_gemini(
    messages: list[dict[str, str]],
    model: str | None,
    temperature: float,
    max_tokens: int,
    timeout: int,
) -> LLMResponse:
    api_key = os.getenv("GEMINI_API_KEY")
    resolved_model = model or os.getenv("GEMINI_MODEL")
    if not api_key:
        raise LLMClientError("Missing GEMINI_API_KEY")
    if not resolved_model:
        raise LLMClientError("Missing model. Set GEMINI_MODEL or pass --model.")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        + resolved_model
        + ":generateContent?key="
        + api_key
    )
    prompt = "\n\n".join(f"{msg['role'].upper()}:\n{msg['content']}" for msg in messages)
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens,
        },
    }
    raw = _post_json(url, payload, headers={"Content-Type": "application/json"}, timeout=timeout)
    try:
        text = raw["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError) as exc:
        raise LLMClientError(f"Unexpected Gemini response shape: {raw}") from exc
    return LLMResponse(provider="gemini", model=resolved_model, text=text, raw=raw)


def _post_json(url: str, payload: dict[str, Any], headers: dict[str, str], timeout: int) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise LLMClientError(f"HTTP {exc.code} from {url}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise LLMClientError(f"Network error calling {url}: {exc}") from exc

#!/usr/bin/env python3
"""Run one model on a DealFlowBench task and save generated artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from llm_client import LLMClientError, generate, load_env_file


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True, help="Task folder name, e.g. T001_homepal_robotics")
    parser.add_argument("--provider", required=True, help="deepseek, moonshot, doubao, gemini, or openrouter")
    parser.add_argument("--model", default=None, help="Optional model override")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--max-tokens", type=int, default=10000)
    parser.add_argument("--timeout", type=int, default=600, help="HTTP read timeout in seconds")
    parser.add_argument("--env-file", default=str(ROOT / ".env"))
    parser.add_argument("--runs-dir", default=str(ROOT / "runs"))
    args = parser.parse_args()

    load_env_file(args.env_file)
    task_dir = ROOT / "tasks" / args.task
    if not task_dir.exists():
        raise SystemExit(f"Task not found: {task_dir}")

    task_prompt = read_text(task_dir / "task_prompt.md")
    data_room_text = build_data_room_text(task_dir / "data_room")
    required_files = infer_required_files(task_prompt)

    system_prompt = (
        "You are an investment associate completing a DealFlowBench task. "
        "Use only the provided data room. Do not use external facts. "
        "Return each required artifact in a separate fenced code block. "
        "Start each artifact with a markdown heading exactly like: "
        "### FILE: filename.ext"
    )
    user_prompt = (
        "# Task Prompt\n\n"
        + task_prompt
        + "\n\n# Data Room\n\n"
        + data_room_text
        + "\n\n# Output Instructions\n\n"
        + "Create the required artifacts. Use this exact format for every file:\n\n"
        + "### FILE: product_kpi_check.csv\n"
        + "```csv\n"
        + "...\n"
        + "```\n\n"
        + "### FILE: investment_memo.md\n"
        + "```markdown\n"
        + "...\n"
        + "```\n\n"
        + "Required files inferred from the task:\n"
        + "\n".join(f"- {name}" for name in required_files)
    )

    response = generate(
        provider=args.provider,
        model=args.model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        timeout=args.timeout,
    )
    if not response.text.strip():
        debug_dir = Path(args.runs_dir) / args.task / "_failed"
        debug_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        debug_path = debug_dir / f"{args.provider}__empty_response__{timestamp}.json"
        debug_path.write_text(json.dumps(response.raw, indent=2, ensure_ascii=False), encoding="utf-8")
        raise SystemExit(f"Model returned empty content. Raw API response saved to {debug_path}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_slug = slugify(response.model)
    run_dir = Path(args.runs_dir) / args.task / f"{response.provider}__{model_slug}__{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)

    (run_dir / "raw_response.md").write_text(response.text, encoding="utf-8")
    (run_dir / "raw_api_response.json").write_text(
        json.dumps(response.raw, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    artifacts = parse_artifacts(response.text)
    for filename, content in artifacts.items():
        safe_name = Path(filename).name
        (run_dir / safe_name).write_text(content.strip() + "\n", encoding="utf-8")

    config = {
        "task": args.task,
        "provider": response.provider,
        "model": response.model,
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "timeout": args.timeout,
        "timestamp": timestamp,
        "required_files": required_files,
        "parsed_artifacts": sorted(artifacts.keys()),
    }
    (run_dir / "run_config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")

    print(f"Saved run to {run_dir}")
    if missing := sorted(set(required_files) - set(artifacts.keys())):
        print("Warning: missing parsed artifacts: " + ", ".join(missing))
    return 0


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def build_data_room_text(data_room_dir: Path) -> str:
    chunks: list[str] = []
    for path in sorted(data_room_dir.iterdir()):
        if not path.is_file():
            continue
        chunks.append(f"## FILE: data_room/{path.name}\n\n```{fence_type(path)}\n{read_text(path)}\n```")
    return "\n\n".join(chunks)


def fence_type(path: Path) -> str:
    if path.suffix == ".csv":
        return "csv"
    if path.suffix == ".json":
        return "json"
    return "markdown"


def infer_required_files(task_prompt: str) -> list[str]:
    matches = re.findall(r"`([^`]+\.(?:csv|md|json|txt))`", task_prompt)
    excluded = {"task_prompt.md"}
    required: list[str] = []
    for match in matches:
        name = Path(match).name
        if name in excluded or name.startswith("data_room/"):
            continue
        if name not in required:
            required.append(name)
    return required


def parse_artifacts(text: str) -> dict[str, str]:
    artifacts: dict[str, str] = {}
    pattern = re.compile(
        r"^### FILE:\s*([^\n]+)\n```[a-zA-Z0-9_-]*\n(.*?)\n```",
        re.MULTILINE | re.DOTALL,
    )
    for filename, content in pattern.findall(text):
        artifacts[Path(filename.strip()).name] = content
    return artifacts


def slugify(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_.-]+", "_", value).strip("_")[:80]


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except LLMClientError as exc:
        print(f"LLM error: {exc}", file=sys.stderr)
        raise SystemExit(2)

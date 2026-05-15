#!/usr/bin/env python3
"""Run one or more providers on a task, evaluate runs, and aggregate results."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from llm_client import load_env_file


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", default="T001_homepal_robotics")
    parser.add_argument("--providers", nargs="+", default=None, help="Providers to run, e.g. deepseek moonshot gemini")
    parser.add_argument("--temperature", type=float, default=None, help="Global temperature override")
    parser.add_argument("--max-tokens", type=int, default=8000)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--env-file", default=str(ROOT / ".env"))
    parser.add_argument("--continue-on-error", action="store_true", default=True)
    args = parser.parse_args()

    load_env_file(args.env_file)
    providers = args.providers or configured_providers()
    if not providers:
        raise SystemExit("No configured providers found in .env")

    failures = []
    for provider in providers:
        print(f"\n## Running {provider} on {args.task}", flush=True)
        cmd = [
            sys.executable,
            str(ROOT / "scripts" / "run_model.py"),
            "--task",
            args.task,
            "--provider",
            provider,
            "--max-tokens",
            str(args.max_tokens),
            "--timeout",
            str(args.timeout),
        ]
        temperature = args.temperature if args.temperature is not None else default_temperature(provider)
        cmd.extend(["--temperature", str(temperature)])
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        print(result.stdout, end="")
        if result.returncode != 0:
            print(result.stderr, end="", file=sys.stderr)
            failures.append((provider, "run_failed"))
            if not args.continue_on_error:
                return result.returncode
            continue

        run_dir = extract_run_dir(result.stdout)
        if not run_dir:
            failures.append((provider, "missing_run_dir"))
            continue
        eval_cmd = [
            sys.executable,
            str(ROOT / "scripts" / "evaluate_outputs.py"),
            "--task",
            args.task,
            "--run",
            run_dir,
        ]
        eval_result = subprocess.run(eval_cmd, cwd=ROOT, capture_output=True, text=True)
        print(eval_result.stdout, end="")
        if eval_result.returncode != 0:
            print(eval_result.stderr, end="", file=sys.stderr)
            failures.append((provider, "eval_failed"))

    print("\n## Aggregating results", flush=True)
    aggregate_cmd = [sys.executable, str(ROOT / "scripts" / "aggregate_results.py")]
    aggregate_result = subprocess.run(aggregate_cmd, cwd=ROOT, capture_output=True, text=True)
    print(aggregate_result.stdout, end="")
    if aggregate_result.returncode != 0:
        print(aggregate_result.stderr, end="", file=sys.stderr)
        return aggregate_result.returncode

    if failures:
        print("\nCompleted with failures:")
        for provider, reason in failures:
            print(f"- {provider}: {reason}")
    return 0


def configured_providers() -> list[str]:
    providers = []
    for provider in ["deepseek", "moonshot", "gemini", "doubao", "openrouter"]:
        prefix = provider.upper()
        if os.getenv(f"{prefix}_API_KEY") and os.getenv(f"{prefix}_MODEL"):
            providers.append(provider)
    return providers


def default_temperature(provider: str) -> float:
    if provider == "moonshot":
        return 0.6
    return 0.2


def extract_run_dir(stdout: str) -> str | None:
    for line in stdout.splitlines():
        if line.startswith("Saved run to "):
            return line.removeprefix("Saved run to ").strip()
    return None


if __name__ == "__main__":
    raise SystemExit(main())

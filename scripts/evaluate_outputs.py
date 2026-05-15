#!/usr/bin/env python3
"""Lightweight evaluator for DealFlowBench model outputs."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True, help="Task folder name, e.g. T001_homepal_robotics")
    parser.add_argument("--run", required=True, help="Run output directory")
    parser.add_argument("--write-report", action="store_true", default=True)
    args = parser.parse_args()

    task_dir = ROOT / "tasks" / args.task
    run_dir = Path(args.run).resolve()
    if not task_dir.exists():
        raise SystemExit(f"Task not found: {task_dir}")
    if not run_dir.exists():
        raise SystemExit(f"Run directory not found: {run_dir}")

    task_prompt = read_text(task_dir / "task_prompt.md")
    required_files = infer_required_files(task_prompt)
    combined_output = collect_output_text(run_dir)
    calc_checks = load_json(task_dir / "expected" / "calculation_checks.json")
    golden = load_json(task_dir / "expected" / "golden_facts.json")

    artifact_report = score_artifacts(run_dir, required_files)
    calculation_report = score_calculations(combined_output, calc_checks.get("checks", []))
    golden_report = score_golden_facts(combined_output, golden.get("golden_facts", []))
    risk_report = score_required_items(combined_output, golden.get("must_identify_risks", []), "risks")
    positive_report = score_required_items(combined_output, golden.get("expected_positive_signals", []), "positive_signals")
    failure_tags = infer_failure_tags(task_dir, artifact_report, calculation_report, risk_report)

    total_score = round(
        artifact_report["score"] * 0.20
        + calculation_report["score"] * 0.30
        + golden_report["score"] * 0.25
        + risk_report["score"] * 0.20
        + positive_report["score"] * 0.05,
        2,
    )

    report = {
        "task": args.task,
        "run_dir": str(run_dir),
        "score": total_score,
        "score_components": {
            "artifacts": artifact_report,
            "calculations": calculation_report,
            "golden_facts": golden_report,
            "required_risks": risk_report,
            "positive_signals": positive_report,
        },
        "failure_tags": failure_tags,
        "note": (
            "This is a lightweight automated evaluator. It checks artifact presence, "
            "numeric/string evidence, and rough golden fact coverage. Investment judgment "
            "quality should still be reviewed with the task rubric or an LLM/human judge."
        ),
    }

    report_path = run_dir / "score_report.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"score": total_score, "report": str(report_path)}, indent=2))
    return 0


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read_text(path))


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


def collect_output_text(run_dir: Path) -> str:
    chunks: list[str] = []
    for path in sorted(run_dir.iterdir()):
        if path.name == "score_report.json" or not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".csv", ".txt", ".json"}:
            continue
        chunks.append(f"\n\n### {path.name}\n\n{read_text(path)}")
    return "\n".join(chunks)


def score_artifacts(run_dir: Path, required_files: list[str]) -> dict[str, Any]:
    present = [name for name in required_files if (run_dir / name).exists()]
    missing = [name for name in required_files if name not in present]
    score = 100.0 if not required_files else round(100 * len(present) / len(required_files), 2)
    return {
        "score": score,
        "present": present,
        "missing": missing,
    }


def score_calculations(output: str, checks: list[dict[str, Any]]) -> dict[str, Any]:
    normalized = normalize(output)
    results = []
    hits = 0
    for check in checks:
        expected_strings = expected_strings_for_check(check)
        matched = [value for value in expected_strings if normalize(value) in normalized]
        ok = bool(matched)
        hits += int(ok)
        results.append(
            {
                "metric": check.get("metric"),
                "expected_display": check.get("expected_display"),
                "matched": ok,
                "matched_evidence": matched[:5],
                "status": check.get("expected_status"),
            }
        )
    score = 100.0 if not checks else round(100 * hits / len(checks), 2)
    return {
        "score": score,
        "matched": hits,
        "total": len(checks),
        "details": results,
    }


def expected_strings_for_check(check: dict[str, Any]) -> list[str]:
    values: list[str] = []
    display = check.get("expected_display")
    if display:
        values.append(str(display))
    expected_value = check.get("expected_value")
    values.extend(render_expected_value(expected_value))
    return dedupe(values)


def render_expected_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, dict):
        values: list[str] = []
        for item in value.values():
            values.extend(render_expected_value(item))
        return values
    if isinstance(value, (int, float)):
        values = [str(value)]
        if isinstance(value, float):
            values.extend(
                [
                    f"{value:.1%}",
                    f"{value:.2%}",
                    f"{value * 100:.1f}%",
                    f"{value * 100:.2f}%",
                    f"{value:.1f}",
                    f"{value:.2f}",
                ]
            )
        return values
    return [str(value)]


def score_golden_facts(output: str, facts: list[dict[str, Any]]) -> dict[str, Any]:
    normalized = normalize(output)
    details = []
    hits = 0
    for fact in facts:
        keywords = keywords_from_text(fact.get("fact", ""))
        matched_keywords = [kw for kw in keywords if kw in normalized]
        required = min(3, max(1, len(keywords) // 3))
        ok = len(matched_keywords) >= required
        hits += int(ok)
        details.append(
            {
                "id": fact.get("id"),
                "category": fact.get("category"),
                "importance": fact.get("importance"),
                "matched": ok,
                "matched_keywords": matched_keywords[:8],
                "fact": fact.get("fact"),
            }
        )
    score = 100.0 if not facts else round(100 * hits / len(facts), 2)
    return {
        "score": score,
        "matched": hits,
        "total": len(facts),
        "details": details,
    }


def score_required_items(output: str, items: list[str], label: str) -> dict[str, Any]:
    normalized = normalize(output)
    details = []
    hits = 0
    for item in items:
        keywords = keywords_from_text(item)
        matched_keywords = [kw for kw in keywords if kw in normalized]
        required = min(2, max(1, len(keywords) // 3))
        ok = len(matched_keywords) >= required
        hits += int(ok)
        details.append({"item": item, "matched": ok, "matched_keywords": matched_keywords[:8]})
    score = 100.0 if not items else round(100 * hits / len(items), 2)
    return {
        "label": label,
        "score": score,
        "matched": hits,
        "total": len(items),
        "details": details,
    }


def infer_failure_tags(
    task_dir: Path,
    artifact_report: dict[str, Any],
    calculation_report: dict[str, Any],
    risk_report: dict[str, Any],
) -> list[str]:
    rubric = read_text(task_dir / "expected" / "scoring_rubric.md")
    available_tags = re.findall(r"`([a-z0-9_]+)`:", rubric)
    tags: list[str] = []
    if artifact_report["missing"] and "artifact_incomplete" in available_tags:
        tags.append("artifact_incomplete")
    if calculation_report["score"] < 60:
        tags.extend(tag for tag in available_tags if any(key in tag for key in ["calculation", "margin", "retention", "monetization", "inventory", "asp"]))
    if risk_report["score"] < 60:
        tags.extend(tag for tag in available_tags if tag.endswith("_miss") or tag.endswith("_bias"))
    return dedupe(tags)


def keywords_from_text(text: str) -> list[str]:
    normalized = normalize(text)
    tokens = re.findall(r"[a-z0-9]+(?:\.[0-9]+)?%?|\$[0-9.]+m?", normalized)
    stop = {
        "the",
        "and",
        "or",
        "of",
        "to",
        "in",
        "is",
        "are",
        "a",
        "an",
        "with",
        "from",
        "about",
        "by",
        "for",
        "as",
        "but",
        "than",
        "into",
        "not",
        "yet",
    }
    keywords = [token for token in tokens if token not in stop and len(token) > 2]
    return dedupe(keywords)


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower().replace(",", "")).strip()


def dedupe(values: list[str]) -> list[str]:
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


if __name__ == "__main__":
    raise SystemExit(main())


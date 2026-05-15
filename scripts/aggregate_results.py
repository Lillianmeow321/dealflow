#!/usr/bin/env python3
"""Aggregate DealFlowBench score reports into CSV and Markdown matrices."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs-dir", default=str(ROOT / "runs"))
    parser.add_argument("--out-dir", default=str(ROOT / "results"))
    parser.add_argument("--include-samples", action="store_true", help="Include sample/manual smoke-test runs")
    parser.add_argument("--all-runs", action="store_true", help="Include all runs instead of latest run per task/provider/model")
    args = parser.parse_args()

    runs_dir = Path(args.runs_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    reports = load_reports(runs_dir, include_samples=args.include_samples)
    if not args.all_runs:
        reports = latest_reports(reports)
    if not reports:
        raise SystemExit(f"No score_report.json files found under {runs_dir}")

    matrix_path = out_dir / "eval_matrix.csv"
    failure_path = out_dir / "failure_matrix.md"
    write_eval_matrix(matrix_path, reports)
    write_failure_matrix(failure_path, reports)

    print(f"Wrote {matrix_path}")
    print(f"Wrote {failure_path}")
    return 0


def load_reports(runs_dir: Path, include_samples: bool) -> list[dict[str, Any]]:
    reports = []
    for path in sorted(runs_dir.glob("*/*/score_report.json")):
        if not include_samples and "sample" in path.parts[-2]:
            continue
        if not include_samples and path.parts[-2].startswith("_failed"):
            continue
        report = json.loads(path.read_text(encoding="utf-8"))
        run_dir = Path(report["run_dir"])
        run_config_path = run_dir / "run_config.json"
        run_config = {}
        if run_config_path.exists():
            run_config = json.loads(run_config_path.read_text(encoding="utf-8"))
        report["_score_report_path"] = str(path)
        report["_provider"] = run_config.get("provider") or infer_provider(run_dir.name)
        report["_model"] = run_config.get("model") or infer_model(run_dir.name)
        report["_timestamp"] = run_config.get("timestamp") or infer_timestamp(run_dir.name)
        if not include_samples and components_are_empty(report):
            continue
        reports.append(report)
    return reports


def components_are_empty(report: dict[str, Any]) -> bool:
    components = report.get("score_components", {})
    artifacts = components.get("artifacts", {})
    return report.get("score") == 0 and not artifacts.get("present")


def latest_reports(reports: list[dict[str, Any]]) -> list[dict[str, Any]]:
    latest: dict[tuple[str, str, str], dict[str, Any]] = {}
    for report in reports:
        key = (report["task"], report["_provider"], report["_model"])
        if key not in latest or report.get("_timestamp", "") > latest[key].get("_timestamp", ""):
            latest[key] = report
    return sorted(latest.values(), key=lambda item: (item["task"], item["_provider"], item["_model"]))


def write_eval_matrix(path: Path, reports: list[dict[str, Any]]) -> None:
    fields = [
        "task",
        "provider",
        "model",
        "total_score",
        "artifact_score",
        "calculation_score",
        "golden_fact_score",
        "risk_score",
        "positive_signal_score",
        "failure_tags",
        "diagnosis",
        "score_report",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for report in reports:
            components = report["score_components"]
            writer.writerow(
                {
                    "task": report["task"],
                    "provider": report["_provider"],
                    "model": report["_model"],
                    "total_score": report["score"],
                    "artifact_score": components["artifacts"]["score"],
                    "calculation_score": components["calculations"]["score"],
                    "golden_fact_score": components["golden_facts"]["score"],
                    "risk_score": components["required_risks"]["score"],
                    "positive_signal_score": components["positive_signals"]["score"],
                    "failure_tags": "; ".join(report.get("failure_tags", [])),
                    "diagnosis": diagnose(report),
                    "score_report": report["_score_report_path"],
                }
            )


def write_failure_matrix(path: Path, reports: list[dict[str, Any]]) -> None:
    counter: Counter[str] = Counter()
    by_tag: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for report in reports:
        for tag in report.get("failure_tags", []):
            counter[tag] += 1
            by_tag[tag].append(report)

    lines = ["# Failure Matrix", ""]
    lines.append("## Run Summary")
    lines.append("")
    lines.append("| Task | Provider | Model | Total | Calculations | Golden Facts | Risks | Failure Tags | Diagnosis |")
    lines.append("|---|---|---|---:|---:|---:|---:|---|---|")
    for report in reports:
        components = report["score_components"]
        lines.append(
            "| {task} | {provider} | {model} | {total:.2f} | {calc:.2f} | {golden:.2f} | {risk:.2f} | {tags} | {diag} |".format(
                task=report["task"],
                provider=report["_provider"],
                model=report["_model"],
                total=report["score"],
                calc=components["calculations"]["score"],
                golden=components["golden_facts"]["score"],
                risk=components["required_risks"]["score"],
                tags=", ".join(report.get("failure_tags", [])) or "-",
                diag=diagnose(report),
            )
        )

    lines.extend(["", "## Failure Mode Counts", ""])
    if counter:
        lines.append("| Failure Mode | Count | Example Diagnosis |")
        lines.append("|---|---:|---|")
        for tag, count in counter.most_common():
            lines.append(f"| `{tag}` | {count} | {diagnose(by_tag[tag][0])} |")
    else:
        lines.append("No failure tags recorded.")

    lines.extend(["", "## Iteration Notes", ""])
    lines.append("- Low calculation scores usually mean the model captured the narrative but did not fully populate the required KPI table.")
    lines.append("- High golden fact and risk scores with lower calculation scores suggest the task is diagnosing spreadsheet discipline rather than investment synthesis.")
    lines.append("- Repeated failure tags should feed back into either task wording, artifact schema, or deterministic checks.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def diagnose(report: dict[str, Any]) -> str:
    components = report["score_components"]
    missing = components["artifacts"]["missing"]
    calc = components["calculations"]["score"]
    golden = components["golden_facts"]["score"]
    risk = components["required_risks"]["score"]
    tags = set(report.get("failure_tags", []))
    if missing:
        return "Incomplete artifact delivery; model did not follow the workflow output contract."
    if calc < 65 and golden >= 80 and risk >= 80:
        return "Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations."
    if golden < 70:
        return "Missed key data-room facts; likely grounding or file-reading weakness."
    if risk < 70:
        return "Missed required diligence risks; investment judgment may be too shallow."
    if tags:
        return "Mostly complete, with targeted failure modes: " + ", ".join(sorted(tags)) + "."
    return "No major automated failure pattern; review qualitative memo quality with rubric."


def infer_provider(run_name: str) -> str:
    return run_name.split("__", 1)[0] if "__" in run_name else "manual"


def infer_model(run_name: str) -> str:
    parts = run_name.split("__")
    return parts[1] if len(parts) > 1 else run_name


def infer_timestamp(run_name: str) -> str:
    parts = run_name.split("__")
    return parts[2] if len(parts) > 2 else ""


if __name__ == "__main__":
    raise SystemExit(main())

# DealFlowBench-mini

DealFlowBench-mini is a cross-application benchmark prototype for PE/VC investment agents. It evaluates whether an agent can operate like a junior investment professional inside a realistic workspace: reading a multi-file data room, checking operating metrics, identifying contradictions and risks, and producing team-ready investment deliverables.

The benchmark is not designed as a finance knowledge quiz. It is designed around real investment workflows where information is incomplete, materials are heterogeneous, and the final answer must be actionable for a deal team.

## Benchmark Objective

DealFlowBench-mini evaluates agents on the following long-horizon workflow:

```text
ambiguous partner request
-> navigate multi-file workspace
-> extract and verify facts
-> calculate investment metrics
-> identify contradictions and risks
-> form investment judgment
-> produce team-ready deliverables
```

## Target Role

Target role: PE/VC investment associate or investment manager.

Representative workflows:

| Workflow | Real user need | Agent capabilities |
|---|---|---|
| Deal screening | Decide whether a new opportunity is worth deeper diligence | Multi-file reading, commercial judgment, risk identification |
| KPI review | Check whether management's headline metrics are reliable | Spreadsheet reasoning, calculation, anomaly detection |
| Thesis update | Revise an investment view based on new evidence | Temporal reasoning, contradiction detection, view revision |
| IC preparation | Create materials that can enter a team workflow | Long-horizon planning, artifact creation, format following |

## Task Design Matrix

| Task ID | Company | Investment type | Skill type | Difficulty | Primary failure modes |
|---|---|---|---|---|---|
| T001 | HomePal Robotics | VC / Series A | AI product + hardware PMF | Medium | Demo bias, retention miss, margin miscalculation, manufacturing risk miss |
| T002 | StoryForge AI | VC / Seed-A | AI-native content workflow + monetization | Medium-High | Output-volume bias, weak monetization miss, platform dependency miss, IP risk miss |
| T003 | VoltBridge Mobility | PE / Growth | Export growth + operating diligence | High | Revenue-growth bias, inventory miss, channel concentration miss, warranty/regulatory risk miss |

## Benchmark Scope

This mini version contains three synthetic-but-realistic data rooms. A full benchmark could scale to 20-50 task packages across industries, stages, and task types.

The three seed tasks are:

| Task ID | Scenario | Core evaluation focus |
|---|---|---|
| T001 | AI-powered home companion robot | Whether impressive AI demos translate into durable household demand and scalable hardware economics |
| T002 | AI-native comic drama content studio | Whether AI production efficiency creates durable content and monetization advantage |
| T003 | China-based e-bike exporter to Europe and Southeast Asia | Whether headline export growth is high quality after channel, inventory, warranty, and compliance risks |

## Task Environment

Each task is an offline synthetic data room. This avoids live web volatility, training data contamination, and confidential data exposure while preserving realistic PE/VC workflows.

Standard package structure:

```text
T001_homepal_robotics/
  task_prompt.md
  data_room/
    partner_email.md
    pitch_deck_summary.md
    pilot_usage_metrics.csv
    feature_usage_breakdown.csv
    commercialization_metrics.csv
    bom_and_margin_table.csv
    user_interview_notes.md
    manufacturing_plan.md
    competitor_snapshot.md
    memo_template.md
  expected/
    golden_facts.json
    calculation_checks.json
    scoring_rubric.md
```

## Evaluation Rubric

Total score: 100 points.

| Dimension | Weight | Evaluation method |
|---|---:|---|
| Task Completion | 15 | Required artifacts are produced and structurally valid |
| Factual Grounding | 15 | Claims are grounded in the data room without hallucinated facts |
| Financial / KPI Accuracy | 15 | Calculations, formulas, and anomaly detection are correct |
| Investment Judgment | 20 | The recommendation identifies the key opportunity, risks, and investability |
| Cross-Application Workflow | 15 | The agent correctly handles documents, tables, templates, and email-like outputs |
| Deliverable Quality | 10 | Memo, risk log, and email are professional and usable |
| Traceability | 10 | Sources, assumptions, calculations, and uncertainty are clear |

## Evaluation Harness

The intended evaluation pipeline is:

```text
Task package creation
-> Agent execution in workspace
-> Artifact collection
-> Deterministic grading
-> Golden fact coverage check
-> LLM rubric grading
-> Human spot check
-> Failure taxonomy
-> Score report
```

## Failure Taxonomy

DealFlowBench-mini records failure modes in addition to numeric scores.

| Failure type | Example |
|---|---|
| File navigation failure | The agent misses a critical data room file |
| Calculation failure | The agent miscalculates gross margin, retention, inventory days, or payback |
| Grounding failure | The agent invents facts not present in the data room |
| Contradiction miss | The agent misses a conflict between management claims and raw data |
| Over-trust management | The agent repeats management's story without challenging assumptions |
| Weak investment judgment | The memo summarizes facts but gives no actionable recommendation |
| Artifact failure | Required files are missing or unusable |
| Thesis inertia | The agent fails to revise a view when new evidence contradicts the old thesis |

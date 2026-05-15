# DealFlowBench-mini Data Room Design Playbook

This playbook captures the design principles learned from iterating T001 HomePal Robotics. Use it when creating T002 StoryForge AI and T003 VoltBridge Mobility so each task feels like a real PE/VC investment workspace rather than a synthetic case prompt.

## Core Principle

A good DealFlowBench data room should create a realistic tension between:

```text
management storytelling
vs.
underlying operating data
vs.
qualitative evidence
vs.
investment decision
```

The agent should not be able to solve the task by summarizing a pitch deck. It should need to reconcile multiple materials, calculate metrics, detect selective framing, and produce an actionable investment recommendation.

## Required Evidence Layers

Each data room should include at least five evidence layers.

| Layer | Purpose | Example file |
|---|---|---|
| Partner request | Creates ambiguous real-world task context | `partner_email.md` |
| Management narrative | Shows the company's optimistic framing | `pitch_deck_summary.md` or `management_presentation.md` |
| Raw operating data | Lets the agent verify or challenge claims | `.csv` files |
| Commercial / monetization data | Tests whether usage or growth converts to economic value | `commercialization_metrics.csv`, `revenue_by_channel.csv` |
| Qualitative evidence | Adds customer, creator, distributor, or user nuance | `interview_notes.md`, `audience_comments.md` |
| Execution / risk memo | Adds operational, legal, regulatory, or supply-chain constraints | `manufacturing_plan.md`, `ip_memo.md`, `regulatory_memo.md` |
| Market / competitor context | Tests differentiation and substitute risk | `competitor_snapshot.md` |
| Output template | Makes the task feel like a real workflow artifact | `memo_template.md`, `ic_note_template.md` |

## The Three-Round Iteration Check

Before freezing a data room, run these three checks.

### Round 1: Does It Match A Real Investment Workflow?

Ask:

- Would a PE/VC associate plausibly receive these files before a partner sync?
- Is the task more than a single Q&A or summarization exercise?
- Does the agent need to produce real artifacts such as a memo, KPI check, risk log, or email?
- Does the task require judgment under uncertainty rather than a single obvious answer?
- Is the company stage consistent with the data? For example, an early Series A company may not have full P&L history, but should have preorder, pilot, CAC, deposit, or paid trial data.

If the answer is no, add or revise files until the task resembles a real workspace.

### Round 2: Does The Data Room Contain Real Tension?

Ask:

- What does management want the investor to believe?
- Which raw data point weakens or complicates that story?
- Are there at least 5-8 golden issues the agent should discover?
- Are there both positive and negative signals, so the recommendation is not trivial?
- Is there at least one metric-definition or cohort-mix trap?
- Is there a difference between headline growth and growth quality?

Good benchmark tasks should reward agents that challenge the narrative without becoming reflexively negative.

### Round 3: Is It Verifiable?

Ask:

- Which metrics can be automatically recalculated?
- Which facts can be stored in `golden_facts.json`?
- Which risks should be mandatory in a strong answer?
- Which outputs can be checked structurally?
- Which parts require LLM judge or human calibration?
- What failure modes should this task diagnose?

If a data room has no deterministic checks, it is too subjective. If it has no judgment checks, it is too mechanical.

## Data Room Quality Checklist

Use this checklist before considering T002 or T003 complete.

### Realism

- The file set resembles an actual investor data room.
- The company stage matches the available data.
- The partner request is specific but not over-instructed.
- The company narrative is optimistic but plausible.
- The materials include both structured data and qualitative notes.

### Cross-Application / Workflow Fit

- The agent must read documents.
- The agent must reason over tables.
- The agent must create multiple artifacts.
- The agent must follow a template.
- The final output could enter a real deal-team workflow.

### Investment Substance

- There is a clear investment question.
- The task tests investability, not just business comprehension.
- There are positive signals worth recognizing.
- There are material risks worth escalating.
- The recommendation can be Proceed / Hold / Reject, or an equivalent task-specific decision.

### Data Tension

- Management claims are not all false, but some are selectively framed.
- Raw data forces cohort, channel, region, or segment analysis.
- At least one metric is true under one basis but misleading under another.
- Qualitative notes explain why the numbers look the way they do.
- The agent must distinguish volume from quality.

### Evaluability

- There are numeric checks with expected values and tolerances.
- There are golden facts with source files.
- There are required risks and positive signals.
- There is a scoring rubric.
- There is a failure taxonomy.

## Reusable File Schema

Use this baseline structure for T002 and T003.

```text
T00X_company_name/
  task_prompt.md
  data_room/
    partner_email.md
    management_narrative.md
    income_statement.csv
    adjusted_ebitda_bridge.csv
    balance_sheet.csv
    cash_flow_statement.csv
    working_capital_schedule.csv
    ar_aging.csv
    operating_metrics.csv
    commercialization_or_revenue_metrics.csv
    qualitative_notes.md
    execution_or_risk_memo.md
    competitor_or_market_snapshot.md
    output_template.md
  expected/
    golden_facts.json
    calculation_checks.json
    scoring_rubric.md
```

Add extra files only when they create meaningful evaluation surface.

## T002 StoryForge AI Guidance

T002 should evaluate whether an AI-native comic drama studio has a durable business advantage or only short-term content/platform arbitrage.

Recommended evidence layers:

| File | Purpose |
|---|---|
| `partner_email.md` | Partner asks whether AI production efficiency translates into investable content economics |
| `company_overview.md` | Management narrative around AI workflow, output velocity, and hit creation |
| `production_workflow.md` | Before/after AI production process, staffing, cycle time |
| `episode_performance.csv` | Episode-level views, completion, continuation, paid conversion, revenue |
| `cost_comparison.csv` | Cost per episode and cycle time before vs after AI |
| `platform_distribution_report.md` | Platform concentration, algorithm dependency, traffic sources |
| `copyright_ip_memo.md` | Training data, asset provenance, likeness/IP risk |
| `audience_comments.md` | Qualitative reactions about story quality, repetition, AI feel |
| `memo_template.md` | Required investment memo format |

T002 should include these tensions:

- AI lowers cost and increases output, but hit rate may be inconsistent.
- High views may not convert into paid users.
- One platform may drive most traffic.
- AI-generated assets may create IP or copyright risk.
- Audience comments may reveal repetitive stories or weak emotional attachment.

Expected failure modes:

- `output_volume_bias`: Mistakes more content for better business quality.
- `monetization_miss`: Ignores low paid conversion or weak revenue per viewer.
- `platform_dependency_miss`: Misses traffic concentration.
- `ip_risk_miss`: Treats AI content as clean without checking asset provenance.
- `quality_signal_miss`: Ignores comments about story repetition or low emotional connection.

## T003 VoltBridge Mobility Guidance

T003 should evaluate whether an e-bike exporter is a high-quality PE/growth asset or a business with low-quality export growth.

Recommended evidence layers:

| File | Purpose |
|---|---|
| `partner_email.md` | Partner asks whether to proceed, request revised plan, or pause |
| `management_presentation.md` | Management narrative around export growth and regional expansion |
| `regional_sales.csv` | Revenue, units, ASP, region growth, channel mix |
| `gross_margin_by_channel.csv` | Margin by Europe distributor, Amazon, DTC, Southeast Asia retail |
| `inventory_aging.csv` | Inventory days, >180 day aging, SKU/region risk |
| `distributor_contracts_summary.md` | Concentration, exclusivity, payment terms |
| `warranty_and_returns.csv` | Warranty cost, return rate, battery/motor issue trends |
| `regulatory_tariff_memo.md` | EU compliance, CE/EN15194, battery transport, tariff exposure |
| `ic_note_template.md` | Required IC note format |

T003 should include these tensions:

- Revenue grows, but mix may shift toward lower-margin channels.
- Europe may have high revenue but aging inventory and distributor concentration.
- Southeast Asia may grow fast but with lower ASP and margin.
- Warranty/return cost may be rising.
- Compliance and tariff requirements may create hidden cost or shipment risk.
- Cash conversion may worsen as inventory builds.

Expected failure modes:

- `headline_growth_bias`: Focuses on revenue growth while missing quality issues.
- `margin_mix_miss`: Misses channel or region margin deterioration.
- `inventory_miss`: Fails to flag aged inventory or cash conversion pressure.
- `concentration_miss`: Ignores distributor dependency.
- `warranty_miss`: Misses rising return or battery warranty cost.
- `regulatory_miss`: Underweights EU compliance and tariff risk.

## Final Design Standard

Each task should be able to answer this sentence:

> A strong agent should discover that the company is not simply good or bad; it has a plausible investment wedge, but the data room contains specific evidence that changes the quality, timing, or conditions of the investment recommendation.

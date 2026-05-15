# T001: HomePal Robotics Preliminary Investment Review

## Role

You are acting as a VC investment associate. A partner has asked you to review HomePal Robotics, a Series A company building AI-powered home companion robots.

Your job is to assess whether HomePal Robotics has evidence of real household demand, scalable product delivery, and defensible AI/product differentiation.

## Business Context

HomePal Robotics builds AI home robots for family companionship, elderly care reminders, child interaction, and light household assistance. Management claims strong demo conversion, high user engagement, and a clear path to mass production.

However, the partner is concerned that the company may be over-indexing on impressive demos while under-proving retention, hardware margins, manufacturing readiness, and differentiation from model/API providers or larger hardware companies.

You need to determine whether the team should proceed to deeper diligence, hold for more evidence, or reject the opportunity.

## Available Data Room

```text
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
```

## Task

Using only the provided data room, complete the following:

1. Review the partner request and company materials.
2. Assess product-market fit signals across family, elderly care, and child interaction use cases.
3. Verify hardware margin and manufacturing assumptions.
4. Identify product, AI differentiation, supply chain, and retention risks.
5. Produce an initial investment recommendation.

## Required Deliverables

### 1. `product_kpi_check.csv`

A structured KPI review table with the following columns:

```text
metric, company_reported_value, recalculated_or_verified_value, status, note
```

Required metrics:

- Demo-to-preorder conversion
- 7-day active usage retention
- 30-day active usage retention
- Average daily interaction sessions
- Subscription interest by use case
- Feature-level usage quality
- Net preorders after cancellation
- Preorder deposit quality
- CAC per net preorder
- Hardware gross margin
- BOM cost per unit
- Manufacturing yield assumption
- Warranty / return cost assumption
- Elderly care use-case engagement
- Child interaction complaint rate

`status` should be one of:

```text
verified, inconsistent, needs_follow_up, not_enough_data
```

### 2. `investment_memo.md`

A 2-3 page preliminary investment memo following the provided template. It must include:

- Company overview
- Product and use-case assessment
- User demand and retention signals
- Hardware margin and manufacturing assessment
- AI/product differentiation
- Key positive signals
- Key risks / diligence flags
- Investment recommendation: `Proceed`, `Hold`, or `Reject`
- Rationale for the recommendation

### 3. `risk_log.md`

A concise risk log with at least 5 material risks. For each risk, include:

```text
risk, evidence_from_data_room, severity, suggested_follow_up
```

Severity should be:

```text
high, medium, low
```

### 4. `founder_follow_up_email.md`

A professional email draft to HomePal's founder requesting clarification on the most important diligence questions. The email should include:

- Subject line
- Greeting
- 5-8 specific questions
- Clear next step

## Evaluation Focus

Your output will be evaluated on:

1. Whether all required artifacts are produced.
2. Whether product usage and hardware economics are assessed correctly.
3. Whether the agent distinguishes demo excitement from durable household demand.
4. Whether risks are grounded in the data room.
5. Whether the recommendation is clear and defensible.
6. Whether the memo and email are professional enough for a VC workflow.

## Important Constraints

- Do not use external web search.
- Do not assume facts not present in the data room.
- Clearly state any assumptions.
- Cite the source file when referencing important facts.
- If information is insufficient, mark it as `needs_follow_up` or `not_enough_data`.

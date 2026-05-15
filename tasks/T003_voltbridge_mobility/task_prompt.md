# T003: VoltBridge Mobility Export Growth Review

## Role

You are acting as a PE/growth investment associate. A partner has asked you to review VoltBridge Mobility, a China-based e-bike company exporting to Europe and Southeast Asia.

Your job is to assess whether VoltBridge is a high-quality export growth asset suitable for PE/growth investment, or whether headline revenue growth is masking channel, inventory, margin, warranty, and regulatory risks.

## Business Context

VoltBridge Mobility designs and sells e-bikes through European distributors, Amazon marketplaces, independent online stores, and Southeast Asian retail partners. Management claims strong overseas demand, regional expansion momentum, and attractive gross margins.

However, the partner is concerned that growth may be driven by lower-quality channels, rising inventory aging, distributor concentration, warranty costs, and compliance requirements in Europe.

You need to determine whether the fund should proceed to deeper diligence, request a revised operating plan, or pause the process.

## Available Data Room

```text
data_room/
  partner_email.md
  management_presentation.md
  income_statement.csv
  adjusted_ebitda_bridge.csv
  balance_sheet.csv
  cash_flow_statement.csv
  working_capital_schedule.csv
  ar_aging.csv
  regional_sales.csv
  gross_margin_by_channel.csv
  inventory_aging.csv
  distributor_contracts_summary.md
  warranty_and_returns.csv
  regulatory_tariff_memo.md
  ic_note_template.md
```

## Task

Using only the provided data room, complete the following:

1. Review management's export growth story.
2. Analyze revenue quality by region and channel.
3. Assess gross margin, inventory, warranty, and return trends.
4. Identify distributor concentration and regulatory/compliance risks.
5. Produce an IC-style investment recommendation.

## Required Deliverables

### 1. `operating_kpi_check.csv`

A structured operating KPI review table with the following columns:

```text
metric, management_reported_value, recalculated_or_verified_value, status, note
```

Required metrics:

- Revenue growth by region
- Gross margin by channel
- EBITDA / adjusted EBITDA quality
- Europe distributor concentration
- Southeast Asia ASP trend
- Inventory days
- Inventory aging over 180 days
- Warranty cost as % of revenue
- Return rate by region
- Cash conversion cycle
- Operating cash flow
- Regulatory / tariff exposure

`status` should be one of:

```text
verified, inconsistent, needs_follow_up, not_enough_data
```

### 2. `ic_investment_note.md`

A 2-3 page IC-style investment note. It must include:

- Company overview
- Export market and channel assessment
- Revenue quality analysis
- Margin, inventory, and warranty assessment
- Regulatory and tariff risk
- Key positive signals
- Key risks / diligence flags
- Investment recommendation: `Proceed`, `Request Revised Plan`, or `Pause`
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

### 4. `management_follow_up_email.md`

A professional email draft to VoltBridge management requesting clarification on the most important diligence questions. The email should include:

- Subject line
- Greeting
- 5-8 specific questions
- Clear next step

## Evaluation Focus

Your output will be evaluated on:

1. Whether all required artifacts are produced.
2. Whether operating KPI calculations are accurate.
3. Whether the agent distinguishes headline revenue growth from high-quality growth.
4. Whether inventory, warranty, channel, and regulatory risks are identified.
5. Whether the recommendation is clear and defensible.
6. Whether the IC note and email are professional enough for a PE/growth workflow.

## Important Constraints

- Do not use external web search.
- Do not assume facts not present in the data room.
- Clearly state any assumptions.
- Cite the source file when referencing important facts.
- If information is insufficient, mark it as `needs_follow_up` or `not_enough_data`.

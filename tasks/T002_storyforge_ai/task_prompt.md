# T002: StoryForge AI Content Studio Review

## Role

You are acting as a VC investment associate. A partner has asked you to review StoryForge AI, an AI-native content studio producing short-form comic dramas and AI-generated manga series.

Your job is to assess whether StoryForge AI's production workflow creates a durable business advantage, or whether the company is mainly benefiting from short-term platform arbitrage.

## Business Context

StoryForge AI uses generative AI tools to produce serialized comic dramas for TikTok, YouTube Shorts, Webtoon-style platforms, and its own app. Management claims that AI has reduced production costs by more than 60%, increased output velocity, and enabled rapid testing of new IP concepts.

However, the partner is concerned about inconsistent hit rates, weak paid conversion, platform dependency, copyright/IP risk, and whether AI-generated content quality can sustain user retention.

You need to determine whether the fund should proceed to deeper diligence, hold for more evidence, or reject the opportunity.

## Available Data Room

```text
data_room/
  partner_email.md
  company_overview.md
  production_workflow.md
  episode_performance.csv
  cost_comparison.csv
  platform_distribution_report.md
  copyright_ip_memo.md
  audience_comments.md
  memo_template.md
```

## Task

Using only the provided data room, complete the following:

1. Review StoryForge's AI content production workflow.
2. Quantify production cost and cycle-time improvement.
3. Analyze episode-level performance, retention, and paid conversion.
4. Identify platform, content quality, monetization, and copyright/IP risks.
5. Produce an initial investment recommendation.

## Required Deliverables

### 1. `content_kpi_check.csv`

A structured KPI review table with the following columns:

```text
metric, company_reported_value, recalculated_or_verified_value, status, note
```

Required metrics:

- Cost per episode before AI
- Cost per episode after AI
- Production cycle time before AI
- Production cycle time after AI
- Output volume increase
- Episode completion rate
- Series continuation rate
- Paid conversion rate
- Revenue per completed viewer
- Platform concentration
- Copyright/IP risk status

`status` should be one of:

```text
verified, inconsistent, needs_follow_up, not_enough_data
```

### 2. `investment_memo.md`

A 2-3 page preliminary investment memo following the provided template. It must include:

- Company overview
- AI workflow and production advantage
- Content performance and monetization quality
- Platform distribution assessment
- Copyright/IP risk assessment
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

A professional email draft to StoryForge's founder requesting clarification on the most important diligence questions. The email should include:

- Subject line
- Greeting
- 5-8 specific questions
- Clear next step

## Evaluation Focus

Your output will be evaluated on:

1. Whether all required artifacts are produced.
2. Whether AI-driven cost and cycle-time improvements are calculated correctly.
3. Whether the agent distinguishes output volume from durable content quality.
4. Whether monetization, retention, platform, and IP risks are identified.
5. Whether the recommendation is clear and defensible.
6. Whether the memo and email are professional enough for a VC workflow.

## Important Constraints

- Do not use external web search.
- Do not assume facts not present in the data room.
- Clearly state any assumptions.
- Cite the source file when referencing important facts.
- If information is insufficient, mark it as `needs_follow_up` or `not_enough_data`.


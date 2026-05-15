### FILE: product_kpi_check.csv
```csv
metric,company_reported_value,recalculated_or_verified_value,status,note
Demo-to-preorder conversion,34%,32.8% (269/820),verified,Calculated from pilot_usage_metrics.csv cohorts
7-day active usage retention,72%,85.9% (average of elderly cohorts: 92.1%, 88.6%),inconsistent,Company reported 72% vs. 85-90% in elderly care cohorts
30-day active usage retention,72%,59.7% (average of elderly cohorts: 81.6%, 77.1%),inconsistent,Company reported 72% vs. 77-82% in elderly care cohorts
Average daily interaction sessions,6.8,6.8 (child interaction cohorts: 7.1, 6.6),verified,Pitch deck summary and child interaction pilot data
Subscription interest by use case,61% (elderly care),61% (partner referrals),verified,From commercialization_metrics.csv channel data
Feature-level usage quality,High,87.6% (medication reminder),verified,From feature_usage_breakdown.csv
Net preorders after cancellation,272,272,verified,From commercialization_metrics.csv
Preorder deposit quality,$300,$300,verified,From commercialization_metrics.csv "avg_deposit_per_gross_preorder"
CAC per net preorder,$185,$185,verified,From commercialization_metrics.csv
Hardware gross margin,39.3%,20.5% (pilot),inconsistent,From bom_and_margin_table.csv
BOM cost per unit,$788,$1033 (pilot),inconsistent,From bom_and_margin_table.csv
Manufacturing yield assumption,95%,93% (pilot final yield),needs_follow_up,From manufacturing_plan.md (pilot yield 93% vs. 95% target)
Warranty / return cost assumption,3% of retail price,8% of retail price (pilot),inconsistent,From bom_and_margin_table.csv
Elderly care use-case engagement,High,80%+ (30-day retention),verified,From user_interview_notes.md and pilot_usage_metrics.csv
Child interaction complaint rate,Low,23/10,6200 events (0.29%),needs_follow_up,From feature_usage_breakdown.csv and user_interview_notes.md
```

### FILE: investment_memo.md
```markdown
# Preliminary Investment Memo: HomePal Robotics

## Recommendation: Hold

## Company Overview
HomePal Robotics is developing AI-powered home companion robots (HomePal One) targeting three use cases: elderly care reminders, child interaction, and family assistant tasks. The company has completed 243 pilot placements across five cities, secured 338 gross preorders ($101,400 in deposits), and is seeking a $18M Series A to scale production. Management claims 34% demo-to-preorder conversion, 72% 30-day retention, and 39.3% gross margin at scale.

## Product and Use-Case Assessment
### Product Overview
HomePal One combines third-party LLM APIs with proprietary household memory, mobility, and sensor systems. The robot offers medication reminders, hydration alerts, bedtime stories, homework help, and calendar management.

### Use-Case Analysis
- **Elderly Care**: Strongest evidence of durable demand. 7-day retention for elderly cohorts averages 88-92% (pilot_usage_metrics.csv), with 80%+ 30-day retention. Interviews show 8/10 elderly households find medication reminders "most useful," and 69% opt for subscription trials in partner channels (commercialization_metrics.csv).
  
- **Child Interaction**: High initial excitement but rapid novelty decay. 30-day retention drops to 40% (CI_SH_01) and 39% (CI_HZ_02), with 33% of households expressing concerns about repetitive content and open-ended answer quality (user_interview_notes.md).

- **Family Assistant**: Low differentiation from smart speakers. 2/5 households prefer smart speakers for calendar/reminder tasks, and 25% usage rate (pilot_usage_metrics.csv) is below elderly care (80%+).

## User Demand and Retention Signals
- **Demo-to-Preorder Conversion**: 34% overall (pilot data: 32.8%), indicating strong offline validation.
- **Retention**: Elderly care shows 85-90% 7-day retention and 77-82% 30-day retention, while child interaction and family assistant cohorts lag (40-45% 30-day retention).
- **Engagement**: Child interaction has highest daily sessions (6.8-7.1), but elderly care has consistent, low-friction usage (5.8-6.2 sessions/day).

## Hardware Margin and Manufacturing Assessment
- **BOM and Margin**: Pilot BOM cost ($1,033) exceeds management's $788 target, resulting in 20.5% gross margin (pilot) vs. 39.3% (management). Warranty costs are 8% of retail price (pilot) vs. 3% assumed (bom_and_margin_table.csv).
  
- **Manufacturing Risks**: Pilot yield is 93% (final after rework), below management's 95% target. Key delays: UN38.3 battery certification pending, enclosure tooling incomplete, and contract manufacturer lacks mobile robot experience (manufacturing_plan.md).

## AI and Product Differentiation
- **Strengths**: Proprietary household memory layer and mobility (differentiates from static smart speakers).
- **Weaknesses**: Relies on third-party LLM APIs (no unique model differentiation). Elderly care workflows lack integration with healthcare systems, limiting defensibility (competitor_snapshot.md).

## Key Positive Signals
1. **Elderly Care Traction**: 80%+ 30-day retention, 61% subscription opt-in in partner channels, and 87.6% success rate for medication reminders (feature_usage_breakdown.csv).
2. **Demo Validation**: 34% conversion and $101K in preorder deposits ($300 avg deposit) demonstrate market interest.
3. **Pilot Experience**: 24 paid households (pilot_usage_metrics.csv) with strong repeat usage in core care cohorts.

## Key Risks / Diligence Flags
1. **Hardware Economics**: 20.5% gross margin (pilot) and 8% warranty costs make profitability unviable without manufacturing improvements.
2. **Manufacturing Execution**: Pending certifications, tooling delays, and yield gaps raise production timeline risks.
3. **Child Interaction Viability**: 30-day retention <40% and 33% household complaint rate (user_interview_notes.md) indicate limited long-term demand.
4. **AI Dependency**: Third-party LLM APIs may face cost increases or feature limitations, with no proprietary model differentiation.

## Conclusion
HomePal Robotics shows promise in elderly care, but critical risks in hardware margin, manufacturing execution, and child interaction viability require further validation. **Hold** for additional diligence on margin optimization, manufacturing timelines, and AI differentiation.
```

### FILE: risk_log.md
```markdown
| Risk | Evidence from Data Room | Severity | Suggested Follow-Up |
|------|-------------------------|----------|---------------------|
| **Hardware Margin Shortfall** | Pilot BOM cost ($1,033) vs. management’s $788, 20.5% gross margin (pilot) vs. 39.3% (claimed). 8% warranty reserve (pilot) vs. 3% (claimed). | High | Verify BOM cost reduction plan and warranty cost mitigation strategies. |
| **Manufacturing Execution Delays** | Pilot final yield 93% (vs. 95% target), pending UN38.3 battery certification, incomplete enclosure tooling, and lack of mobile robot manufacturing experience. | High | Audit contract manufacturer’s robot production experience and certification timelines. |
| **Child Interaction Retention** | 30-day retention <40% (CI cohorts), 33% household complaints (open-ended answers, content repetition), 22% subscription opt-in (commercialization_metrics.csv). | High | Validate long-term engagement strategies and parental control improvements. |
| **Family Assistant Substitution** | 2/5 households prefer smart speakers for calendar/reminder tasks, 25% usage rate (pilot). | Medium | Assess pricing strategy and unique value proposition for family use cases. |
| **AI Differentiation Weakness** | Relies on third-party LLM APIs; no proprietary model differentiation. Competitors (Astro, ElliQ) offer similar functionality. | Medium | Review proprietary household memory layer development and data ownership strategy. |
```

### FILE: founder_follow_up_email.md
```markdown
### FILE: founder_follow_up_email.md
```markdown
Subject: HomePal Robotics: Key Diligence Questions for Series A Review

Dear [Founder Name],

Following our preliminary review of HomePal Robotics, we have several critical questions to clarify before advancing to deeper diligence:

1. **Elderly Care Retention**: With 80%+ 30-day retention in elderly cohorts, what specific long-term engagement strategies are planned to maintain this? What healthcare system integrations (e.g., hospital partnerships) exist to reduce false reminders?

2. **Hardware Margin Optimization**: Pilot gross margin is 20.5% (vs. 39.3% claimed). How will you achieve $788 BOM cost target? What supplier negotiations or design revisions are planned to reduce BOM costs?

3. **Manufacturing Yield**: Pilot final yield is 93% (vs. 95% target). What contingency plans exist if yield does not improve? When will UN38.3 battery certification and enclosure tooling be finalized?

4. **Child Interaction Strategy**: Given 33% household complaints about content quality, what parental control improvements are scheduled? Are you developing proprietary educational content to reduce third-party API dependency?

5. **AI Differentiation**: With third-party LLM APIs, what unique value does HomePal’s proprietary layer provide? How will you protect household data and ensure data ownership?

6. **Subscription Economics**: 61% opt-in for elderly care subscriptions, but 34% cancellation rate (commercialization_metrics.csv). What is the projected LTV:CAC ratio for subscription models?

7. **Family Assistant Viability**: Smart speakers dominate 50% of households. How will you price and package HomePal One to justify $1,299 vs. $100 smart speakers?

Please provide data/updates on these points by [Date]. We look forward to addressing these gaps to validate HomePal’s commercial potential.

Best regards,
[Your Name]
```
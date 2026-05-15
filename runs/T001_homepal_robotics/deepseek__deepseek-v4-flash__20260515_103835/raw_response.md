### FILE: product_kpi_check.csv
```csv
metric,company_reported_value,recalculated_or_verified_value,status,note
Demo-to-preorder conversion,34%,32.6% (weighted average of offline demo cohorts),verified,Management's claim is close but not exact; varies by cohort (19%–41%). Based on pilot_usage_metrics.csv.
7-day active usage retention,Not explicitly stated (management refers to "core care cohorts" 30-day),73.8% (overall),needs_follow_up,Overall 7-day retention from pilot_usage_metrics.csv = 166/225 = 73.8%. Management's 30-day claim may use a subset.
30-day active usage retention,"72% (core care cohorts)",50.7% (overall),inconsistent,Overall 30-day retention = 114/225 = 50.7%. Elderly care cohorts achieve 77.3% (58/75), but child and family segments drag down overall. Management's claim only applies to selected cohorts.
Average daily interaction sessions,6.8,5.61 (overall weighted average),inconsistent,Computed from pilot_usage_metrics.csv: weighted average by activated households = 5.61. Even elderly+child average is 6.47, still below 6.8.
Subscription interest by use case,Not claimed (preorder deposit only),Elderly care 64–69%, Child 19–22%, Family 12–14%,verified,From pilot_usage_metrics.csv subscription_interest_rate. Elderly care shows strongest interest.
Feature-level usage quality,Not claimed,Medication reminder success 87.6%; Open-ended chat success 54.6% with high complaints,needs_follow_up,From feature_usage_breakdown.csv. Child interaction features have low success rates and high safety/complaint tickets.
Net preorders after cancellation,272 (implied from 338 gross – 66 cancelled),272,verified,From commercialization_metrics.csv total row.
Preorder deposit quality,$300 per gross preorder ($101,400 / 338),$300 per gross preorder,verified,From commercialization_metrics.csv. However, cancellation rate is 19.5%, and deposit refund policy not disclosed – risk.
CAC per net preorder,$185,$180 (weighted average),verified,From commercialization_metrics.csv. Weighted average computed as $48930/272 = $180, close to $185.
Hardware gross margin,39.3% (launch case),20.5% (current pilot cost),inconsistent,From bom_and_margin_table.csv. Management assumes volume discounts and reduced warranty reserve to reach 39.3%.
BOM cost per unit,$788 (launch case),$1033 (current pilot cost),inconsistent,Current pilot cost is 31% higher than launch case target.
Manufacturing yield assumption,"95% first-pass yield by month 4",86% first-pass yield in pilot,needs_follow_up,From manufacturing_plan.md. Pilot yield of 86% is below initial mass production assumption of 88%.
Warranty / return cost assumption,3% of retail price ($39),8% of retail price ($104 based on pilot experience),inconsistent,From bom_and_margin_table.csv. Pilot warranty experience suggests significantly higher cost.
Elderly care use-case engagement,High (qualitative),88% 7-day retention, 77% 30-day retention, 64–69% subscription interest,verified,From pilot_usage_metrics.csv and user_interview_notes.md. Strongest evidence of durable demand.
Child interaction complaint rate,Not disclosed,40% of households filed at least one complaint; 22% return intent,needs_follow_up,From pilot_usage_metrics.csv and feature_usage_breakdown.csv. High complaint and safety ticket rates (8 safety tickets).
```

### FILE: investment_memo.md
```markdown
# Preliminary Investment Memo

## Recommendation

**Hold**

One-sentence rationale: HomePal Robotics shows promising elderly care engagement but has significant risks in overall retention, hardware margins, manufacturing readiness, and child interaction safety; more evidence is needed before proceeding to full diligence.

## Company Overview

HomePal Robotics is a Series A company developing an AI-powered home companion robot (HomePal One) targeting three use cases: elderly care reminders, child interaction, and family assistant tasks. The company has completed 243 structured household pilots across five cities and claims 338 gross preorders with $101,400 in deposits. Management is raising an $18M Series A to fund tooling, certification, hiring, and launch inventory for 25,000 units in the first year.

## Product and Use-Case Assessment

**Elderly care reminders** (medication, hydration, family check-ins) show the strongest evidence of durable demand. Pilot cohorts achieve 77.3% 30-day active retention and 64–69% subscription interest. User interviews confirm consistent daily use and willingness to pay for reliable family notification features. This is the most differentiated and defensible use case.

**Child interaction** (bedtime stories, open-ended chat) generates high initial excitement (7–8 sessions per active day in first week) but suffers from rapid novelty decay (30-day retention drops to 20% across child cohorts). Complaint rates are high: 40% of child-interaction households filed at least one complaint, and 22% indicated return intent. Open-ended chat has a 54.6% success rate and 8 safety tickets. Parents express concerns about inappropriate answers and excessive screen-like interaction. This use case is currently problematic and may require significant product improvements.

**Family assistant** (calendar, shopping list) shows the weakest engagement. 30-day retention is only 20–25%, and subscription interest is below 15%. Users compare the robot unfavorably to smart speakers and mobile apps. This use case is unlikely to drive purchase decisions on its own.

## User Demand and Retention

- **Demo-to-preorder conversion**: 32.6% weighted average (close to management’s 34%), but varies from 19% (family assistant) to 41% (elderly care). The overall rate masks strong segment differences.
- **Net preorders after cancellation**: 272 (cancellation rate 19.5%). High cancellations in parenting KOL (33%) and online ad (34%) channels suggest low purchase intent for these segments.
- **Overall 30-day active retention is 50.7%**, far below management’s claimed 72% (which applies only to selected “core care cohorts” – likely elderly care). Elderly care achieves 77.3%, but child and family segments drag down the average. This indicates that novelty-driven excitement declines sharply for non-elderly use cases.
- **Subscription interest varies widely** from 12% (family assistant) to 69% (elderly care, partner-referral channel). The majority of users are not yet paying for the subscription.

**Bottom line**: Elderly care shows early, durable household behavior. Child interaction and family assistant do not pass the novelty test.

## Hardware Margin and Manufacturing

- **Current pilot BOM**: $1,033 per unit (20.5% gross margin at $1,299 retail). Management targets $788 BOM (39.3% margin) at volume, but this requires significant cost reductions (processor, sensors, motors, enclosure) and lower warranty reserves.
- **Warranty assumption**: Management models 3% of retail price ($39), while pilot experience suggests ~8% ($104). This alone adds $65 per unit to cost.
- **Manufacturing yield**: Pilot first-pass yield is 86% (final 93% after rework). Management assumes 88% in month 1 ramping to 95% by month 4. Given motor calibration (5.5%), camera alignment (3.2%), and battery housing (2.7%) defects, the ramp is optimistic.
- **Open manufacturing items**: Enclosure tooling not finalized, battery certification pending (UN38.3), drop test and long-duration motor reliability not completed. Contract manufacturer has no prior mobile home robot experience.

**Bottom line**: The hardware margin story depends on aggressive cost reductions and yield improvements that are not yet validated. Current economics are unattractive and launch timing is at risk.

## AI and Product Differentiation

HomePal’s AI stack relies on third-party LLM APIs for conversation, with proprietary layers for household memory, routine orchestration, and personality tuning. The strongest differentiation is in elderly care, where the physical, mobile presence and family notification workflow create a more personal experience than stationary smart speakers or tablets. However:

- Large competitors (Amazon Astro, Samsung Ballie) and specialist products (ElliQ) could replicate or surpass this.
- In child interaction and family assistant, smart speakers and tablets are lower-cost substitutes with more mature content libraries.
- If third-party model providers improve agent memory, HomePal’s software advantage may compress.
- Child interaction safety and open-ended answer quality are significant risks.

**Bottom line**: Differentiation is real but narrow (elderly care) and not yet defensible from larger hardware or model providers.

## Key Positive Signals

1. **Elderly care engagement is strong**: 77.3% 30-day retention, 64–69% subscription interest, 88% 7-day retention. (pilot_usage_metrics.csv, user_interview_notes.md)
2. **Demo-to-preorder conversion is solid** (32.6%) and higher in elderly care (40.7%). (pilot_usage_metrics.csv)
3. **Preorder deposits total $101,400** (272 net preorders at $300 average deposit). This shows some early financial commitment. (commercialization_metrics.csv)
4. **Medication reminder feature has high success rate** (87.6%) and low complaint tickets. (feature_usage_breakdown.csv)
5. **User interviews confirm elderly care value**: “My mother responds to the robot more consistently than to phone alarms.” (user_interview_notes.md)

## Key Risks and Diligence Flags

1. **Overall 30-day retention is 50.7%, not 72%** – Management’s cherry-picked metric conceals poor child and family retention. (pilot_usage_metrics.csv)
2. **Hardware margin is 20.5% at current cost, not 39.3%** – Management’s launch case relies on unrealistic cost reductions and warranty assumptions. (bom_and_margin_table.csv)
3. **Child interaction safety and quality issues** – 8 safety tickets, 23 complaint tickets, 22% return intent. Open-ended chat success rate only 54.6%. (feature_usage_breakdown.csv, pilot_usage_metrics.csv)
4. **Manufacturing plan is risky** – Unproven contract manufacturer, uncertified battery, incomplete tooling, optimistic yield ramp. (manufacturing_plan.md)
5. **Competitive differentiation is narrow** – Smart speakers and tablets are cheaper substitutes for child and family uses. Large hardware companies could enter elderly care. (competitor_snapshot.md)
6. **High cancellation rate (19.5%)** in some channels suggests weak purchase intent outside elderly care. (commercialization_metrics.csv)
7. **Recurring revenue not yet validated** – Only 58 households paid for premium features; subscription interest drops sharply outside elderly care. (pilot_usage_metrics.csv)

## Follow-Up Questions

1. What is the exact 30-day retention for each segment (elderly care, child interaction, family assistant) using the same definition as management's "core care cohorts"?
2. Can you provide a detailed bridge from the current $1,033 BOM to the target $788 BOM, with supplier commitments or letters of intent?
3. What is the warranty/return rate in the pilot, and what is the actual cost per returned unit (including refurbishment or replacement)?
4. How do you plan to address child interaction safety (inappropriate answers, excessive screen-like interaction) before launch?
5. What are the specific milestones and contingency plans for battery certification, enclosure tooling, and motor reliability testing?
6. What is the current retention and subscription conversion for households that have had the robot for more than 60 days?
7. How do you plan to differentiate from smart speakers and tablets for general family assistant tasks?

## Rationale for Hold

HomePal Robotics has a real product-market fit signal in elderly care, which could anchor the business. However, the company overstates its overall performance by cherry-picking its best segment. The hardware margin, manufacturing readiness, and child interaction risks are severe enough to require further validation. Proceeding to full diligence now would waste resources; rejecting would ignore a potentially viable elderly care wedge. A **Hold** recommendation allows us to request specific evidence (e.g., segment-level retention, BOM commitments, child interaction safety plan, longer-term retention data) before making a final decision.
```

### FILE: risk_log.md
```markdown
# Risk Log

| Risk | Evidence from Data Room | Severity | Suggested Follow-Up |
|------|-------------------------|----------|---------------------|
| Inflated retention metrics | Management claims 72% 30-day retention for "core care cohorts"; overall retention from pilot data is 50.7%. Elderly care is 77.3%, but child (22%) and family (20%) are much lower. (pilot_usage_metrics.csv, pitch_deck_summary.md) | High | Request segment-level retention for all cohorts using consistent definition. Clarify which cohorts are considered "core care." |
| Hardware margin not achievable | Current BOM $1,033 (20.5% margin). Management target BOM $788 (39.3% margin) assumes volume discounts, lower warranty reserve (3% vs 8% pilot), and yield improvements not yet proven. (bom_and_margin_table.csv) | High | Request supplier letters of intent for volume pricing, detailed cost reduction plan with timelines, and warranty cost breakdown from pilot. |
| Child interaction safety and quality | 8 safety tickets, 23 complaint tickets, 22% return intent in child cohorts. Open-ended chat success rate 54.6%. (feature_usage_breakdown.csv, pilot_usage_metrics.csv) | High | Request detailed plan for content moderation, safety guardrails, and age-appropriate interaction modes before launch. |
| Manufacturing readiness | Pilot first-pass yield 86%; motor calibration drift (5.5%), camera alignment (3.2%), battery housing (2.7%). Enclosure tooling not finalized, battery certification pending, contract manufacturer inexperienced with mobile robots. (manufacturing_plan.md) | High | Request certification timeline, tooling completion milestones, yield improvement plan with contract manufacturer, and backup manufacturing options. |
| Competitive substitution risk | Smart speakers and tablets are low-cost substitutes for child and family assistant use cases. Amazon Astro, Samsung Ballie, and ElliQ are relevant competitors. (competitor_snapshot.md) | Medium | Request competitive analysis, user switching data, and differentiation strategy for each use case. |
| Recurring revenue unproven | Only 58 of 243 pilot households paid for premium features. Subscription interest drops to 12-14% for family assistant. (pilot_usage_metrics.csv) | Medium | Request current subscription revenue, conversion funnel, and churn data for paid pilot households. |
| Preorder deposit quality and cancellation risk | 19.5% overall cancellation rate; 33% for parenting KOL, 34% for online ads. Deposit refund policy unknown. (commercialization_metrics.csv) | Medium | Request refund policy, deposit conversion rate to paid orders, and reasons for cancellation. |
| Reliance on third-party AI models | AI stack uses third-party LLM APIs for open-ended conversation. Proprietary layer is early. (pitch_deck_summary.md, competitor_snapshot.md) | Medium | Request details on model provider contracts, ability to switch providers, and roadmap for proprietary model capability. |
```

### FILE: founder_follow_up_email.md
```markdown
**Subject:** Follow-up Questions on HomePal Robotics – Preliminary Review

Dear [Founder Name],

Thank you for the opportunity to review HomePal Robotics. We are impressed by the early traction in elderly care and the thoughtful product design. After initial analysis of the data room, we would like to clarify a few points before proceeding further.

Specifically:

1. **Segment-level retention**: Could you provide 7-day and 30-day active usage retention for each of the three use cases (elderly care, child interaction, family assistant) separately? We see a 72% claim for "core care cohorts" but would like to understand retention across all segments.

2. **BOM cost bridge**: What specific supplier commitments or quotes support the planned reduction from the current $1,033 BOM to the target $788 BOM? Are there any letters of intent or volume discounts already secured?

3. **Warranty and return costs**: In the pilot, warranty reserve appears to be ~8% of retail price, while the launch case assumes 3%. Could you share actual warranty/return cost per unit from the pilot, including refurbishment and logistics?

4. **Child interaction safety and quality**: Given 8 safety tickets, 23 complaint tickets, and 22% return intent in child cohorts, what specific product changes or content moderation plans are in place before launch?

5. **Manufacturing milestones**: Can you provide a detailed timeline with contingencies for battery certification (UN38.3), final enclosure tooling, and long-duration motor reliability testing? What is the backup plan if battery certification is delayed beyond August 2026?

6. **Longer-term retention**: What is the retention and subscription conversion for households that have had the robot for more than 60 days? We want to understand behavior beyond the initial month.

7. **Competitive differentiation**: How do you plan to defend against smart speaker and tablet substitutes for the family assistant and child interaction use cases? Do you see elderly care as the primary wedge, and if so, what is the go-to-market plan for that segment?

We would be happy to schedule a call to discuss these points at your earliest convenience. Please let us know a time that works.

Best regards,

[Your Name]
Investment Associate
[Firm Name]
```
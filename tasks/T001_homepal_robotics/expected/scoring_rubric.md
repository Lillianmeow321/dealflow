# T001 Scoring Rubric

Total score: 100 points.

## 1. Task Completion - 15 points

- 4 points: Creates `product_kpi_check.csv` with required columns.
- 4 points: Creates `investment_memo.md` with all required sections.
- 3 points: Creates `risk_log.md` with at least 5 material risks.
- 2 points: Creates `founder_follow_up_email.md` with subject, greeting, questions, and next step.
- 2 points: Uses the required status and severity labels.

## 2. Factual Grounding - 15 points

- 5 points: Cites or clearly references the correct source files for major claims.
- 4 points: Does not introduce unsupported external facts.
- 3 points: Correctly distinguishes management claims from recalculated raw data.
- 3 points: Handles insufficient data with `needs_follow_up` or `not_enough_data` instead of inventing answers.

## 3. Product / KPI Accuracy - 15 points

- 3 points: Correctly recalculates demo-to-preorder conversion at about 32.8%.
- 3 points: Correctly identifies the 30-day retention basis issue: 72% applies to elderly/core care cohorts, while total pilot-basis 30-day retention is about 46.9%.
- 2 points: Correctly identifies elderly care as the strongest use case, including retention, subscription interest, and reminder success evidence.
- 2 points: Correctly identifies child interaction weakness, including lower day-30 activity, complaint tickets, and safety tickets.
- 3 points: Correctly compares management launch margin with current pilot margin.
- 2 points: Correctly identifies preorder/channel quality issues or warranty reserve mismatch.

## 4. Hardware and Manufacturing Assessment - 10 points

- 3 points: Flags the aggressive yield ramp from 86% current first-pass yield to 95% by month 4.
- 2 points: Flags unfinished tooling, battery certification, drop testing, or motor reliability testing.
- 2 points: Recognizes launch timing risk if certification or tooling slips.
- 3 points: Connects manufacturing and warranty issues to margin, working capital, or launch risk.

## 5. Investment Judgment - 20 points

- 5 points: Provides a clear `Proceed`, `Hold`, or `Reject` recommendation.
- 5 points: Appropriately balances the promising elderly care wedge against unresolved retention, margin, manufacturing, and differentiation risks.
- 4 points: Avoids over-trusting the pitch deck's headline metrics.
- 3 points: Identifies what evidence would be required to upgrade the opportunity.
- 3 points: Produces a conclusion useful to a VC partner, not just a summary.

Strong answers are expected to recommend `Hold` unless they make an unusually well-supported case for another answer. A `Proceed` answer should lose points if it does not clearly condition the recommendation on resolving retention, margin, manufacturing, and AI differentiation concerns.

## 6. Deliverable Quality - 15 points

- 5 points: Memo is structured, concise, and professional.
- 3 points: Risk log prioritizes material risks rather than listing generic concerns.
- 3 points: Follow-up email asks specific, answerable diligence questions.
- 2 points: Writing is appropriate for an investment workflow.
- 2 points: Output is internally consistent across artifacts.

## 7. Traceability and Assumptions - 10 points

- 4 points: Clearly cites source files for major facts.
- 3 points: Shows calculation logic or assumptions for derived metrics.
- 2 points: Separates observed data, management assumptions, and interpretation.
- 1 point: Notes uncertainty where the data room is insufficient.

## Expected Failure Modes

Track the following failure tags where applicable:

- `demo_bias`: Overweights demo-to-preorder conversion and ignores retention decay.
- `retention_miss`: Fails to identify the 30-day retention discrepancy.
- `cohort_mix_miss`: Fails to distinguish elderly care performance from total pilot performance.
- `feature_quality_miss`: Mistakes high interaction/event volume for durable demand.
- `commercialization_miss`: Fails to distinguish gross preorders from net demand after cancellations.
- `channel_quality_miss`: Fails to identify elderly referrals as higher-quality than KOL or online ads.
- `margin_miscalculation`: Accepts management gross margin without checking pilot cost.
- `warranty_miss`: Fails to identify warranty reserve mismatch.
- `manufacturing_risk_miss`: Fails to flag yield, tooling, certification, or reliability risks.
- `child_safety_miss`: Fails to identify child interaction complaints and guardrail concerns.
- `differentiation_overclaim`: Overstates proprietary AI differentiation despite third-party model reliance.
- `artifact_incomplete`: Fails to produce one or more required deliverables.

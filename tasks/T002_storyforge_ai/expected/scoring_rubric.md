# T002 Scoring Rubric

Total score: 100 points.

## 1. Task Completion - 15 points

- 4 points: Creates `content_kpi_check.csv` with required columns.
- 4 points: Creates `investment_memo.md` with all required sections.
- 3 points: Creates `risk_log.md` with at least 5 material risks.
- 2 points: Creates `founder_follow_up_email.md` with subject, greeting, questions, and next step.
- 2 points: Uses the required status and severity labels.

## 2. Factual Grounding - 15 points

- 5 points: Cites or clearly references the correct source files for major claims.
- 4 points: Does not introduce unsupported external facts.
- 3 points: Correctly distinguishes management claims from recalculated episode data.
- 3 points: Handles insufficient data with `needs_follow_up` or `not_enough_data`.

## 3. Content / KPI Accuracy - 20 points

- 3 points: Correctly recalculates cost per episode reduction at about 64.0%.
- 3 points: Correctly recalculates production cycle reduction at about 67.9%.
- 2 points: Correctly identifies monthly output increased about 4.1x.
- 3 points: Correctly verifies aggregate completion rate around 49.0%.
- 3 points: Correctly identifies paid conversion among engaged viewers around 9.3%, below the 11% management claim.
- 2 points: Correctly calculates low paid conversion among completed viewers around 1.5%.
- 2 points: Correctly calculates paid unlock revenue per completed viewer around $0.027.
- 2 points: Correctly identifies concentration in top two series.

## 4. Platform, IP, and Quality Risk Assessment - 15 points

- 4 points: Flags TikTok concentration and algorithm dependency.
- 3 points: Flags owned app traction as promising but still too small.
- 3 points: Flags asset provenance, character similarity, and clearance risks.
- 3 points: Connects audience comments to story quality, continuity, and retention risk.
- 2 points: Identifies that workflow speed creates additional QA/editorial burden.

## 5. Investment Judgment - 20 points

- 5 points: Provides a clear `Proceed`, `Hold`, or `Reject` recommendation.
- 5 points: Appropriately balances real production efficiency against unresolved monetization, hit repeatability, platform, and IP risks.
- 4 points: Avoids mistaking output volume for durable business quality.
- 3 points: Identifies what evidence would be required to upgrade the opportunity.
- 3 points: Produces a conclusion useful to a VC partner, not just a summary.

Strong answers are expected to recommend `Hold` unless they make an unusually well-supported case for another answer. A `Proceed` answer should lose points if it does not condition the recommendation on repeatable paid conversion, owned distribution, and IP controls.

## 6. Deliverable Quality - 10 points

- 4 points: Memo is structured, concise, and professional.
- 2 points: Risk log prioritizes material risks rather than generic concerns.
- 2 points: Follow-up email asks specific, answerable diligence questions.
- 2 points: Output is internally consistent across artifacts.

## 7. Traceability and Assumptions - 5 points

- 2 points: Clearly cites source files for major facts.
- 2 points: Shows calculation logic or assumptions for derived metrics.
- 1 point: Notes uncertainty where the data room is insufficient.

## Expected Failure Modes

Track the following failure tags where applicable:

- `output_volume_bias`: Mistakes more content for better business quality.
- `monetization_miss`: Ignores low paid conversion or weak revenue per completed viewer.
- `platform_dependency_miss`: Misses TikTok concentration or algorithm risk.
- `ip_risk_miss`: Treats AI content as clean without checking asset provenance and clearance.
- `quality_signal_miss`: Ignores comments about repetitive plots, weak endings, and visual drift.
- `hit_concentration_miss`: Fails to identify that views and paid users are concentrated in top series.
- `workflow_burden_miss`: Ignores increased revision rounds, continuity errors, legal review, or editor overtime.
- `artifact_incomplete`: Fails to produce one or more required deliverables.


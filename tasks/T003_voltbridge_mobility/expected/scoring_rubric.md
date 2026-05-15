# T003 Scoring Rubric

Total score: 100 points.

## 1. Task Completion - 15 points

- 4 points: Creates `operating_kpi_check.csv` with required columns.
- 4 points: Creates `ic_investment_note.md` with all required sections.
- 3 points: Creates `risk_log.md` with at least 5 material risks.
- 2 points: Creates `management_follow_up_email.md` with subject, greeting, questions, and next step.
- 2 points: Uses the required status and severity labels.

## 2. Factual Grounding - 15 points

- 5 points: Cites or clearly references the correct source files for major claims.
- 4 points: Does not introduce unsupported external facts.
- 3 points: Correctly distinguishes management claims from recalculated operating data.
- 3 points: Handles insufficient data with `needs_follow_up` or `not_enough_data`.

## 3. Operating / KPI Accuracy - 20 points

- 3 points: Correctly verifies total revenue growth at about 51.0%.
- 3 points: Correctly identifies blended ASP decline of about 17.4%.
- 2 points: Correctly identifies Southeast Asia ASP decline in both retail and marketplace channels.
- 3 points: Correctly calculates implied 2025 gross margin at about 25.3%, below management's 28.4% claim.
- 2 points: Correctly identifies reported EBITDA is negative despite positive adjusted EBITDA.
- 2 points: Correctly identifies that adjusted EBITDA depends heavily on questionable add-backs.
- 2 points: Correctly identifies operating cash flow is materially negative.
- 2 points: Correctly identifies cash conversion cycle is about 126.7 days versus management's 95 days.
- 1 point: Correctly identifies AR aging or top distributor receivables concentration.
- 1 point: Correctly identifies inventory days inconsistency: 137 days versus management's 118 days.
- 1 point: Correctly calculates total inventory over 180 days at about 19.0%.
- 2 points: Correctly calculates top three Europe distributor concentration.
- 2 points: Correctly identifies warranty cost at about 4.0% of revenue, above management's 3.2% claim.

## 4. PE / Growth Risk Assessment - 15 points

- 3 points: Flags that revenue growth quality is weakened by ASP and channel mix.
- 3 points: Flags Europe distributor concentration and extended payment terms.
- 3 points: Flags inventory aging and working capital risk.
- 2 points: Flags negative operating cash flow and adjusted EBITDA quality.
- 2 points: Flags warranty/return issues, especially battery and motor claims.
- 2 points: Flags regulatory/compliance and battery transport cost risk.

## 5. Investment Judgment - 20 points

- 5 points: Provides a clear `Proceed`, `Request Revised Plan`, or `Pause` recommendation.
- 5 points: Appropriately balances real export demand against operating quality issues.
- 4 points: Avoids mistaking headline revenue growth for high-quality growth.
- 3 points: Identifies what evidence or plan changes would be required to proceed.
- 3 points: Produces a conclusion useful to a PE/growth IC, not just a summary.

Strong answers are expected to recommend `Request Revised Plan` unless they make an unusually well-supported case for another answer. A `Proceed` answer should lose points if it does not condition the recommendation on inventory, distributor, warranty, and regulatory improvements.

## 6. Deliverable Quality - 10 points

- 4 points: IC note is structured, concise, and professional.
- 2 points: Risk log prioritizes material risks rather than generic concerns.
- 2 points: Follow-up email asks specific, answerable diligence questions.
- 2 points: Output is internally consistent across artifacts.

## 7. Traceability and Assumptions - 5 points

- 2 points: Clearly cites source files for major facts.
- 2 points: Shows calculation logic or assumptions for derived metrics.
- 1 point: Notes uncertainty where the data room is insufficient.

## Expected Failure Modes

Track the following failure tags where applicable:

- `headline_growth_bias`: Focuses on revenue growth while missing quality issues.
- `asp_decline_miss`: Fails to identify blended or regional ASP decline.
- `margin_mix_miss`: Misses channel or region margin deterioration.
- `inventory_miss`: Fails to flag aged inventory or cash conversion pressure.
- `concentration_miss`: Ignores distributor dependency.
- `warranty_miss`: Misses rising return or battery/motor warranty cost.
- `regulatory_miss`: Underweights EU compliance, battery transport, or tariff risk.
- `artifact_incomplete`: Fails to produce one or more required deliverables.

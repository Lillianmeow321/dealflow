# Failure Matrix

## Run Summary

| Task | Provider | Model | Total | Calculations | Golden Facts | Risks | Failure Tags | Diagnosis |
|---|---|---|---:|---:|---:|---:|---|---|
| T001_homepal_robotics | deepseek | deepseek-v4-flash | 86.36 | 54.55 | 100.00 | 100.00 | retention_miss, margin_miscalculation | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |
| T001_homepal_robotics | doubao | doubao-seed-1-6-flash-250828 | 87.73 | 59.09 | 100.00 | 100.00 | retention_miss, margin_miscalculation | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |
| T001_homepal_robotics | gemini | gemini-2.5-flash | 90.45 | 68.18 | 100.00 | 100.00 | - | No major automated failure pattern; review qualitative memo quality with rubric. |
| T001_homepal_robotics | moonshot | kimi-k2.6 | 91.82 | 72.73 | 100.00 | 100.00 | - | No major automated failure pattern; review qualitative memo quality with rubric. |
| T002_storyforge_ai | deepseek | deepseek-v4-flash | 90.00 | 66.67 | 100.00 | 100.00 | - | No major automated failure pattern; review qualitative memo quality with rubric. |
| T002_storyforge_ai | doubao | doubao-seed-1-6-flash-250828 | 95.00 | 83.33 | 100.00 | 100.00 | - | No major automated failure pattern; review qualitative memo quality with rubric. |
| T002_storyforge_ai | moonshot | kimi-k2.6 | 85.00 | 50.00 | 100.00 | 100.00 | monetization_miss | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |
| T003_voltbridge_mobility | deepseek | deepseek-v4-flash | 86.25 | 54.17 | 100.00 | 100.00 | asp_decline_miss, margin_mix_miss, inventory_miss | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |
| T003_voltbridge_mobility | doubao | doubao-seed-1-6-flash-250828 | 87.50 | 58.33 | 100.00 | 100.00 | asp_decline_miss, margin_mix_miss, inventory_miss | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |
| T003_voltbridge_mobility | moonshot | kimi-k2.6 | 88.75 | 62.50 | 100.00 | 100.00 | - | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |

## Failure Mode Counts

| Failure Mode | Count | Example Diagnosis |
|---|---:|---|
| `retention_miss` | 2 | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |
| `margin_miscalculation` | 2 | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |
| `asp_decline_miss` | 2 | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |
| `margin_mix_miss` | 2 | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |
| `inventory_miss` | 2 | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |
| `monetization_miss` | 1 | Strong synthesis and risk identification, but incomplete or imprecise KPI table calculations. |

## Iteration Notes

- Low calculation scores usually mean the model captured the narrative but did not fully populate the required KPI table.
- High golden fact and risk scores with lower calculation scores suggest the task is diagnosing spreadsheet discipline rather than investment synthesis.
- Repeated failure tags should feed back into either task wording, artifact schema, or deterministic checks.

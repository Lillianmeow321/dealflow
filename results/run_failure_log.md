# Run Failure Log

This log records run-level failures observed during DealFlowBench-mini testing. These failures are tracked separately from model-quality scores because they may come from provider availability, API behavior, timeout, output formatting, or harness compatibility rather than the model's investment reasoning capability.

## Failure Summary

| Task | Provider | Model | Failure Type | Included In Score Matrix? | Observation | Handling |
|---|---|---|---|---|---|---|
| T001 | Moonshot | kimi-k2.6 | Empty content / harness compatibility | No | Initial non-streaming Kimi K2.6 run returned empty `content`, producing no artifacts. | Updated Moonshot adapter to disable thinking for Kimi K2.6 and use the provider-required temperature. Reran successfully. |
| T001 | Gemini | gemini-2.5-flash | Output truncation / artifact incomplete | No | Initial run produced only a partial `product_kpi_check.csv`, so artifacts could not be parsed. | Increased `max_tokens` and reran successfully. |
| T002 | Gemini | gemini-2.5-flash | Provider availability | No | Provider returned HTTP 503 high-demand / unavailable error. | Recorded as provider-side run failure; excluded from T002 score comparison. |
| T003 | Gemini | gemini-2.5-flash | Provider/network failure | No | Provider connection reset during long-context run. | Recorded as provider-side run failure; excluded from T003 score comparison. |
| T003 | Moonshot | kimi-k2.6 | Remote disconnection on long task | No for failed run | One long-context run disconnected before response completion. | Increased timeout / reran successfully; latest successful Kimi run is included in the matrix. |

## Scoring Policy

- A run is included in the benchmark matrix only if it produces parseable artifacts and a valid `score_report.json`.
- Empty responses, provider-side 503 errors, connection resets, and known harness incompatibilities are treated as run-level failures, not as model-quality failures.
- Failed runs may still be useful for harness iteration, but they should not be mixed into model rankings.
- The aggregation script defaults to the latest valid run per task/provider/model and skips empty failed runs.

## Why This Matters

Real agent benchmarks need run hygiene. Without separating provider/runtime failures from task-performance failures, a leaderboard can punish models for API instability or harness mismatch rather than actual task capability.

In this prototype, run-level failure handling became part of the evaluation system itself:

```text
model execution
-> artifact parsing
-> run validity check
-> scoring only on valid runs
-> separate failure log for provider/harness issues
```


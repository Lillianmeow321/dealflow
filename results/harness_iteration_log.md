# Harness Iteration Log

This log summarizes how the DealFlowBench-mini evaluation harness evolved while running real model tests.

## Iteration Table

| Iteration | Issue Observed | Root Cause | Change Made | Impact |
|---|---|---|---|---|
| v0.1 | Manual scoring would not scale across models | Model outputs needed consistent artifact extraction and scoring | Added `run_model.py`, `evaluate_outputs.py`, and provider wrapper | Enabled repeatable API-based model runs and automated score reports |
| v0.2 | Provider API keys and model names changed during testing | Hard-coded model/provider assumptions would be brittle | Added `.env`-based provider configuration and command-line model override | Model selection can change without editing benchmark logic |
| v0.3 | Need to know which models a key can access | Users may not know provider model IDs | Added `list_models.py` for DeepSeek, Moonshot, Doubao, Gemini, and OpenRouter | Reduced setup friction and avoided guessing model IDs |
| v0.4 | Kimi K2.6 initial run returned empty content | Kimi K2.6 defaults to thinking behavior that was not compatible with the simple non-streaming parser | Added Moonshot/Kimi-specific handling: disable thinking and use provider-required temperature | Kimi K2.6 produced valid artifacts and was included in T001/T002/T003 |
| v0.5 | Long-context runs timed out or disconnected | Some providers needed longer read timeout for multi-file data rooms | Added `--timeout` to runner and client | Reduced false failures on longer tasks |
| v0.6 | Gemini initial T001 output was truncated | Output token budget was too low for all required artifacts | Increased `max_tokens` for reruns | Gemini T001 produced valid artifacts and became comparable |
| v0.7 | Failed runs polluted aggregate results | Old empty or incomplete runs appeared in result matrices | Updated `aggregate_results.py` to skip empty failed runs and default to latest valid run per task/provider/model | Result matrix became cleaner and closer to real eval reporting |
| v0.8 | Manual path copying was slow | Running, scoring, and aggregating each model individually created friction | Added `run_and_eval.py` for batch run + score + aggregate | Enabled efficient multi-provider runs from one terminal command |

## Current Harness

The current harness supports:

- OpenAI-compatible providers: DeepSeek, Moonshot/Kimi, Doubao, OpenRouter.
- Gemini API.
- `.env`-based API key and model configuration.
- Provider-specific defaults and overrides.
- Batch run and evaluate flow.
- Artifact extraction from model responses.
- Deterministic calculation checks.
- Golden fact and required-risk coverage checks.
- Failure tags and diagnostic summaries.
- Aggregated score and failure matrices.

## Current Limitations

- Artifact parsing still depends on models following the requested `### FILE: filename` format.
- Golden fact matching is keyword-based and can over-credit or under-credit paraphrases.
- Calculation checks currently look for expected values in outputs rather than fully parsing each KPI table into typed fields.
- The evaluator does not yet score memo quality with a calibrated LLM judge or human expert.
- Provider-side runtime instability is logged but not automatically retried with exponential backoff.

## Next Harness Iterations

Recommended next steps:

1. Parse output CSV artifacts into structured rows and compare metric names to expected checks.
2. Add an LLM-as-judge layer for investment memo quality, using a fixed rubric and pairwise comparison.
3. Add human calibration on a small sample to measure agreement between expert judgment and automated scores.
4. Add retry policy for provider/network failures.
5. Add trace scoring for future browser/file-system agents.
6. Generate randomized task variants to reduce overfitting and prompt leakage.

## Takeaway

The benchmark did not stay fixed after the first run. The harness changed in response to real failure modes: provider quirks, output truncation, timeout, parsing failure, and result contamination. This mirrors how production eval systems evolve: the scoring rubric matters, but the harness reliability and failure accounting matter just as much.


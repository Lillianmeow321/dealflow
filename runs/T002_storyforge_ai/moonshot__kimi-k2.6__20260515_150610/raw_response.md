### FILE: content_kpi_check.csv
```csv
metric,company_reported_value,recalculated_or_verified_value,status,note
Cost per episode before AI,6800,6800,verified,From production_workflow.md and cost_comparison.csv
Cost per episode after AI,2450,2450,verified,From production_workflow.md and cost_comparison.csv; management claim of 64% reduction is accurate ((6800-2450)/6800 = 63.97%)
Production cycle time before AI,14 days,14 days,verified,From production_workflow.md and cost_comparison.csv
Production cycle time after AI,4.5 days,4.5 days,verified,From production_workflow.md and cost_comparison.csv; management claim of 68% faster is accurate ((14-4.5)/14 = 67.86%)
Output volume increase,4.1x (18 to 74 episodes/month),4.11x (18 to 74 episodes/month),verified,From cost_comparison.csv; 74/18 = 4.11x
Episode completion rate,49%,47.31%,inconsistent,Management reports 49% across launched series; recalculated from episode_performance.csv as 11,128,000 / 23,520,000 = 47.31%. Note: company may weight by series or use different denominator
Series continuation rate,Not explicitly stated,31.96%,needs_follow_up,Calculated from episode_performance.csv as 3,556,000 / 11,128,000 = 31.96%; management does not provide a direct comparable figure
Paid conversion rate,11% among engaged viewers,9.27%,inconsistent,Management claims 11% paid conversion among engaged viewers; recalculated from episode_performance.csv as 166,685 / 1,798,000 = 9.27%. Discrepancy may reflect definition of engaged viewers or timing differences
Revenue per completed viewer,Not stated,0.027 USD,needs_follow_up,Calculated from episode_performance.csv as total revenue ($410,833) / completions (11,128,000) = $0.037 per completion; or paid revenue ($300,033) / completions = $0.027. Management does not provide this metric
Platform concentration,Not explicitly stated,71% TikTok views; 63% TikTok paid users,verified,From platform_distribution_report.md; extreme concentration on single platform
Copyright/IP risk status,Manageable,Manageable but with significant gaps,needs_follow_up,From copyright_ip_memo.md: no formal chain-of-title, inconsistent asset provenance tracking, two platform notices received, no external clearance for top series, inconsistent contractor IP assignment
```

### FILE: investment_memo.md
```markdown
# Preliminary Investment Memo: StoryForge AI Content Studio

## Recommendation

**Hold**

One-sentence rationale: StoryForge AI demonstrates genuine production efficiency gains from generative AI, but the combination of extreme platform concentration, declining content quality at scale, weak and inconsistent monetization, and unaddressed IP risks make the current $9M ask premature without stronger evidence of durable audience ownership and franchise repeatability.

---

## Company Overview

StoryForge AI is an AI-native content studio producing short-form comic dramas and vertical manga series for mobile-first audiences. The company distributes through TikTok, YouTube Shorts, Instagram Reels, Webtoon-style platforms, and its own app, with monetization via in-app paid unlocks, platform revenue share, and nascent sponsorship placements. The company is raising $9M to expand production slate, hire editorial and legal staff, improve its story testing dashboard, acquire paid app traffic, and develop premium original IP franchises. (Sources: company_overview.md, platform_distribution_report.md)

---

## AI Workflow and Production Advantage

**Verified Efficiency Gains**

StoryForge's AI-assisted workflow delivers measurable production improvements:
- **Cost reduction**: $6,800 to $2,450 per episode (64% decrease) (cost_comparison.csv, production_workflow.md)
- **Cycle time reduction**: 14 days to 4.5 days (68% faster) (cost_comparison.csv, production_workflow.md)
- **Output increase**: 18 to 74 episodes/month (4.1x) (cost_comparison.csv)

**Quality-Scale Tradeoffs**

However, these gains come with material operational costs that management underemphasizes:
- Continuity error rate increased from 4% to 11% (cost_comparison.csv)
- Revision rounds increased from 3.2 to 4.6 per episode, indicating AI output requires more human correction (cost_comparison.csv)
- Editor overtime spiked from 6 to 18 hours/week during high-output periods (cost_comparison.csv)
- Character face drift and visual inconsistency emerge after ~20 episodes, per audience complaints (audience_comments.md, production_workflow.md)

**Assessment**: The production advantage is real but narrow. It enables *more* content and *faster testing*, not necessarily *better* content. The workflow appears optimized for volume of "shots on goal" rather than sustained franchise quality. The increase in continuity errors and editor workload suggests diminishing returns as series extend—critical for building durable IP.

---

## Content Performance and Monetization Quality

**View Concentration in Outliers**

Total reported views of 43.5M are heavily concentrated: the top two series (CEO Contract Bride, Reborn As The Villainess) generate 70% of views and 71% of paid users. The remaining six series show steep performance decay. (episode_performance.csv)

| Metric | Company Claim | Recalculated | Gap |
|--------|-------------|------------|-----|
| Episode completion rate | 49% | 47.3% | Minor |
| Paid conversion (engaged viewers) | 11% | 9.3% | Material |

**Retention and Continuation Weakness**

Series continuation rate (completions → series continuations) is 32%—meaning 68% of viewers who finish an episode do not continue the series. This drops further in later episodes: Reborn As The Villainess shows "retention drops after episode 10" (episode_performance.csv notes). Audience comments cite "repetitive plot arcs," "weak endings," and "feels like five romance tropes stitched together" (audience_comments.md).

**Monetization Quality**

- Total revenue per completed viewer: ~$0.037 (all revenue) or $0.027 (paid revenue only)
- Platform revenue share ($110,800) exceeds paid unlock revenue on a gross basis for several smaller series
- Paid acquisition economics are unproven: $1.42 CPI, 6.5% trial-to-paid, 18% day-7 retention, no proven payback period (platform_distribution_report.md)

**Assessment**: Hits are not clearly repeatable. The top series benefit from strong hooks and cliffhangers, but audience feedback indicates formulaic construction. Paid conversion is weaker than reported, and the path to venture-scale unit economics depends on unproven paid acquisition and IP licensing that has not yet materialized.

---

## Platform Distribution Assessment

**Extreme TikTok Dependency**

| Platform | View Share | Paid User Share |
|----------|-----------|-----------------|
| TikTok | 71% | 63% |
| YouTube Shorts | 18% | 15% |
| Instagram Reels | 6% | 3% |
| Webtoon communities | 3% | 8% |
| StoryForge app | 2% | 11% |

(platform_distribution_report.md)

A March TikTok algorithm change reduced new-series first-week impressions by 37%. The team's response—more hook testing and paid app retargeting—does not address structural dependency. The owned app, while highest monetization per user, represents only 2% of views and 11% of paid users.

**Assessment**: Platform arbitrage risk is high. The company is building on rented land with minimal owned-audience transfer. The app is strategically important but unproven at scale.

---

## Copyright / IP Risk Assessment

Current controls are inadequate for venture-scale IP development:

| Issue | Evidence | Severity |
|-------|----------|----------|
| No panel-level asset provenance | copyright_ip_memo.md | High |
| Style similarity to known franchises in prompts | copyright_ip_memo.md | High |
| Two platform notices for character similarity | copyright_ip_memo.md | Medium |
| No formal chain-of-title for AI assets | copyright_ip_memo.md | High |
| No external clearance for top 3 series | copyright_ip_memo.md | High |
| Inconsistent contractor IP assignment | copyright_ip_memo.md | Medium |

Counsel explicitly states risk is "not yet appropriate for large-scale IP licensing or adaptation" (copyright_ip_memo.md). This directly undermines the $9M fundraise's stated goal of "premium original IP franchises" and "future IP licensing."

---

## Key Positive Signals

1. **Genuine production efficiency**: 64% cost reduction and 4x output increase are verified and meaningful for a content business (cost_comparison.csv, production_workflow.md)
2. **Proven hook capability**: CEO Contract Bride reached 18.4M views with strong cliffhanger engagement; audience acknowledges "I know this plot is ridiculous but I need the next episode" (episode_performance.csv, audience_comments.md)
3. **Early monetization infrastructure**: In-app unlocks generate $300K in paid revenue with functioning payment flow (episode_performance.csv)
4. **Data-driven testing culture**: Management emphasizes fast iteration and genre-specific prompts, suggesting organizational learning potential (company_overview.md)
5. **Higher-intent Webtoon community**: Small but 8% of paid users from 3% of views suggests format-audience fit for longer-form content (platform_distribution_report.md)

---

## Key Risks and Diligence Flags

1. **Platform concentration with algorithm volatility**: 71% TikTok dependency; 37% impression drop from single algorithm change with no durable mitigation (platform_distribution_report.md)
2. **Quality degradation at scale**: Continuity errors up 175%, editor overtime tripling, and audience complaints of "AI-looking" content as series extend (cost_comparison.csv, audience_comments.md, production_workflow.md)
3. **Unaddressed IP infrastructure**: No clearance for top series, no chain-of-title, inconsistent contractor rights—blocking licensing path (copyright_ip_memo.md)
4. **Weak paid conversion and unproven acquisition**: 9.3% actual vs. 11% claimed paid conversion; $1.42 CPI with 18% day-7 retention and no payback proof (episode_performance.csv, platform_distribution_report.md)
5. **Hit non-repeatability**: Top 2 of 8 series drive 70% of performance; no evidence of systematic hit generation vs. outliers (episode_performance.csv)
6. **Management metric optimism**: Reported completion and conversion rates are directionally close but consistently favorable to company; revision rounds and error rates are underemphasized (content_kpi_check.csv)

---

## Follow-Up Questions

See founder_follow_up_email.md for detailed questions. Priority areas:
1. Reconciliation of 11% claimed vs. 9.3% calculated paid conversion
2. Plan to reduce TikTok dependency below 50% and app growth trajectory
3. IP clearance timeline and budget for top 3 series
4. Evidence of repeatable hit formula beyond first two series
5. Editor capacity planning and continuity error reduction roadmap
6. Paid acquisition payback period target and current cohort data
```

### FILE: risk_log.md
```markdown
# Risk Log: StoryForge AI Content Studio

| risk | evidence_from_data_room | severity | suggested_follow_up |
|------|------------------------|----------|---------------------|
| Extreme platform concentration with algorithm dependency | TikTok represents 71% of views and 63% of paid users; March algorithm change reduced new-series impressions by 37% with limited offset capability (platform_distribution_report.md) | high | Request 12-month platform mix targets and specific investment in owned app/YouTube long-form; verify if any platform exclusivity or MCN obligations exist |
| Content quality degradation at series length and scale | Continuity error rate increased from 4% to 11%; editor overtime tripled; audience reports face drift after episode 9, "AI-looking" content, and repetitive plots; workflow notes continuity issues beyond 20 episodes (cost_comparison.csv, audience_comments.md, production_workflow.md) | high | Request episode-level retention curves for top 3 series; ask for editor hiring plan and tooling roadmap to reduce continuity errors; test if 20-episode limit is hard constraint |
| Unresolved copyright and IP infrastructure blocking licensing path | No panel-level asset provenance; no formal chain-of-title; two platform notices for character similarity; no external clearance for top 3 series; inconsistent contractor IP assignment; counsel explicitly states not ready for licensing (copyright_ip_memo.md) | high | Request 90-day IP remediation plan with budget; confirm if any pending claims beyond two notices; obtain updated contractor templates; verify insurance coverage for IP claims |
| Overstated paid conversion and unproven unit economics | Management claims 11% paid conversion; recalculated at 9.3%; paid acquisition shows $1.42 CPI, 6.5% trial-to-paid, 18% day-7 retention with no proven payback (episode_performance.csv, platform_distribution_report.md) | high | Request detailed cohort analysis of paid acquisition from test campaigns; reconcile engaged viewer definition with paid conversion calculation; obtain LTV/CAC target and timeline to prove unit economics |
| Hit non-repeatability and outlier-driven performance | Top 2 of 8 series generate 70% of views and paid users; remaining series show steep decay; no evidence of systematic hit generation vs. lucky outliers (episode_performance.csv) | medium | Request pipeline of next 12 series with genre/thesis; ask for pre-launch predictive scoring; analyze whether top series success was replicable or timing/algorithm-dependent |
| Management metric presentation optimism | Consistent pattern of favorable rounding (11% vs. 9.3%, 49% vs. 47.3%); operational challenges (revision rounds, error rates, legal hours) are buried in data tables not highlighted in narrative (content_kpi_check.csv, company_overview.md, cost_comparison.csv) | medium | Request full data room with raw episode-level data; ask management to present their own risk assessment; evaluate founder transparency and board reporting quality in reference checks |
```

### FILE: founder_follow_up_email.md
```markdown
Subject: Follow-up Questions from [Fund Name] — StoryForge AI Diligence

Hi [Founder Name],

Thank you for sharing the StoryForge data room with our team. We've completed our initial review and are impressed by the verified production efficiency gains and the early traction of CEO Contract Bride and Reborn As The Villainess.

Before we determine next steps, we'd like to clarify several areas where additional detail would help us assess the durability of the business. Our questions below:

**1. Paid Conversion Methodology**
You report 11% paid conversion among "engaged viewers." Our recalculation from episode-level data shows 166,685 paid users against 1,798,000 engaged viewers, or 9.3%. Could you walk us through how you define and count "engaged viewers" for this metric? Is there a timing or cohort difference in the denominator?

**2. Platform Concentration and Owned App Strategy**
TikTok represents 71% of views and 63% of paid users, and the March algorithm change reduced new-series impressions by 37%. What is your target platform mix in 12–18 months, and what specific investment from this round will reduce TikTok dependency below 50%? Separately, what is your path to grow the StoryForge app from 2% of views to a material acquisition channel?

**3. IP Clearance and Licensing Readiness**
Outside counsel notes that current controls are "not yet appropriate for large-scale IP licensing or adaptation." Your fundraise includes premium IP franchise development. What is your 90-day plan and budget to complete external clearance for your top three series, implement panel-level asset provenance, and update contractor IP assignment templates? Have you received any additional platform notices or informal claims beyond the two disclosed?

**4. Repeatable Hit Formula vs. Outliers**
Your top two series drive 70% of total views and paid users. What evidence do you have that this performance is repeatable through process rather than dependent on timing, algorithm luck, or specific creator talent? Could you share your pipeline of the next 12 series with pre-launch scoring or predictive framework?

**5. Quality at Scale and Editor Capacity**
Continuity errors increased from 4% to 11%, and editor overtime tripled to 18 hours/week during high-output periods. Audience feedback cites face drift after episode 9 and "AI-looking" quality drops. What is your hiring plan for story editors, and what tooling or workflow changes do you believe can extend series quality beyond 20 episodes without linear cost increases?

**6. Paid Acquisition Economics**
Your early paid acquisition tests show $1.42 CPI and 6.5% trial-to-paid with 18% day-7 retention. What is your target LTV/CAC ratio and timeline to prove payback? Can you share cohort retention and revenue data from these test campaigns?

**Next Step**

If you're open to it, we'd like to schedule a 60-minute call next week to discuss these questions and tour your story testing dashboard. We're particularly interested in understanding whether the production advantages you've built can translate into durable franchise economics and owned audience relationships.

Please let us know your availability.

Best,

[Your Name]
Investment Associate
[Fund Name]
[Email] | [Phone]
```
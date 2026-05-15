### FILE: content_kpi_check.csv
```csv
metric,company_reported_value,recalculated_or_verified_value,status,note
Cost per episode before AI,6800,6800,verified,From cost_comparison.csv before_ai_workflow column
Cost per episode after AI,2450,2450,verified,From cost_comparison.csv current_ai_workflow column
Production cycle time before AI (days),14,14,verified,From cost_comparison.csv before_ai_workflow column
Production cycle time after AI (days),4.5,4.5,verified,From cost_comparison.csv current_ai_workflow column
Output volume increase (multiple),4.1x,4.11x,verified,From cost_comparison.csv: 74/18 = 4.11
Episode completion rate,49%,47.3%,inconsistent,Recalculated from episode_performance.csv: 11,128,000 completions / 23,520,000 starts = 0.473; difference may be due to rounding or series subset
Series continuation rate,not reported,not calculable,not_enough_data,No clear denominator; series_continuations (3,556,000) vs engaged viewers (1,798,000); definition unclear
Paid conversion rate (engaged viewers),11%,9.27%,inconsistent,Recalculated: 166,685 paid users / 1,798,000 engaged viewers = 0.0927
Revenue per completed viewer (USD),not reported,0.037,needs_follow_up,Total revenue ($410,833) / total completions (11,128,000) = $0.037; low figure suggests either definition mismatch or weak monetization
Platform concentration (TikTok share of views),not reported,71%,verified,From platform_distribution_report.md; high dependency
Copyright/IP risk status,not reported,high risk,needs_follow_up,From copyright_ip_memo.md: no chain-of-title, platform notices, incomplete contractor rights
```

### FILE: investment_memo.md
```markdown
# Preliminary Investment Memo: StoryForge AI

## Recommendation

**Hold**

One-sentence rationale: AI reduces production cost and cycle time, but hit rates are inconsistent, paid conversion is lower than claimed, platform dependency on TikTok is extreme, and copyright/IP controls are too immature for a venture-scale IP business.

## Company Overview

StoryForge AI is an AI-native content studio producing short-form comic dramas, vertical manga series, and serialized visual fiction for mobile-first audiences. Content is distributed on TikTok, YouTube Shorts, Instagram Reels, Webtoon-style platforms, and the company’s own app. The company is raising a $9M Seed+/pre-Series A round. Management claims that generative AI has reduced episode cost by 64%, cycle time by 68%, and increased monthly output from 18 to 74 episodes.

## AI Workflow and Production Advantage

The shift from a traditional outsourced workflow to an AI-assisted pipeline is well-documented in the *cost_comparison.csv* and *production_workflow.md* files:

- Cost per episode: $6,800 → $2,450 (verified 64% reduction).
- Cycle time: 14 days → 4.5 days (verified 68% reduction).
- Monthly output: 18 → 74 episodes (verified 4.1x increase).
- Human hours per episode: 112 → 46 (verified 59% reduction).

However, the same data reveals quality and operational trade-offs:

- Revision rounds increased from 3.2 to 4.6 (not highlighted by management).
- Continuity error rate rose from 4% to 11%.
- Legal review hours per series increased from 2 to 7.
- Average editor overtime per week increased from 6 to 18 hours.

These caveats suggest that while AI accelerates initial visual production, human oversight for consistency and provenance is growing. The advantage is not a pure scalable automation; it is a semi-automated assembly line that still depends on skilled editors to compensate for AI-generated errors. The gains are real but incremental improvements may face diminishing returns as series lengthen.

## Content Performance and Monetization Quality

From *episode_performance.csv* and *audience_comments.md*:

- Two series (`CEO Contract Bride` and `Reborn As The Villainess`) account for 70% of total views and 84% of paid revenue. The remaining six series show much weaker engagement and monetization.
- Episode completion rate is 47.3% (recalculated), below the reported 49%.
- Paid conversion among engaged viewers is 9.27% (recalculated), below the reported 11%.
- Revenue per completed viewer is only ~$0.037, indicating that even among users who finish an episode, very few convert to paying or generate meaningful revenue.
- Audience comments consistently mention repetitive plots, inconsistent character faces, and weak endings. Paid users are more critical.

The hit pattern is heavily skewed. The company is not yet demonstrating repeatable success across a portfolio; it has two hot series and a long tail of underperformers.

## Platform Distribution

*platform_distribution_report.md* shows:

- TikTok drives 71% of total views, 68% of engaged viewers, and 63% of paid users.
- The StoryForge app contributes only 2% of views but 11% of paid users, indicating higher intent but a tiny funnel.
- A March TikTok algorithm change reduced new-series first-week impressions by 37%.
- Paid acquisition for the app shows early CPI of $1.42, trial-to-paid conversion of 6.5%, and Day-7 retention of 18%. Payback period is unproven.

The business is highly dependent on a single algorithm-controlled platform. Distribution concentration creates significant risk if TikTok changes recommendations or policy on AI-generated content.

## Copyright / IP Risk

*copyright_ip_memo.md* outlines multiple material issues:

- No chain-of-title process for AI-generated visual assets.
- Two platform notices regarding character similarity.
- No external clearance for top series.
- Freelance story editor contracts do not consistently assign derivative work rights.
- Counsel views current controls as sufficient for early testing but insufficient for IP licensing.

Since the company’s long-term value thesis depends on building owned IP franchises, the current IP posture is a serious vulnerability.

## Key Positive Signals

1. **Real cost and speed improvements** – Verified reductions in cost, cycle time, and output volume. (cost_comparison.csv, production_workflow.md)
2. **Two breakout series** – CEO Contract Bride and Reborn As The Villainess show strong view counts, completion rates, and monetization. (episode_performance.csv)
3. **App monetization signal** – StoryForge app users have 11% share of paid users despite only 2% of views, indicating potential for controlled distribution. (platform_distribution_report.md)
4. **Reactive distribution team** – The team successfully mitigated a TikTok algorithm change by testing hooks and moving to paid retargeting. (platform_distribution_report.md)

## Key Risks and Diligence Flags

1. **Platform concentration** – 71% of views on TikTok; algorithm changes directly threaten top-line growth. (platform_distribution_report.md)
2. **Inconsistent hit success** – Only two of eight series drive the majority of engagement and revenue; portfolio repeatability unproven. (episode_performance.csv)
3. **Inflated conversion metrics** – Paid conversion (9.27% vs. reported 11%) and completion rate (47.3% vs. reported 49%) are lower when recalculated. (episode_performance.csv)
4. **Weak monetization per viewer** – Revenue per completed viewer is $0.037; even engaged viewers convert at low rates. (episode_performance.csv)
5. **Copyright/IP risk** – No chain-of-title, platform notices, and incomplete contractor rights block any large-scale IP licensing strategy. (copyright_ip_memo.md)
6. **Quality degradation at scale** – Continuity errors increase with long series; audience comments report deteriorating visuals. (cost_comparison.csv, audience_comments.md)
7. **Editor workload bottleneck** – Editor overtime nearly tripled; human editors are critical for consistency and may not scale linearly. (cost_comparison.csv)

## Follow-Up Questions

- What is the exact definition of “engaged viewer” and “paid conversion”? Why does the recalculated rate differ?
- What is the series continuation rate over a 30-day window for the top two series?
- What is the churn experience for paid app users? What is the average revenue per paying user?
- How does the team plan to reduce platform concentration? What are the current organic vs. paid acquisition splits?
- What is the specific timeline for implementing panel-level provenance tracking and external clearance for IP?
- How does the team manage editor workload sustainability as the slate grows?
- What is the dollar cost per engaged viewer on TikTok? Is unit economics improving?

```

### FILE: risk_log.md
```markdown
# Risk Log: StoryForge AI

| Risk | Evidence from Data Room | Severity | Suggested Follow-Up |
|---|---|---|---|
| Platform concentration on TikTok | TikTok drives 71% of views and 68% of engaged viewers; algorithm change in March cut new-series impressions by 37% (platform_distribution_report.md) | high | Request monthly platform mix trends and sensitivity analysis for a 50% drop in TikTok traffic |
| Copyright/IP provenance gaps | No chain-of-title for AI assets; two platform notices for character similarity; contractor rights not fully assigned (copyright_ip_memo.md) | high | Ask for external IP audit timeline and budget; review updated contractor templates |
| Inconsistent content quality | Continuity error rate rose from 4% to 11% (cost_comparison.csv); audience comments report repetitive plots, inconsistent faces, weak endings (audience_comments.md) | high | Request internal quality score tracking across all series; analyze correlation with continuation and paid conversion |
| Inflated management KPIs | Paid conversion recalculated at 9.27% vs. reported 11%; episode completion rate recalculated at 47.3% vs. reported 49% (episode_performance.csv) | medium | Request raw data and exact definitions for all reported metrics; validate with cohort analysis |
| Weak unit economics | Revenue per completed viewer is $0.037; app paid acquisition CPI $1.42 with 18% D7 retention and unproven payback (episode_performance.csv, platform_distribution_report.md) | high | Request detailed cohort LTV and payback period; ask for breakeven timeline for paid acquisition |
| Concentration in hit franchises | CEO Contract Bride and Reborn As The Villainess represent 70% of views and 84% of paid revenue; remaining six series underperform (episode_performance.csv) | medium | Ask for production roadmap and validation of past portfolio performance; test new series concept testing methodology |
| Editor workload bottleneck | Editor overtime increased from 6 to 18 hours/week (cost_comparison.csv); human editors are critical for consistency and copyright review | medium | Request editor headcount plan and tools to reduce manual review; assess scalability of current workflow |
```

### FILE: founder_follow_up_email.md
```
Subject: StoryForge AI Diligence – Follow-Up Questions

Dear [Founder's Name],

Thank you for your time last week. We have completed our initial review of StoryForge AI using the materials you provided. The AI production efficiency gains are compelling, and the early traction of CEO Contract Bride and Reborn As The Villainess is impressive.

As we move to the next stage of diligence, we would appreciate clarification on a few items.

1. **Key Metric Definitions**: Could you provide the exact definitions for “engaged viewer” and “paid conversion”? Our recalculations using the aggregated data show a conversion rate of ~9.3% versus the 11% you reported. Similarly, the episode completion rate appears closer to 47% than the 49% stated. Understanding the denominator and any exclusions would be helpful.

2. **Series Continuation**: What is the 30-day series continuation rate for your top two series? We want to understand how many viewers return for subsequent episodes.

3. **Paid User Retention**: What is the average revenue per paying user and the churn curve for in-app purchasers? How long is the typical paid subscription window?

4. **Platform Dependency**: Given that 71% of views come from TikTok, can you share your organic vs. paid acquisition mix and how you plan to reduce concentration risk? Do you have contingency plans for further algorithm changes?

5. **Copyright/IP Plan**: Your legal memo highlights gaps in asset provenance and contractor IP assignments. Do you have a timeline and budget for implementing panel-level tracking, external clearance for top series, and updated contributor contracts? This is critical for the IP licensing strategy.

6. **Editor Scalability**: Editor overtime has tripled in the AI workflow. How do you plan to scale editorial capacity as the slate grows? Are there automation tools you’re exploring for continuity and provenance checks?

7. **Unit Economics of Paid Acquisition**: Your early paid acquisition campaigns show a CPI of $1.42 and D7 retention of 18%. What is the estimated payback period, and what is the dollar cost per engaged viewer on TikTok?

Our next step would be to set up a 30-minute call to discuss these questions and any additional data you can share. We are also interested in a live demo of your testing dashboard.

Please let me know what time works best next week.

Best regards,

[Your Name]
Investment Associate
```
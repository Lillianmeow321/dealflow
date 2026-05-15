### FILE: operating_kpi_check.csv
```csv
metric,management_reported_value,recalculated_or_verified_value,status,note
Revenue growth by region - Europe,2025 revenue $36.2M up 48% YoY (from $24.3M),2025 Europe revenue $36.2M vs 2024 $24.3M = 48.8% growth,verified,"Source: regional_sales.csv; growth driven by top_3_distributors (+40.1%) and Southeast Asia retail (+143.8%)"
Revenue growth by region - Southeast Asia,2025 revenue $10.7M up 128% YoY (from $4.7M),2025 Southeast Asia revenue $10.7M vs 2024 $4.7M = 127.7% growth,verified,"Source: regional_sales.csv; fastest growing region but from low base, driven by retail partners and marketplace"
Gross margin by channel - Europe top 3 distributors,Not explicitly stated by channel in management presentation,29.0% in 2025 vs 31.5% in 2024,verified,"Source: gross_margin_by_channel.csv; 250 bps compression YoY on strategic volume"
Gross margin by channel - Europe Amazon marketplace,Not explicitly stated by channel,21.0% in 2025 vs 27.0% in 2024,verified,"Source: gross_margin_by_channel.csv; 600 bps compression, promotions and returns pressure"
Gross margin by channel - Southeast Asia retail partners,Not explicitly stated by channel,18.5% in 2025 vs 24.5% in 2024,verified,"Source: gross_margin_by_channel.csv; 600 bps compression, entry-level mix shift"
Gross margin by channel - Southeast Asia marketplace,Not explicitly stated by channel,14.0% in 2025 vs 22.0% in 2024,verified,"Source: gross_margin_by_channel.csv; 800 bps compression, aggressive pricing"
EBITDA / adjusted EBITDA quality,Adjusted EBITDA of $1.1M,Reported EBITDA is -$1.82M; adjusted EBITDA of $1.1M relies on $2.9M of questionable/partly recurring add-backs,inconsistent,"Source: adjusted_ebitda_bridge.csv; only $320K add-back (founder recruiting) rated 'acceptable', $2.0M rated 'questionable', $420K 'partial'"
Europe distributor concentration,Top 3 distributors provide scale and local coverage,Top 3 distributors = 66.6% of Europe revenue and 51.5% of total company revenue,verified,"Source: distributor_contracts_summary.md; NordBike alone is 29.3% of Europe revenue"
Southeast Asia ASP trend,Not explicitly discussed,ASP declined from $500 to $400 for retail partners (-20%) and $455 to $341 for marketplace (-25%),verified,"Source: regional_sales.csv; severe ASP erosion indicating pricing-driven growth, not brand-driven"
Inventory days,118 days (management headline),159.8 days using year-end inventory/COGS*365; 137 days using total inventory and implied daily COGS,inconsistent,"Source: inventory_aging.csv notes say 'Management headline inventory days excludes China buffer stock'; working_capital_schedule.csv shows 159.8 days"
Inventory aging over 180 days,Not explicitly stated,19.0% of total inventory ($2.9M); Europe specifically 24.5% ($2.3M),verified,"Source: inventory_aging.csv; Europe over-180-days inventory up significantly with prior-year commuter and slow cargo SKUs"
Warranty cost as % of revenue,3.2% (management presentation),4.0% actual warranty cost / revenue; 3.2% appears to exclude pending distributor claims,inconsistent,"Source: warranty_and_returns.csv total shows 4.0%; management_presentation.md cites 3.2% 'excluding pending distributor claims'"
Return rate by region - Europe,Not explicitly stated,6.4% weighted average for Europe channels (6.8% top 3 distributors; 9.4% Amazon),verified,"Source: warranty_and_returns.csv; Amazon marketplace highest at 9.4%"
Return rate by region - Southeast Asia,Not explicitly stated,4.2% weighted average for Southeast Asia channels (3.8% retail; 5.6% marketplace),verified,"Source: warranty_and_returns.csv; lower than Europe but rising on marketplace channel"
Cash conversion cycle,95 days (management presentation),162.0 days using year-end balances; 126.7 days using average balances,inconsistent,"Source: working_capital_schedule.csv; management's 95 days not reconcilable to any calculation methodology in data room"
Operating cash flow,Not explicitly stated as negative,-$9.8M in 2025; cumulative -$13.6M over 2023-2025,verified,"Source: cash_flow_statement.csv; deeply negative operating cash flow despite revenue growth, funded by debt and equity"
Regulatory / tariff exposure,Manageable; key models have CE and EN15194,Updated cargo model needs EN15194; battery UN38.3 incomplete; EU anti-dumping scrutiny; 1.2-1.8pp logistics cost increase possible,needs_follow_up,"Source: regulatory_tariff_memo.md; compliance risk 'manageable but not fully reflected in operating plan'; counsel recommends dedicated compliance budget before 2026 expansion"
```

### FILE: ic_investment_note.md
```markdown
# IC Investment Note: VoltBridge Mobility

## Recommendation

**Pause**

One-sentence rationale: Headline revenue growth of 51% masks severe channel degradation, margin compression, negative operating cash flow, rising warranty costs, and regulatory gaps that suggest the business is consuming capital to buy low-quality market share rather than building sustainable export economics.

---

## Company Overview

VoltBridge Mobility is a Shenzhen-based e-bike design and export company selling to European distributors, Amazon marketplaces, a small DTC site, and Southeast Asian retail partners. The company generated $46.8M in 2025 revenue (up 51% YoY) and is seeking $20M growth capital to fund inventory, European service centers, Southeast Asia expansion, battery certification, and working capital for distributor payment terms. The company operates with contract manufacturers in Guangdong and Zhejiang and maintains limited owned infrastructure.

## Export Market and Channel Assessment

**Europe (77% of 2025 revenue):** Growth of 48.8% appears robust but is increasingly concentrated and lower-quality. The top three distributors (NordBike, VeloMaison, Nordic Motion) represent 66.6% of European revenue and 51.5% of total company revenue, with payment terms extending to 75-90 days and active disputes over rebates, sell-through support, and warranty claims (distributor_contracts_summary.md; ar_aging.csv). Amazon marketplace grew 46.4% but at 21.0% gross margin with 9.4% return rates. DTC, the highest-quality channel at 32.0% margin, remains only 3.6% of revenue.

**Southeast Asia (23% of 2025 revenue):** Revenue more than doubled (+127.7%), but this is entirely volume-driven with severe ASP erosion. Retail partner ASP fell from $500 to $400 (-20%); marketplace ASP collapsed from $455 to $341 (-25%). Unit growth of 205% for retail partners and 158% for marketplace masks a race-to-the-bottom dynamic. Gross margins compressed to 18.5% and 14.0% respectively, with the marketplace channel now below typical consumer electronics levels (gross_margin_by_channel.csv; regional_sales.csv).

**Channel Quality Conclusion:** Growth is shifting toward lower-margin, higher-return, more capital-intensive channels. The fastest-growing segments (Southeast Asia retail, Amazon Europe) are the least profitable. This is not sustainable quality growth.

## Revenue Quality

Revenue quality is deteriorating across multiple dimensions:

- **ASP Decline:** Blended ASP fell from $734 to $606 (-17.4%), driven by mix shift to entry-level Southeast Asia models and promotional pricing in Europe (regional_sales.csv).
- **Distributor Concentration & AR Risk:** NordBike alone represents 29.3% of European revenue and has $3.6M in receivables with $900K over 90 days, while requesting extended 2026 terms. Total AR of $11.8M exceeds the revenue table because it includes gross billings before credits, suggesting revenue recognition may be aggressive (ar_aging.csv; balance_sheet.csv).
- **Rebate and Warranty Disputes:** VeloMaison has an active rebate dispute; Nordic Motion is withholding $400K pending motor controller warranty claims. These are not one-off issues but structural tensions in the distributor model (distributor_contracts_summary.md; ar_aging.csv).
- **Cash Collection Deteriorating:** DSO increased from 74.8 to 92.0 days, with management's 2026 plan assuming an unrealistic improvement to 57.8 days despite larger revenue and ongoing distributor negotiations (working_capital_schedule.csv).

## Margin, Inventory, and Warranty

**Gross Margin:** Reported gross margin of 25.3% (down from 30.1% in 2024) is actually overstated. Management's presentation claims 28.4% by excluding certain warranty accruals from the gross margin bridge (gross_margin_by_channel.csv notes). Every channel except DTC saw margin compression, with Southeast Asia marketplace at 14.0%—likely unprofitable after operating costs.

**Inventory:** Inventory days are 159.8 (year-end method) or 137 (total including buffer stock), not the 118 days management claims. The discrepancy arises because management excludes China buffer stock. More critically, 19.0% of inventory ($2.9M) is over 180 days, including 24.5% in Europe ($2.3M) tied to prior-year commuter models and slow-moving cargo SKUs. The $500K inventory markdown add-back in adjusted EBITDA is questionable because aged inventory remains elevated (inventory_aging.csv; adjusted_ebitda_bridge.csv).

**Warranty & Returns:** Actual warranty cost is 4.0% of revenue, not the 3.2% management cites. The 3.2% figure excludes pending distributor claims. Winter motor controller failures and battery range complaints drove 1,525 battery-related and 988 motor-controller claims in 2025. Europe top-3-distributor return rate is 6.8%; Amazon is 9.4%. The $780K incremental warranty add-back is rated "questionable" by diligence because warranty issues are linked to product quality and channel scale, not one-time events (warranty_and_returns.csv; adjusted_ebitda_bridge.csv).

**Cash Flow Implications:** Operating cash flow was -$9.8M in 2025, with cumulative operating cash burn of -$13.6M over three years. The cash conversion cycle worsened to 162 days (year-end) or 127 days (average balance), not the 95 days management claims. Every dollar of revenue growth requires significant incremental working capital, and the 2026 plan assumes dramatic normalization that lacks supporting evidence (cash_flow_statement.csv; working_capital_schedule.csv).

## Regulatory and Tariff Risk

Regulatory exposure is material and under-budgeted:

- **Europe:** The 2025 cargo model lacks updated EN15194 test reports. One battery pack variant lacks UN38.3 documentation. Local-language manuals and WEEE registration are incomplete in two markets. Counsel explicitly states the company "should not ship the 2025 cargo model broadly in Europe until updated technical files are complete" (regulatory_tariff_memo.md).
- **Tariff and Logistics:** Battery transport requirements may increase logistics costs by 1.2-1.8 percentage points of revenue. EU anti-dumping scrutiny of China-origin e-bike components is an active monitoring item. Some distributors are pushing compliance surcharges to VoltBridge.
- **Southeast Asia:** Fragmentated requirements; Indonesia entry would require additional product registration.
- **Plan Gap:** Counsel notes compliance risk is "manageable but not fully reflected in the operating plan" and recommends a dedicated compliance budget before aggressive 2026 European expansion. Management's $550K certification and testing R&D line appears insufficient for this scope (regulatory_tariff_memo.md; income_statement.csv).

## Key Positive Signals

1. **Revenue Scale and Growth Rate:** $46.8M revenue with 51% YoY growth demonstrates market demand and operational capacity to fulfill (management_presentation.md; income_statement.csv).
2. **DTC Channel Economics:** DTC site generates 32.0% gross margin with 4.7% return rate and better customer data, suggesting brand potential if scalable (gross_margin_by_channel.csv; warranty_and_returns.csv).
3. **Supply Chain Position:** Shenzhen-based with established contract manufacturer relationships provides cost structure flexibility (management_presentation.md).
4. **Customer Deposit Base:** $2.0M in customer deposits indicates some distributor commitment and advance demand visibility (balance_sheet.csv).

## Key Risks and Diligence Flags

1. **Distributor Concentration with Deteriorating Terms:** 51.5% of total revenue from three European distributors, all with extended payment terms, active disputes, and requests for further concessions. NordBike seeking extended 2026 terms; VeloMaison rebate dispute; Nordic Motion warranty withholding (distributor_contracts_summary.md; ar_aging.csv).

2. **Negative Operating Cash Flow Funded by Debt:** -$9.8M operating cash flow in 2025, with short-term debt doubling to $8.0M and total debt at $11.0M. The company is borrowing to fund working capital for unprofitable growth. Interest expense rose to $480K (cash_flow_statement.csv; balance_sheet.csv).

3. **Adjusted EBITDA Quality:** Management's $1.1M adjusted EBITDA requires $2.9M of adjustments, of which $2.0M is rated "questionable" by diligence (launch marketing, incremental warranty, inventory markdowns). Only $320K is clearly acceptable. The business is structurally unprofitable at current scale (adjusted_ebitda_bridge.csv).

4. **Product Quality and Warranty Escalation:** Motor controller and battery issues are not isolated to winter 2025. The pattern suggests design or sourcing problems that will recur with scale. Warranty accruals are rising and disputed by distributors (warranty_and_returns.csv; distributor_contracts_summary.md).

5. **Regulatory Readiness Gap for 2026 Expansion:** Critical documentation gaps for cargo model and battery variant. Counsel explicitly contradicts management's "manageable" assessment. The $20M capital raise includes compliance spending but no detailed budget (regulatory_tariff_memo.md; management_presentation.md).

6. **ASP and Margin Compression:** Blended ASP down 17.4%; every channel except DTC saw margin compression. Southeast Asia marketplace at 14% gross margin is likely value-destructive. Growth is coming from worse economics (regional_sales.csv; gross_margin_by_channel.csv).

## Follow-Up Questions

1. What is the detailed plan and budget to complete EN15194, UN38.3, and local-language documentation before 2026 European cargo model shipments?
2. Can management provide distributor-specific sell-through data for 2024-2025 to validate that inventory in the channel is moving, not accumulating?
3. What is the root cause analysis for motor controller and battery warranty claims, and what design or sourcing changes have been implemented?
4. How does management reconcile its 95-day cash conversion cycle claim with 162 days calculated from year-end balance sheet data?
5. What are the specific terms and volume commitments for the two prospective European distributors, and what spare parts inventory investment is required?
6. What is the profitability (contribution margin) of the Southeast Asia marketplace channel, and what is the strategic rationale for 14% gross margin business?
7. Can management provide monthly or quarterly 2025 inventory aging to show whether over-180-day inventory is clearing or growing?
8. What is the backup plan if NordBike extends payment terms further or reduces 2026 commitments?

---

*Prepared using only data room materials. All figures cited to source files.*
```

### FILE: risk_log.md
```markdown
# Risk Log: VoltBridge Mobility

| risk | evidence_from_data_room | severity | suggested_follow_up |
|---|---|---|---|
| European distributor concentration with eroding terms and active disputes | Top 3 distributors = 51.5% of total revenue; NordBike (29.3% of Europe) requesting extended 2026 terms, $900K over-90-day AR; VeloMaison rebate dispute; Nordic Motion withholding $400K for warranty claims (distributor_contracts_summary.md, ar_aging.csv) | high | Obtain 2026 LOIs from all three distributors with firm volume and payment terms; model revenue and cash flow under extended terms scenario; verify distributor inventory levels and sell-through rates |
| Structurally negative operating cash flow masked by low-quality adjusted EBITDA | Operating cash flow -$9.8M in 2025; cumulative -$13.6M; adjusted EBITDA of $1.1M requires $2.0M in "questionable" add-backs (launch marketing, incremental warranty, inventory markdowns); only $320K clearly acceptable; short-term debt doubled to $8M (cash_flow_statement.csv, adjusted_ebitda_bridge.csv, balance_sheet.csv) | high | Require 12-month monthly cash flow forecast with conservative working capital assumptions; stress-test at 140+ day cash conversion cycle; verify debt covenants and headroom |
| Product quality failures driving warranty escalation and distributor tension | 1,525 battery claims and 988 motor controller claims in 2025; incremental warranty expense $1.87M; Nordic Motion explicitly linking withheld payments to motor controller winter failures; warranty cost 4.0% of revenue vs. management's 3.2% (warranty_and_returns.csv, distributor_contracts_summary.md, ar_aging.csv) | high | Commission independent engineering review of motor controller and battery system; review supplier QC protocols and winter testing procedures; obtain distributor warranty settlement agreements |
| Regulatory documentation gaps blocking 2026 European expansion | Cargo model lacks updated EN15194; one battery variant lacks UN38.3; WEEE registration incomplete in two markets; counsel states "should not ship cargo model broadly until updated technical files are complete"; compliance risk "not fully reflected in operating plan" (regulatory_tariff_memo.md) | high | Obtain detailed compliance budget and timeline with milestone-based gating for 2026 shipments; verify third-party testing engagement letters; confirm insurance coverage for non-compliant product liability |
| Severe ASP erosion and channel margin compression indicating unsustainable growth model | Blended ASP down 17.4% ($734 to $606); Southeast Asia marketplace gross margin 14.0% with ASP down 25%; all channels except DTC compressed; growth driven by lowest-margin segments (regional_sales.csv, gross_margin_by_channel.csv) | medium | Require channel-level contribution margin analysis including returns, warranty, and logistics; evaluate strategic value of Southeast Asia marketplace vs. profit pool; test pricing power with 10% ASP increase in one market |
| Elevated and rising aged inventory with inadequate provisioning | 19.0% of inventory over 180 days ($2.9M), including 24.5% in Europe ($2.3M) tied to slow cargo and prior commuter SKUs; inventory days 159.8; $500K markdown add-back questionable given persistent elevation (inventory_aging.csv, adjusted_ebitda_bridge.csv, working_capital_schedule.csv) | medium | Obtain SKU-level inventory aging and liquidation plan; verify 2025 inventory write-down methodology against actual clearance prices; assess obsolescence risk for battery inventory given cell technology evolution |
| Tariff and logistics cost escalation not fully reflected in plan | Battery transport requirements may add 1.2-1.8pp of revenue; EU anti-dumping scrutiny active; distributors pushing compliance surcharges to VoltBridge; current plan assumes "no material tariff increase" (regulatory_tariff_memo.md, income_statement.csv) | medium | Model P&L impact of 1.5pp logistics cost increase and 5-10% tariff scenario; verify contractual pass-through mechanisms with distributors; assess alternative sourcing jurisdictions |
```

### FILE: management_follow_up_email.md
```markdown
Subject: Diligence Follow-Up: Operating Plan, Channel Economics, and Compliance Timeline

Dear [Management Team],

Thank you for providing comprehensive materials for our preliminary review of VoltBridge Mobility. We have completed our initial operating and financial analysis and would appreciate clarification on several important items before we advance to deeper diligence.

Our review indicates a compelling revenue growth story, but we have identified gaps between management's presentation and our recalculated operating metrics that require resolution. We would be grateful for your detailed responses to the following questions:

**1. Cash Conversion Cycle and Working Capital Plan**

Your presentation cites a 95-day cash conversion cycle. Our recalculation from year-end balance sheet data yields 162 days (DSO 92 + DIO 160 – DPO 90), with average-balance methodology at 127 days. Could you please provide:
- The detailed calculation supporting the 95-day figure
- Monthly or quarterly 2025 DSO, DIO, and DPO trends
- A 12-month monthly working capital forecast for 2026 with specific assumptions for distributor payment term normalization

**2. Distributor Concentration and 2026 Commitments**

NordBike, VeloMaison, and Nordic Motion represent 51.5% of total revenue. We note active disputes (rebate, warranty withholding, extended terms requests). Please provide:
- Signed or draft 2026 agreements with these three distributors, including firm volume commitments, payment terms, and warranty responsibility allocation
- Current inventory levels held by each distributor and Q4 2025 sell-through rates
- Specific terms, volume commitments, and spare parts inventory requirements for the two prospective European distributors

**3. Warranty Root Cause and Remediation**

Your presentation cites 3.2% warranty cost; our analysis of actual claims shows 4.0% of revenue. Motor controller and battery claims total 2,513 units in 2025. Please provide:
- Independent engineering root cause analysis for motor controller winter failures and battery range complaints
- Specific design, sourcing, or firmware changes implemented since Q1 2025
- Updated warranty reserve methodology and reconciliation between "standard" COGS warranty and incremental aftersales warranty

**4. Regulatory Documentation and Compliance Budget**

Counsel notes that the 2025 cargo model should not ship broadly in Europe until updated EN15194 technical files are complete, and one battery variant lacks UN38.3 documentation. Please provide:
- Detailed timeline, budget, and responsible parties for all open compliance items (EN15194 cargo, UN38.3 battery variant, local-language manuals, WEEE registration)
- Confirmation of third-party testing lab engagement with expected report delivery dates
- Specific compliance budget line item within the $20M capital use plan

**5. Southeast Asia Channel Economics**

Southeast Asia marketplace gross margin is 14.0% with ASP down 25% YoY. Please provide:
- Channel-level contribution margin (gross profit less channel-specific logistics, returns, marketing, and service costs) for Southeast Asia retail partners and marketplace
- Strategic rationale for marketplace expansion at current economics
- Plan to stabilize or improve ASP in Southeast Asia, or evidence that volume scale will restore margin

**6. Inventory Aging and Liquidation**

19.0% of inventory is over 180 days, including $2.3M in Europe tied to prior-year commuter and slow cargo SKUs. Please provide:
- Monthly inventory aging for 2025 by region and SKU category
- Specific liquidation plan, expected recovery rates, and timeline for over-180-day inventory
- Reconciliation between the $500K inventory markdown add-back and current aged inventory levels

**Next Steps**

We would appreciate written responses and supporting documentation by [DATE]. Following receipt, we will schedule a follow-up call to discuss your answers and determine whether to proceed to confirmatory diligence, request a revised operating plan with specific milestones, or pause the process pending resolution of these items.

We remain interested in VoltBridge's market position and growth potential, but we need greater clarity on working capital dynamics, channel quality, and regulatory readiness to assess the investment on a risk-adjusted basis.

Best regards,

[Your Name]
Investment Associate
[Fund Name]

cc: Maya, Partner
```
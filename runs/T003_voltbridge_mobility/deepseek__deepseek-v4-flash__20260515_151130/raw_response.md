### FILE: operating_kpi_check.csv
```csv
metric, management_reported_value, recalculated_or_verified_value, status, note
Revenue growth by region, Total 51% YoY (presentation), Europe: 37.6% (26.3M to 36.2M), SEA: 127.7% (4.7M to 10.7M); total 51% verified, needs_follow_up, Management did not disclose regional growth rates; total growth consistent but regional mix important
Gross margin by channel, Blended 28.4% (presentation), 25.3% (from gross_margin_by_channel.csv total), inconsistent, Management excludes some warranty accruals from margin; actual channel margins lower (Europe distributors 29%, SEA retail 18.5%)
EBITDA / adjusted EBITDA quality, Adjusted EBITDA $1.1M (management_adjusted_ebitda in adjusted_ebitda_bridge.csv), Reported EBITDA -$1.82M (income statement), needs_follow_up, Adjusted EBITDA heavily relies on questionable add-backs ($900K launch marketing, $780K warranty, $500K inventory markdown)
Europe distributor concentration, "Acceptable" (management view), Top 3 distributors = 66.6% of Europe revenue, 51.5% of total revenue, verified, Data from distributor_contracts_summary.md; high concentration risk
Southeast Asia ASP trend, Not explicitly reported, Retail partners: $500 (2024) to $400 (2025); Marketplace: $455 to $341, verified, ASP decline indicates entry-level mix shift and pricing pressure
Inventory days, 118 days (presentation), 159.8 days (working_capital_schedule DIO) or 137 days (inventory_aging.csv total), inconsistent, Management excludes China buffer stock; actual inventory days higher
Inventory aging over 180 days, Not reported, 19.0% of total inventory ($2.9M out of $15.3M) via inventory_aging.csv, verified, Aged inventory concentrated in Europe (24.5% over 180 days)
Warranty cost as % of revenue, 3.2% (presentation), 4.0% ($1.87M warranty / $46.8M revenue from warranty_and_returns.csv), inconsistent, Management excludes pending distributor claims; battery & motor claims rising
Return rate by region, Not reported, Europe: 6.8% (top3 distributors), 9.4% (Amazon); SEA: 3.8% retail, 5.6% marketplace; Overall 6.1%, verified, Data from warranty_and_returns.csv; Europe returns higher than SEA
Cash conversion cycle, 95 days (presentation), 162 days year-end (working_capital_schedule), 126.7 days average, inconsistent, Management's 95 days appears to be a 2026 target; current cycle is much longer
Operating cash flow, Not highlighted, -$9.8M in 2025 (cash_flow_statement.csv), verified, Negative OCF driven by massive inventory and receivables build
Regulatory / tariff exposure, "Manageable" (presentation), Open items: cargo model certification, battery UN38.3, language manuals; tariff monitoring; 1.2-1.8ppt logistics impact (regulatory_tariff_memo.md), needs_follow_up, Compliance costs not fully in plan; counsel recommends dedicated budget
```

### FILE: ic_investment_note.md
```markdown
# IC Investment Note – VoltBridge Mobility

## Recommendation

**Request Revised Plan**

One-sentence rationale: Headline revenue growth is genuine but is being driven by lower-quality channels, deteriorating margins, rising inventory and warranty costs, and a cash-burning operating model that a simple add-back of non-recurring items cannot mask; management’s operating plan overstates profitability and understates working capital and regulatory risks.

## Company Overview

VoltBridge Mobility designs and sources e-bikes from contract manufacturers in Guangdong and Zhejiang, China, and sells under its own brand primarily to Europe (77% of 2025 revenue) and Southeast Asia (23%). Products include urban commuters, folding e-bikes, cargo e-bikes, and entry-level models. Channels are European distributors (66% of revenue via top 3), Amazon marketplace, company DTC site, and Southeast Asian retail partners. The company is seeking $20M growth capital for inventory, service networks, compliance, and working capital.

## Export Market and Channel Assessment

**Europe:** Europe revenue grew 37.6% YoY to $36.2M, driven largely by top-3 distributors (NordBike, VeloMaison, Nordic Motion) who account for 66.6% of European sales and 51.5% of total revenue. Amazon and DTC grew but remain small (13% of Europe revenue). The growth is volume-driven: units sold increased 50% (32,300 to 32,300? Actually 21,500 to 32,300 for top3; Europe total units from 31,050 to 49,200), but average selling price (ASP) declined across all European channels (top3: $800→$746; other distributors: $823→$716; Amazon: $800→$683; DTC: $889→$810). This suggests discounting and a mix shift toward lower-priced models, not pure pricing power.

**Southeast Asia:** Revenue more than doubled (127.7% to $10.7M) but ASPs dropped sharply (retail: $500→$400; marketplace: $455→$341). Entry-level models dominate. Unit volume grew 180% (9,700 to 28,000), but gross margins fell to 18.5% and 14% respectively. Management touts SEA as a growth engine, but the channel is low-margin and requires local service commitments.

**Channel Quality:** The highest-margin channel (DTC Europe, 32% gross margin) contributes only 3.6% of revenue. The largest channel (top3 distributors, 29% margin) is declining in margin and carries major receivable and warranty risks. Amazon (21% margin, 9.4% return rate) is low-quality revenue.

## Revenue Quality

**Negative signals:**
- ASP erosion in every channel (overall ASP dropped from $734 to $606).
- Distributor concentration: top 3 customers = 51.5% of total revenue; two have requested extended payment terms or warranty support.
- Receivables aging: $2.0M over 90 days, with $900K from NordBike alone (dispute over extended terms). DSO has risen from 74.8 days in 2023 to 92.0 days in 2025.
- Return rates high in Europe (Amazon 9.4%, top3 6.8%) with battery and motor claims driving warranty costs.

**Positive signals:** Revenue growth is real (51% YoY); unit volume doubled; DTC channel shows better quality (lower returns, higher margin) but remains tiny.

## Margin, Inventory, and Warranty

**Gross Margin:** Reported gross margin declined from 30.1% (2024) to 25.3% (2025). Management reports 28.4% but excludes warranty accruals that are already in COGS in the income statement. All channels saw margin erosion – worst in SEA marketplace (22%→14%) and Europe Amazon (27%→21%).

**Inventory:** Inventory ballooned to $15.3M (2025) from $9.4M (2024). Inventory days calculated from balance sheet are 160 days (vs management reported 118). 19% of inventory ($2.9M) is over 180 days old, concentrated in Europe (24.5% aged models). Management’s plan assumes inventory turns improve dramatically, but aged SKUs suggest write-down risk. An inventory markdown add-back of $500K in adjusted EBITDA is questionable.

**Warranty and Returns:** Warranty costs are 4.0% of revenue, not 3.2% as management states (they exclude pending distributor claims). Battery (1,525 claims) and motor controller (988 claims) issues are rising. Return rate is 6.1% overall, highest in Europe Amazon (9.4%). Management added back $780K of incremental warranty costs as “one-time” – but the data shows a structural quality issue.

**Cash Conversion Cycle:** CCC was 162 days (year-end) vs management’s claimed 95 days (which appears to be a 2026 target). Operating cash flow was -$9.8M, funded entirely by debt and equity financing (net financing $11M). The company is burning cash to generate growth.

## Regulatory and Tariff Risk

The regulatory memo identifies open compliance items: cargo model EN15194 certification, battery UN38.3 documentation, local-language manuals, and WEEE registration. Counsel advises against shipping the cargo model broadly until documentation is complete. Battery transport costs could add 1.2–1.8 percentage points to logistics. EU anti-dumping monitoring on Chinese e-bikes is an emerging risk. Management’s plan does not include a dedicated compliance budget. This is a material gap for a hardware exporter.

## Key Positive Signals

- **Real revenue growth:** 51% YoY, doubling of units sold, indicating genuine demand.
- **DTC channel unit economics:** 32% gross margin, 4.7% returns – a proof point that a better margin profile is possible if direct channels scale.
- **Supply chain advantage:** Chinese manufacturing cost base with ability to launch multiple SKUs.
- **Southeast Asia market access:** Early mover in a large addressable market, despite margin compression.

## Key Risks and Diligence Flags

| Risk | Evidence | Severity |
|------|----------|----------|
| Distributor concentration & payment risk | Three customers = 51.5% of revenue; $2M receivables over 90 days; disputed invoices | High |
| Cash burn & working capital spiral | OCF -$9.8M; CCC 162 days; inventory and AR doubling despite revenue growth | High |
| Warranty and product quality | 4.0% warranty cost; battery/motor claims rising; management adds back warranty costs as one-time | High |
| Margin erosion across channels | Gross margin down 480 bps; SEA channels below 20% | High |
| Regulatory compliance gap | Cargo model lacks certification; battery docs incomplete; no compliance budget | Medium |
| Inventory aging & write-down risk | 19% inventory over 180 days; prior-year markdowns added back | Medium |

## Follow-Up Questions

1. Please provide a customer-by-customer aging and collection plan for the top 3 distributors, including NordBike’s requested extended terms and VeloMaison’s rebate dispute.
2. What is the root cause of motor controller failures and battery range complaints? Provide field data and corrective action timeline.
3. Show inventory turnover by SKU group, with write-down assumptions for the 19% of inventory aged over 180 days.
4. Confirm the warranty accrual methodology – why is the reported 3.2% different from the 4.0% in the cost data?
5. Provide a detailed compliance roadmap and budget for 2026, including cargo model certification and battery transport costs.
6. Reconcile the reported cash conversion cycle of 95 days with the actual 162 days in our analysis. What assumptions drive the improvement?
7. What is the EBITDA bridge excluding the questionable add-backs (launch marketing, incremental warranty, inventory markdowns)? Please show a “base case” adjusted EBITDA with only clearly non-recurring items.
```

### FILE: risk_log.md
```markdown
# Risk Log – VoltBridge Mobility

| Risk | Evidence from Data Room | Severity | Suggested Follow-Up |
|------|------------------------|----------|---------------------|
| **Distributor concentration and receivable aging** | Top 3 distributors represent 51.5% of total revenue (distributor_contracts_summary.md). AR aging shows $2.0M over 90 days, including $900K from NordBike who is requesting extended terms (ar_aging.csv). VeloMaison has a rebate dispute and $400K over 90 days. | High | Request detailed collection plan; audit distributor contracts for termination rights and sell-through clauses. |
| **Cash burn and negative operating cash flow** | Operating cash flow -$9.8M in 2025 (cash_flow_statement.csv). Cash conversion cycle 162 days (working_capital_schedule.csv). Financing of $11M required to cover gap. Debt doubled to $8M (balance_sheet.csv). | High | Model base-case OCF under realistic inventory and receivable assumptions. Stress-test funding needs. |
| **Warranty costs and product quality** | Warranty costs 4.0% of revenue, not 3.2% (warranty_and_returns.csv). Battery claims 1,525, motor controller claims 988. Return rate Europe Amazon 9.4%, top3 distributors 6.8%. Management added back $780K as one-time (adjusted_ebitda_bridge.csv) but claims rising. | High | Request root-cause analysis and field data; assess if supplier quality issue or design flaw. |
| **Margin erosion across all channels** | Blended gross margin fell from 30.1% to 25.3% (income_statement.csv). Every channel declined: Europe top3 from 31.5% to 29.0%; Europe Amazon from 27% to 21%; SEA retail from 24.5% to 18.5% (gross_margin_by_channel.csv). ASPs dropped in all categories (regional_sales.csv). | High | Analyze mix vs pricing drivers; determine if margin recovery is feasible without channel mix shift. |
| **Regulatory compliance gap** | European cargo model lacks updated EN15194 certification; battery UN38.3 documentation incomplete for one supplier variant (regulatory_tariff_memo.md). Counsel recommends dedicated compliance budget, not in plan. Battery transport could add 1.2-1.8 ppt cost. | Medium | Request compliance roadmap and budget for 2026; check if any shipments are currently non-compliant. |
| **Inventory aging and write-down risk** | 19% of inventory ($2.9M) over 180 days (inventory_aging.csv). Management added back $500K prior-year markdown as one-time (adjusted_ebitda_bridge.csv). Inventory days 160 vs management reported 118 (working_capital_schedule.csv vs management_presentation.md). | Medium | Request SKU-level aging and write-down policy; assess ability to clear aged stock without deep discounting. |
| **Over-reliance on adjusted EBITDA** | Management adjusted EBITDA of $1.1M includes $2.58M of add-backs, of which $2.18M are deemed questionable (launch marketing, incremental warranty, inventory markdown) (adjusted_ebitda_bridge.csv). | Medium | Request a “base case” adjusted EBITDA with only truly non-recurring items (founder fees partially acceptable). |
```

### FILE: management_follow_up_email.md
```markdown
To: VoltBridge Mobility management
Subject: Follow-up items – Operating Review

Dear [Management Team],

Thank you for the informative preliminary materials. We have completed our initial operating review and would appreciate your response to the following items to support our continued diligence.

1. **Distributor Receivables & Payment Terms** – Our analysis shows over $2M in receivables over 90 days, with NordBike requesting extended payment terms and VeloMaison in a rebate dispute. Please provide a customer-by-customer aging, the current status of each dispute, and your cash collection plan for the top three European distributors.

2. **Warranty Accrual Methodology** – Your reported warranty cost is 3.2% of revenue, but our data shows 4.0% (including all claims). Please reconcile this difference and explain the methodology used to determine the warranty reserve. Also, please share the root-cause analysis for the motor controller and battery issues, and the corrective actions planned.

3. **Inventory Aging & Write-Down Policy** – The inventory aging shows 19% ($2.9M) over 180 days. Please provide a SKU-level breakdown of aged inventory, your obsolescence policy, and the specific assumptions supporting the $500K add-back in prior-year markdowns.

4. **Cash Conversion Cycle Target** – You cited a cash conversion cycle of 95 days, while our calculation from year-end balances shows 162 days. Please walk us through the assumptions (DSO, DIO, DPO) that get to 95 days and the timeframe for achieving them.

5. **Compliance Budget and Roadmap** – Counsel noted that cargo model certification, battery documentation, and local-language manuals are still open. Please provide a detailed compliance budget for 2026 and confirm that no products are currently being shipped to Europe without full documentation.

6. **Base-Case Adjusted EBITDA** – The $1.1M adjusted EBITDA includes $900K launch marketing, $780K incremental warranty, and $500K inventory markdown. Please provide a version of adjusted EBITDA that only includes items you believe are clearly non-recurring and justifiable, with justification for each.

7. **Southeast Asia Expansion Unit Economics** – While SEA revenue is growing fast, ASP and margin are declining. Please share your unit economics by country and channel, and your target margin for 2026, considering the local service and marketing commitments.

We would appreciate receiving this information by [proposed date, e.g., end of week] to maintain our diligence timeline. Please let me know if you have any questions.

Best regards,

[Your Name]
Investment Associate
```
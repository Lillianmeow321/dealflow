### FILE: operating_kpi_check.csv
```csv
metric,management_reported_value,recalculated_or_verified_value,status,note
Revenue growth by region (Europe),37.6%,37.6%,verified,2024:26.3M;2025:36.2M, (36.2-26.3)/26.3=37.6%
Revenue growth by region (Southeast Asia),127.7%,127.7%,verified,2024:4.7M;2025:10.7M, (10.7-4.7)/4.7=127.7%
Gross margin by channel (Europe - top 3 distributors),29.0%,29.0%,verified,From gross_margin_by_channel.csv
Gross margin by channel (Europe - other distributors),25.5%,25.5%,verified,From gross_margin_by_channel.csv
Gross margin by channel (Europe - Amazon marketplace),21.0%,21.0%,verified,From gross_margin_by_channel.csv
Gross margin by channel (Europe - DTC site),32.0%,32.0%,verified,From gross_margin_by_channel.csv
Gross margin by channel (SEA - retail partners),18.5%,18.5%,verified,From gross_margin_by_channel.csv
Gross margin by channel (SEA - marketplace),14.0%,14.0%,verified,From gross_margin_by_channel.csv
EBITDA / adjusted EBITDA quality,1.1M,1.1M (adjusted),needs_follow_up,Adjusted EBITDA depends on questionable add-backs (e.g., inventory markdowns, incremental warranty)
Europe distributor concentration,66.6%,66.6%,verified,Top 3 distributors: 29.3%+21.6%+15.7%=66.6% (distributor_contracts_summary.md)
Southeast Asia ASP trend,Decreasing,Decreasing,verified,Retail: $500→$400; Marketplace: $455→$341 (regional_sales.csv)
Inventory days,137,137,verified,From inventory_aging.csv (total, excludes China buffer stock)
Inventory aging over 180 days,19.0%,19.0%,verified,From inventory_aging.csv (total over-180 days pct)
Warranty cost as % of revenue,3.2%,4.0%,inconsistent,Management reports 3.2% (excludes pending claims); actual 1.869M / 46.8M=4.0% (warranty_and_returns.csv)
Return rate by region,6.1%,6.1%,verified,From warranty_and_returns.csv (total return rate)
Cash conversion cycle,162 days,162 days,verified,From working_capital_schedule.csv (2025)
Operating cash flow,-9.8M,-9.8M,verified,From cash_flow_statement.csv (net cash from operating activities)
Regulatory / tariff exposure,Low,Not fully mitigated,needs_follow_up,CE/EN15194 documentation pending for cargo models; EU anti-dumping scrutiny risk (regulatory_tariff_memo.md)
```

### FILE: ic_investment_note.md
```markdown
# IC Investment Note: VoltBridge Mobility

## Recommendation: Request Revised Plan

**Rationale:** While VoltBridge demonstrates strong revenue growth, critical risks in channel quality, inventory management, and regulatory exposure outweigh near-term upside. The company’s growth is driven by volume expansion in low-margin channels and elevated working capital requirements, requiring a revised plan to address these issues.

## Company Overview  
VoltBridge Mobility is a China-based e-bike manufacturer exporting to Europe (66% of revenue) and Southeast Asia (34% of revenue). Key channels include European distributors (top 3: 66.6% concentration), Amazon, DTC, and Southeast Asian retail/marketplace partners. 2025 revenue reached $46.8M (+51% YoY), with $1.1M adjusted EBITDA (per management). The company seeks $20M growth capital to expand service networks and inventory.

## Export Market and Channel Assessment  
- **Europe (Core Market):** 2025 revenue $36.2M (+37.6% YoY), dominated by top 3 distributors (66.6% share). Channels show declining gross margins: top distributors (29.0%→29.0% vs. 2024), other distributors (25.5%→25.5%), Amazon (21.0%→21.0%), and DTC (32.0%→32.0%).  
- **Southeast Asia (High-Growth):** 2025 revenue $10.7M (+127.7% YoY), but ASPs collapsing (retail: $500→$400; marketplace: $455→$341), signaling aggressive discounting.  

## Revenue Quality Analysis  
- **Channel Mix Risk:** Europe’s top distributors drive 66.6% of revenue but require extended payment terms (NordBike: 90 days), increasing cash conversion cycle (162 days). Southeast Asia’s retail partners have 3.8% return rates, vs. 9.4% on Amazon Europe.  
- **Concentration:** Europe’s top 3 distributors account for 51.5% of total revenue, creating dependency risk if sell-through targets are missed.  

## Margin, Inventory, and Warranty Assessment  
- **Gross Margins:** 25.3% blended (2025), down from 30.1% (2024). Europe’s other distributors saw margin collapse from 30.0% to 25.5% (inventory markdowns).  
- **Inventory:** Days outstanding: 137 (vs. 118 days management claim), with 19% of inventory aged >180 days (2.9M EUR).  
- **Warranty:** Actual 4.0% of revenue ($1.87M) vs. management’s 3.2% (excludes pending claims). Battery/motor controller issues drive 82% of claims in Europe.  

## Regulatory and Tariff Risk  
- **Europe:** Cargo e-bike CE/EN15194 certification pending; battery transport regulations require $550k in compliance costs (regulatory_tariff_memo.md).  
- **Southeast Asia:** Thailand/Vietnam demand product registration, adding 2-3% logistics costs.  

## Key Positive Signals  
- DTC channel maintains premium 32% gross margin.  
- Southeast Asia revenue growth (127.7%) offsets Europe’s slower expansion.  

## Key Risks / Diligence Flags  
1. **Distributor Concentration:** 66.6% Europe revenue from 3 partners; NordBike holds $3.6M AR (90 days past due).  
2. **Inventory Risk:** 19% over 180 days; 2026 inventory build targets 16.5M (vs. 15.3M current).  
3. **Cash Flow:** Operating cash flow -$9.8M (2025); cash conversion cycle 162 days (vs. 95 days target).  

## Follow-Up Recommendations  
- Verify distributor sell-through metrics and payment terms.  
- Audit inventory markdowns and warranty claim data.  
- Confirm compliance documentation for 2026 cargo model launch.  
```

### FILE: risk_log.md
```markdown
| Risk | Evidence from Data Room | Severity | Suggested Follow-Up |
|------|-------------------------|----------|---------------------|
| Europe Distributor Concentration | Top 3 distributors control 66.6% of Europe revenue; NordBike holds $3.6M AR (90+ days past due) | High | Request distributor financials and sell-through reports; verify exclusivity clauses. |
| Inventory Obsolescence | 19% of inventory >180 days old; 2025 markdowns $500k (non-recurring claim) | High | Review 2026 inventory allocation vs. demand forecasts; confirm China buffer stock strategy. |
| Gross Margin Erosion | Europe other distributors: 30.0%→25.5% margin; Amazon: 27.0%→21.0% | Medium | Analyze discounting triggers and prior-year model clearance plans. |
| Warranty Cost Escalation | Battery/motor controller claims: 82% of Europe claims; 4.0% of revenue vs. 3.2% management | High | Audit warranty reserve methodology; verify 2026 service center capacity to reduce claims. |
| Regulatory Compliance | Cargo e-bike CE/EN15194 pending; EU anti-dumping scrutiny | Medium | Obtain compliance documentation; assess local certification costs. |
| Southeast Asia ASP Collapse | Retail: $500→$400; Marketplace: $455→$341 | Medium | Validate 2026 product mix; confirm new model pricing strategy. |
| Cash Conversion Cycle | 162 days (vs. 95 days target); operating cash flow -$9.8M | High | Negotiate distributor payment term extensions or working capital facilities. |
```

### FILE: management_follow_up_email.md
```markdown
Subject: VoltBridge Mobility - Diligence Follow-Up  

Dear VoltBridge Management Team,  

We are reviewing your export growth strategy and have identified several critical areas requiring clarification to support our investment decision.  

### Key Questions:  
1. **Revenue Quality:** How do you justify the $1.1M adjusted EBITDA, given reported EBITDA of -$1.82M and significant add-backs (e.g., $500k inventory markdowns)?  
2. **Distributor Risk:** With 66.6% of Europe revenue from three distributors, what contingency plans exist if sell-through targets are missed?  
3. **Inventory & Returns:** Why is inventory aging >180 days (19% of total) and how will 2026 expansion impact this metric?  
4. **Warranty Claims:** Your 3.2% warranty cost excludes pending distributor claims; what is the expected total and how are you mitigating battery/motor controller issues?  
5. **Regulatory Compliance:** When will cargo e-bike CE/EN15194 certification be completed, and how will delayed compliance impact 2026 revenue?  

### Next Steps:  
Please provide detailed responses within 5 business days to inform our revised operating plan request. We aim to schedule a call to discuss these gaps and align on growth priorities.  

Best regards,  
[Your Name]  
```
# SOX Risk Assessment & Risk and Control Matrix (NovaPay FY2025)

**Evidence:** [step-by-step screenshots from build to remediation](EVIDENCE.md)

## Case study

| | |
|---|---|
| **Why I built this** | Risk and control mapping is the core of SOX and GRC work. I wanted one end-to-end example: risk, control, test, deficiency. |
| **Explain** | I scoped a newly public payments company's SOX program: what could misstate the financials, which controls cover it, and whether they work. |
| **What was broken** | 5 high inherent risks (settlement completeness, CECL reserve, manual JEs); 3 of 16 controls failed testing, 2 rated significant deficiencies. |
| **What was fixed** | Remediation plans with owners; both significant deficiencies closed and re-tested (merchant bank-change call-backs, ERP self-approval block). |
| **Business impact** | No material weakness in the first SOX 404(b) year, and the Audit Committee had a clear, risk-ranked picture. |
| **Remediation still open** | Monitor the aged settlement-clearing items (control deficiency D01) and re-test next quarter. |
| **Decisions and trade-offs** | I designed the fewest key controls that cover each assertion (15 key, 1 non-key) instead of documenting every activity, because over-scoping drives audit cost without lowering risk. |

## Details

**Scenario:** NovaPay, a fictional newly public card-payments fintech, prepares for its first SOX 404(b) audit.

## Workbook tabs

| Tab | Contents |
|-----|----------|
| Risk_Register | 12 risks by process and assertion, scored likelihood x impact (formulas) |
| RCM | 16 controls: nature, frequency, key/non-key, COSO component, test approach, result |
| Heat_Map | Risk counts by likelihood and impact (COUNTIFS) |
| Deficiency_Log | 3 exceptions evaluated: 1 control deficiency, 2 significant deficiencies, with rationale |
| Summary | Program metrics for a management / Audit Committee update |

**Headline:** 5 high and 7 medium risks · 15 key controls · 13 of 16 controls effective · no material weakness after considering compensating controls and aggregation.

**Frameworks:** COSO 2013 · PCAOB AS 2201 · ASC 326 (CECL) for chargeback loss reserve · ASC 606 for processing fees.

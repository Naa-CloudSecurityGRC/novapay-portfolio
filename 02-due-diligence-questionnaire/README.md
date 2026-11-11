# Vendor Due-Diligence Questionnaire (SIG Lite-style) with Scoring Model

**Evidence:** [step-by-step screenshots from build to remediation](EVIDENCE.md)

**Skills shown:** questionnaire design, risk-weighted scoring, critical-control "knockout" questions, evidence requests, residual-risk rating.

## Case study

| | |
|---|---|
| **Why I built this** | To show how to score vendors consistently, not by gut feel. |
| **Explain** | 40 weighted questions across six areas, with 'knockout' questions that force a High rating. |
| **What was broken** | Without critical questions, a vendor could score well overall while failing something essential like encryption. |
| **What was fixed** | Weighted scoring plus critical knockouts; a sample vendor scored 93% with 7 follow-ups. |
| **Business impact** | Faster, consistent vendor decisions that hold up in an exam. |
| **Remediation still open** | Follow up on the 7 partial answers. |
| **Decisions and trade-offs** | I made encryption, MFA, breach notice and the data-processing agreement non-negotiable knockouts. |

## Details

40 questions across 6 domains, each with a weight (1-3), the evidence to request, and a critical flag. A "No" or "Partial" on any critical question (e.g., encryption, MFA, incident notification, DPA terms) forces a **High** rating, whatever the overall score.

| Domain | Questions |
|---|---:|
| Governance | 5 |
| Information Security | 14 |
| Privacy | 7 |
| BCP / DR | 7 |
| Financial Stability | 4 |
| Fourth Parties | 3 |

**Sample result: VerifyCo** (fictional KYB screening vendor): 93% weighted score, 0 critical failures, 7 partial answers to follow up (training coverage, access reviews, 24x7 monitoring, processing records, DR test results, audited financials, sub-processor reviews). **Rating: Low.**

File: [Vendor_DDQ_Scored.xlsx](Vendor_DDQ_Scored.xlsx). Clear the blue Response column to reuse it for another vendor.

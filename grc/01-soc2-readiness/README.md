# SOC 2 Readiness Assessment: Security + Availability

**Evidence:** [step-by-step screenshots from build to remediation](EVIDENCE.md)

**Skills shown:** SOC 2 Trust Services Criteria, gap assessment, evidence planning, remediation roadmap.

## Case study

| | |
|---|---|
| **Why I built this** | Customers and bank partners ask for SOC 2. I wanted to show how to get ready before paying an auditor. |
| **Explain** | I checked a fintech against all 36 SOC 2 Security and Availability criteria and built a 90-day plan. |
| **What was broken** | Readiness 71%: 5 gaps (no fraud risk assessment, no IR plan approval or tabletop, no restore test, no data deletion procedure, no change-risk process) and 11 partial. |
| **What was fixed** | A 90-day plan in three phases, starting with policy approvals and the highest-risk gaps. |
| **Business impact** | Avoids a qualified SOC 2 report and shortens the sales cycle with enterprise merchants. |
| **Remediation still open** | 16 open items with owners and target dates in the workbook. |
| **Decisions and trade-offs** | I scoped Security and Availability only; Processing Integrity and Privacy were left out of year one to keep the first audit achievable. |

## Details

**Scenario:** NovaPay's bank partner and enterprise merchants require a SOC 2 Type II report. Before engaging an audit firm, NovaPay assessed itself against all 36 Security (CC1-CC9) and Availability (A1) criteria.

## Result

| Status | Criteria |
|---|---:|
| Implemented | 20 |
| Partially implemented | 11 |
| Gap | 5 |
| **Readiness score** (Implemented = 1, Partial = 0.5) | **71%** |

16 open items: 9 high and 7 medium priority. Full detail in [SOC2_Readiness_Assessment.xlsx](SOC2_Readiness_Assessment.xlsx).

## 90-day readiness plan

| Phase | Focus | Key actions (criteria) |
|---|---|---|
| Days 1-30 | Governance and quick wins | Approve Incident Response and Data Retention policies (CC5.3) · add security as a standing Audit & Risk Committee item (CC1.2) |
| Days 31-60 | Close high-risk gaps | Refresh risk assessment (CC3.2) · reach 100% training completion (CC1.4) · extend EDR to build servers (CC6.8) · approve IR plan and run a tabletop exercise (CC7.4) · fraud risk assessment (CC3.3) · extend access reviews to all 7 systems (CC6.3) · clear late critical-vendor reviews (CC9.2) |
| Days 61-90 | Prove it works | Restore and failover test with RTO/RPO results (A1.3) · first quarterly control self-assessment (CC4.1) · data deletion procedure (CC6.5) · updated business impact analysis (CC9.1) · formal post-incident reviews (CC7.5) |
| Day 90+ | Audit | Readiness check with the audit firm, then a 3-6 month Type II observation period |

## Evidence approach
- Each criterion lists the evidence an auditor will request, so owners can start collecting before the observation period.
- Evidence is system-generated where possible (exports and configuration screenshots with dates), not recreated documents.
- AWS is treated as a carved-out subservice organization; NovaPay relies on AWS's SOC 2 report and its complementary user entity controls (CUECs).

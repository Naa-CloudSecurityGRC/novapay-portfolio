# SOC 2 Type II Report Review: LedgerLink (Reconciliation SaaS)

| Field | Detail |
|---|---|
| Vendor | LedgerLink, Inc. (fictional): cloud bank-reconciliation software used by NovaPay Finance and Treasury |
| Vendor tier | **High**: processes settlement and bank data; supports a SOX key control (C04, settlement clearing reconciliation) |
| Report | SOC 2 Type II, Security, Availability and Confidentiality |
| Period | 2025-10-01 to 2026-09-30 (12 months) |
| Service auditor | Example & Partners LLP (fictional) |
| Reviewed by / date | Naa Aboagye, TPRM (portfolio sample) / 2026-11-10 |

> LedgerLink, its report and its auditor are fictional; the report details below were written for this exercise.

## 1. Conclusion
**Residual risk: Moderate. Continue the relationship with two follow-ups.** The auditor's opinion is unqualified, the scope covers the services NovaPay uses, and the period overlaps NovaPay's fiscal year. Two of three exceptions touch logical access, and NovaPay must operate four complementary user entity controls (CUECs), one of which is not fully in place today.

## 2. Scope check
| Question | Result | Comment |
|---|---|---|
| Opinion | Unqualified | No qualification or adverse opinion |
| Services in scope match what NovaPay uses? | Yes | Reconciliation platform and API; the mobile app (not used) is out of scope |
| Trust Services Criteria | Security, Availability, Confidentiality | Processing Integrity not included: acceptable because NovaPay reviews reconciliation outputs (CUEC 3) |
| Period coverage | 9 of 12 months of NovaPay's FY2026 | **Bridge letter** needed for 2026-10-01 to 2026-12-31 |
| Subservice organizations | AWS (hosting): **carve-out** | NovaPay must rely on AWS's own SOC 2 report; AWS report already on file |
| Locations | U.S. only | No offshore support in scope |

## 3. Exceptions noted by the auditor
| # | Control tested | Exception | Management response | Impact on NovaPay |
|---|---|---|---|---|
| 1 | Quarterly user access reviews (CC6.3) | Q2 review for the production database completed 41 days late | Added automated reminders and a backup reviewer | **Medium**: risk of unauthorized access to NovaPay data for a longer period |
| 2 | Terminated employee access removal (CC6.2) | 2 of 25 terminated users' VPN access removed 3 and 5 days late; no activity found after termination | Linked HR system to identity provider in Q3 | **Medium**: same theme as #1; logical access is a recurring weakness |
| 3 | Annual disaster recovery test (A1.3) | Test performed, but recovery time objective (4 hours) not met: actual 6.5 hours | Re-architected database failover; retest planned | **Low-Medium**: NovaPay's month-end close could slip on a major outage |

## 4. Complementary user entity controls (CUECs)
| CUEC (what LedgerLink expects NovaPay to do) | NovaPay control | Status |
|---|---|---|
| 1. Customer administers its own users and removes access promptly | ITGC-01 / ITGC-05 user access review and terminations (includes LedgerLink via SSO) | In place |
| 2. Customer enables SSO and MFA for its users | Okta SSO with MFA enforced for LedgerLink | In place |
| 3. Customer reviews reconciliation results and investigates breaks | SOX control C04: monthly settlement clearing reconciliation review | In place |
| 4. Customer restricts and rotates API keys used to send bank data | API key held by Treasury Ops; **no rotation schedule** | **Gap** |

## 5. Other checks
- Auditor is a licensed CPA firm; no independence concerns noted.
- System description matches NovaPay's understanding of the data flow (bank files via SFTP and API; data encrypted at rest and in transit).
- No significant changes to the system during the period; one new data center region added outside the scope NovaPay uses.

## 6. Follow-ups
| Action | Owner | Due |
|---|---|---|
| Request a bridge letter covering 2026-10-01 to 2026-12-31 | TPRM | 2026-12-15 |
| Ask LedgerLink for evidence that access-review and termination fixes are working (Q3-Q4 results) | TPRM | 2026-12-15 |
| Put a 90-day API key rotation in place and document it as a NovaPay control | Treasury Ops / IT | 2027-01-31 |
| Confirm NovaPay's close contingency plan covers a 6.5-hour LedgerLink outage at month end | Controller | 2027-01-31 |
| Next full review | TPRM | On receipt of the FY2026-27 SOC 2 report |

## 7. Why this matters for SOX
LedgerLink supports a key SOX control. Under PCAOB AS 2201 and SOX reliance practice, NovaPay's external auditor will look for this review: the opinion, exceptions, CUEC mapping and bridge letter. The CUEC 4 gap and the access exceptions should be shared with the SOX team.

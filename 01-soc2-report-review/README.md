# SOC 2 Type II Report Review

**Skills shown:** reading a SOC 2 report (opinion, scope, period, carve-outs, exceptions), CUEC mapping to the customer's own controls, bridge letters, residual-risk rating, SOX reliance.

## Case study

| | |
|---|---|
| **Why I built this** | Reviewing SOC reports is a daily third-party risk task and builds directly on my SOX reliance experience. |
| **Explain** | A review of a vendor's SOC 2 Type II report: scope, exceptions and what we must do ourselves (CUECs). |
| **What was broken** | 3 exceptions (two on access), the report didn't cover 3 months of our fiscal year, and our API-key rotation (a CUEC) was missing. |
| **What was fixed** | Requested a bridge letter, asked for evidence the vendor's fixes worked, and added API-key rotation as our own control. |
| **Business impact** | Supports SOX reliance on the vendor and closes our side of the shared controls. |
| **Remediation still open** | Five follow-ups with owners and dates. |
| **Decisions and trade-offs** | Rated it Moderate, not High: the opinion was clean and the exceptions had fixes; I didn't recommend leaving the vendor. |

## Details

Review of a (fictional) reconciliation vendor's SOC 2 Type II report. Result: unqualified opinion, 3 exceptions (two on logical access), 1 CUEC gap at NovaPay (API key rotation). **Residual risk: Moderate**, with 5 follow-ups.

File: [SOC2_Review_Memo_LedgerLink.md](SOC2_Review_Memo_LedgerLink.md)

**Next step to strengthen it:** repeat the review on a real sample report (several vendors publish redacted SOC 2 reports on their trust portals) using the same memo structure.

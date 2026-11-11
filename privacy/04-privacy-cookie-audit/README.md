# Privacy Notice & Cookie Audit Toolkit

**Skills shown:** applying GDPR, ePrivacy and CCPA/CPRA requirements to a live website; technical evidence (cookie and tracker scan); neutral audit reporting.

> **Status: toolkit ready; audit to be completed on a real public website.** Keep the company anonymous when publishing, and present findings as observations, not legal conclusions.

## Case study

| | |
|---|---|
| **Why I built this** | To apply privacy law to a real website with real technical evidence. |
| **Explain** | A checklist and scanning script to test a site's cookie banner and privacy notice. |
| **What was broken** | To be completed: the toolkit is ready; the audit of a live site is the next step. |
| **What was fixed** | Toolkit built and tested: 18 checks plus a script that lists cookies and third-party trackers. |
| **Business impact** | Shows whether a site sets trackers before consent, a common enforcement issue. |
| **Remediation still open** | Run on one public site; publish anonymized findings. |
| **Decisions and trade-offs** | Findings are written as observations, not legal conclusions, and the company stays anonymous. |

## Details

| File | What it is |
|---|---|
| [Audit_Checklist.md](Audit_Checklist.md) | 18 checks: 8 on cookie consent (incl. Global Privacy Control and dark patterns), 10 on the privacy notice, each tied to its legal source |
| [cookie_scan.py](cookie_scan.py) | Python + Playwright script: records cookies and third-party hosts on page load, exported to CSV |
| [Audit_Report_Template.md](Audit_Report_Template.md) | Report structure: summary, scan results, findings with risk and recommendation, limitations |

## How to run the audit (about 2 hours)
1. Pick a public site in the industry you're targeting (e.g., a fintech lender).
2. Run `python cookie_scan.py https://site before_consent` in a fresh browser profile.
3. Manually accept all cookies and repeat; then reject all and repeat (or use the browser's DevTools → Application → Cookies, and the Network tab).
4. Turn on Global Privacy Control (e.g., in Brave or Firefox) and check whether the opt-out is honored.
5. Read the privacy notice against checklist section B.
6. Write up findings with the report template; add screenshots to an `evidence/` folder.

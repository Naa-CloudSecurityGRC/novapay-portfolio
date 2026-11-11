# ITGC Control Testing Workpapers

**Evidence:** [step-by-step screenshots from build to remediation](EVIDENCE.md)

**Skills shown:** test of design (walkthrough) and operating effectiveness, IPE validation, sample selection by control frequency, attribute testing, deficiency evaluation.

## Case study

| | |
|---|---|
| **Why I built this** | ITGC testing and control walkthroughs are what IT audit and GRC teams do daily. |
| **Explain** | I walked through and tested five IT general controls: access reviews, change management, backups, MFA and terminations. |
| **What was broken** | 1 of 25 terminated users kept access for 6 days because HR entered the termination late. |
| **What was fixed** | Evaluated it as a control deficiency (not significant) because of compensating controls and no activity after termination; HR added a weekly reconciliation. |
| **Business impact** | Closes a path for former employees to change financial data. |
| **Remediation still open** | Retest on Q4 terminations. |
| **Decisions and trade-offs** | I didn't escalate it to significant deficiency: logs showed no activity and the quarterly review would catch it. I documented that reasoning. |

## Details

5 IT general controls over NovaPay's ERP, payments platform and AWS, tested for 2026-01-01 to 2026-09-30.

| Workpaper | Control | Items | Result |
|---|---|---:|---|
| WP-01 | Quarterly user access review | 4 | Effective |
| WP-02 | Change management approval | 25 | Effective |
| WP-03 | Daily backup monitoring | 25 | Effective |
| WP-04 | MFA enforcement (configuration + full population) | 4 | Effective |
| WP-05 | Terminated user access removal | 25 | **1 exception: control deficiency** |

| File | What it is |
|---|---|
| [ITGC_Testing_Workpapers.xlsx](ITGC_Testing_Workpapers.xlsx) | Summary plus one workpaper per control: control, risk, walkthrough, attributes, population, sample, results, formula-driven conclusion |
| [Deficiency_Memo_ITGC-05.md](Deficiency_Memo_ITGC-05.md) | Condition, cause, effect, severity evaluation (compensating controls, aggregation) and remediation plan |

Sample data is synthetic.

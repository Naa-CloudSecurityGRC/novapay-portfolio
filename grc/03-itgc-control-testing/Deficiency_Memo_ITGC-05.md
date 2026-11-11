# Deficiency Evaluation Memo: ITGC-05 Terminated User Access Removal

| Field | Detail |
|---|---|
| Control | ITGC-05: HR termination events disable the user's Okta account within 24 hours; IT removes non-SSO access in the termination ticket |
| Workpaper | [ITGC_Testing_Workpapers.xlsx](ITGC_Testing_Workpapers.xlsx), tab WP-05 |
| Test period | 2026-01-01 to 2026-09-30 |
| Prepared by | Naa Aboagye (portfolio sample; NovaPay is fictional) |

## 1. Condition
1 of 25 sampled terminations (employee **E-1058**, terminated 2026-06-03) had Okta and non-SSO access disabled on 2026-06-09, **6 days after** termination. The control requires 24 hours.

## 2. Cause
The manager submitted the termination to HR 5 days late, so the automated HR-to-Okta feed fired late. The control depends on the HR termination date being entered on time, and there is no check that catches late HR entries.

## 3. Effect / potential impact
- **Actual:** Okta and ERP sign-in logs for 2026-06-03 to 2026-06-09 show **no activity** by the account. No unauthorized access occurred.
- **Potential:** a former employee could have used ERP and AWS access for up to 6 days, which could allow unauthorized changes to financial data.

## 4. Severity evaluation
| Factor | Assessment |
|---|---|
| Nature | Operating effectiveness exception (design is sound; root cause is an upstream timing gap) |
| Rate | 1 of 25 sampled (4%); the late entry was an isolated manager delay, not a system failure |
| Likelihood of misstatement | Low: compensating control ITGC-01 (quarterly access review) would detect the account, and no activity occurred |
| Magnitude | Not quantifiable as a dollar misstatement; the user had read-and-post access to the AP module |
| Compensating controls | ITGC-01 quarterly user access review (effective); ERP manual journal entry approval |
| Aggregation | No other deficiencies affect logical access to the ERP in this period |

**Conclusion:** **Control deficiency** (not a significant deficiency or material weakness). Report to management; no Audit Committee escalation required on its own.

## 5. Recommendation and management response
| Action | Owner | Due |
|---|---|---|
| Add a weekly reconciliation of HR termination dates vs. the date entered, flagging entries more than 1 day late | HR Operations | 2026-12-15 |
| Remind managers of the same-day termination notice requirement; add it to the manager offboarding checklist | HR Business Partners | 2026-11-30 |
| Retest ITGC-05 on Q4 terminations | GRC | 2027-01-31 |

**Management response (illustrative):** HR agrees and will implement the weekly reconciliation by 2026-12-15.

# DSAR Playbook: Access and Deletion Requests (GDPR + CCPA/CPRA)

**Skills shown:** operationalizing privacy rights, identity verification, exemptions (BSA retention, legal holds), deadline management, metrics.

## Case study

| | |
|---|---|
| **Why I built this** | Data subject requests have legal deadlines; a repeatable process prevents missed ones. |
| **Explain** | An end-to-end process for access and deletion requests under GDPR and CCPA, with a deadline tracker. |
| **What was broken** | One deletion completed late because a system owner was slow. |
| **What was fixed** | Formula-driven deadlines, a system search checklist and a 5-business-day owner SLA. |
| **Business impact** | 8 of 9 requests on time; clear records for regulators. |
| **Remediation still open** | Escalation path for owners who miss the SLA. |
| **Decisions and trade-offs** | I keep KYC records even after a deletion request: the Bank Secrecy Act requires 5 years, and the response explains that. |

## Details

| File | What it is |
|---|---|
| [DSAR_Playbook.md](DSAR_Playbook.md) | Deadlines table, process flow, verification standards, system search checklist, exemptions, response templates, roles |
| [DSAR_Tracker.xlsx](DSAR_Tracker.xlsx) | Request log with formula-driven deadlines (GDPR one month / +2; CCPA 10 business days to confirm, 45 / +45 days to respond, 15 business days for opt-outs) and a dashboard |

**Sample dashboard (12 fictional requests):** 9 closed, 8 of 9 on time (89%), average 31 days to close, 1 extension, 1 late deletion traced to an HR system owner delay.

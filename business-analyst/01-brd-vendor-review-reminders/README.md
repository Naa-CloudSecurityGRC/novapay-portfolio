# BRD: Automated Vendor-Review Reminders

**Skills shown:** requirements elicitation and writing, MoSCoW prioritization, Gherkin acceptance criteria, requirements traceability.

## Case study

| | |
|---|---|
| **Why I built this** | BA roles want to see real requirements documents, not a claim of 'requirements gathering'. |
| **Explain** | The third-party risk team missed vendor review deadlines because reminders were manual. I wrote the requirements for an automated fix. |
| **What was broken** | 23% of critical vendor reviews were late; analysts spent about 6 hours a week chasing owners; a bank-partner exam finding. |
| **What was fixed** | A BRD with 12 functional and 4 non-functional requirements, acceptance criteria, and a traceability matrix linking each requirement to a story and test. |
| **Business impact** | Target: 95% of critical reviews on time and follow-up time under 1 hour a week; full audit trail of reminders. |
| **Remediation still open** | One requirement failed testing (pause reminders) and two 'Could have' items are deferred. |
| **Decisions and trade-offs** | I deferred Teams delivery and weekly digests ('Could have') to hit the exam date with the 'Must haves'. |

## Details

NovaPay's third-party risk team misses vendor review deadlines because reminders are manual (23% of critical reviews late). This BRD defines a reminder and escalation feature in the GRC platform.

| File | What it is |
|---|---|
| [BRD.md](BRD.md) | Problem, objectives, stakeholders, scope, 12 functional and 4 non-functional requirements, acceptance criteria, risks |
| [RTM_Vendor_Review_Reminders.xlsx](RTM_Vendor_Review_Reminders.xlsx) | Requirements traceability matrix: objective → requirement → Jira story → test case → status, with a coverage summary |

The user stories for this feature are in [the Agile backlog project](../03-agile-backlog/).

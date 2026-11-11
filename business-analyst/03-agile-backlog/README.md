# Agile Backlog: Automated Vendor-Review Reminders

**Skills shown:** epics and user stories, Gherkin acceptance criteria, story-point estimation, sprint planning, traceability to the BRD.

## Case study

| | |
|---|---|
| **Why I built this** | To show I can turn requirements into a delivery plan a development team can use. |
| **Explain** | An epic with 14 user stories, acceptance criteria and a two-sprint plan, ready to import into Jira. |
| **What was broken** | Requirements without stories and estimates can't be planned or tracked. |
| **What was fixed** | Stories with Gherkin acceptance criteria, story points, a Definition of Done and traceability back to the BRD. |
| **Business impact** | Core reminders and the audit log ship in sprint 1, ahead of the exam. |
| **Remediation still open** | Two 'Could have' stories remain in the backlog. |
| **Decisions and trade-offs** | Sprint 2 carries fewer points on purpose, to leave room for user testing with Internal Audit. |

## Details

Epic **NP-100 Automated vendor-review reminders** delivers the requirements in the [BRD](../01-brd-vendor-review-reminders/BRD.md). Every story traces to a requirement ID (see the [RTM](../01-brd-vendor-review-reminders/RTM_Vendor_Review_Reminders.xlsx)).

## Sprint plan (2-week sprints, team velocity ~24-26 points)

| Sprint | Goal | Stories | Points |
|---|---|---|---:|
| 1 | Core reminders, escalations and audit log live for Critical/High vendors | NP-101, NP-102, NP-103, NP-104, NP-105, NP-107, NP-113, NP-114 | 26 |
| 2 | Dashboard, pause and export; UAT with TPRM and Internal Audit | NP-106, NP-108, NP-109, NP-110 | 16 |
| Backlog | Nice-to-have delivery options (Could have) | NP-111, NP-112 | 10 |

Sprint 2 carries fewer points to leave room for UAT, defect fixes and the go-live checklist.

## Stories

| ID | Story | Points | Priority | Sprint | Traces to |
|---|---|---:|---|---|---|
| NP-101 | As a TPRM analyst, I want each vendor's next review date calculated from its risk tier, so that I don't track due dates by hand. | 3 | Highest | 1 | FR-01 |
| NP-102 | As a vendor owner, I want reminders 60, 30 and 7 days before my review is due and on the due date, so that I have time to complete it. | 5 | Highest | 1 | FR-02, FR-03 |
| NP-103 | As the Head of TPRM, I want overdue reviews escalated to the owner's manager after 7 days, so that reviews don't stall. | 3 | High | 1 | FR-04 |
| NP-104 | As the Head of TPRM, I want 30-day overdue Critical and High reviews escalated to me, so that I can act before an exam finding. | 2 | High | 1 | FR-05 |
| NP-105 | As a vendor owner, I want reminders to stop once my review is marked complete, so that I'm not sent irrelevant emails. | 2 | High | 1 | FR-06 |
| NP-106 | As a TPRM analyst, I want to pause reminders for a vendor with a reason and end date, so that vendors in offboarding aren't chased. | 3 | Medium | 2 | FR-07 |
| NP-107 | As an internal auditor, I want a read-only log of every reminder and escalation, so that I can test the control without email searches. | 5 | Highest | 1 | FR-08, NFR-02 |
| NP-108 | As the Head of TPRM, I want a dashboard of upcoming, due and overdue reviews by tier and owner, so that I can report to the risk committee. | 8 | High | 2 | FR-09, NFR-04 |
| NP-109 | As a TPRM analyst, I want to click from a dashboard tile to the vendor list behind it, so that I can follow up quickly. | 3 | Medium | 2 | FR-09 |
| NP-110 | As an internal auditor, I want to export the reminder log to CSV, so that I can select test samples. | 2 | Medium | 2 | FR-10 |
| NP-111 | As a vendor owner, I want to choose email or Microsoft Teams for reminders, so that I see them where I work. | 5 | Low | Backlog | FR-11 |
| NP-112 | As a vendor owner with more than 3 open reviews, I want one weekly digest, so that I'm not flooded with emails. | 5 | Low | Backlog | FR-12 |
| NP-113 | As the GRC platform lead, I want the daily job to finish by 07:00 ET and alert on failure, so that reminders are never silently missed. | 3 | High | 1 | NFR-01 |
| NP-114 | As the Head of TPRM, I want only the TPRM role to pause reminders or change due dates, so that the control can't be bypassed. | 3 | High | 1 | NFR-03 |

## Acceptance criteria

### NP-101 Calculate review due dates from vendor tier

```gherkin
Given a vendor with risk tier "Medium" and last review completed 2025-06-30
When the vendor record is saved
Then the next review date is 2027-06-30
```

### NP-102 Send pre-due reminders to vendor owners

```gherkin
Given a Critical vendor with review due 2026-03-31 and status "Not started"
When the daily job runs on 2026-03-24
Then the owner receives the "7 days to due date" reminder
```

### NP-103 Escalate 7-day overdue reviews to owner's manager

```gherkin
Given a review due 2026-03-31 that is not complete
When the daily job runs on 2026-04-07
Then the owner's manager receives an escalation
And the escalation is logged
```

### NP-104 Escalate 30-day overdue Critical/High reviews to TPRM head

```gherkin
Given a High-tier review 30 days overdue
When the daily job runs
Then the Head of TPRM receives an escalation
And Medium and Low tiers are not escalated to the Head of TPRM
```

### NP-105 Stop reminders when review is complete

```gherkin
Given a review marked "Complete"
When the daily job runs
Then no reminder or escalation is sent for that vendor
```

### NP-106 Pause reminders with reason and end date

```gherkin
Given I pause reminders with reason "Contract ending" until 2026-05-01
When the daily job runs on 2026-04-15
Then no reminder is sent
And reminders resume on 2026-05-02 if the review is still open
```

### NP-107 Immutable reminder and escalation log

```gherkin
Given any reminder or escalation is sent
Then the log records vendor ID, recipient, channel and timestamp
And no user, including administrators, can edit or delete the entry
```

### NP-108 Overdue reviews dashboard

```gherkin
Given 1,000 vendors in the inventory
When I open the dashboard
Then it loads in under 3 seconds
And I can filter by tier and owner
```

### NP-109 Dashboard drill-down to vendor record

```gherkin
Given the dashboard shows 12 overdue High-tier reviews
When I click the tile
Then I see the 12 vendors with owner and days overdue
```

### NP-110 Export log and dashboard data to CSV

```gherkin
Given I have the Auditor role
When I export the reminder log for Q1
Then I receive a CSV with every Q1 entry
```

### NP-111 Teams delivery preference

```gherkin
Given my preference is "Teams"
When a reminder is due
Then I receive it in Teams and not by email
```

### NP-112 Weekly digest for owners of many vendors

```gherkin
Given I own 5 vendors with open reviews
When reminders are due in the same week
Then I receive one digest listing all 5
```

### NP-113 Daily reminder job reliability and alerting

```gherkin
Given the daily job fails
When 07:00 ET passes
Then the platform team receives an alert
And the job can be re-run without sending duplicates
```

### NP-114 Role-based access for pause and date edits

```gherkin
Given I sign in through SSO without the TPRM role
When I try to pause reminders
Then the action is blocked and logged
```

## Definition of Done

- Acceptance criteria pass in the test environment
- Peer code review complete; change ticket approved
- Reminder log entries verified for the story's scenarios
- RTM test status updated
- Product owner (Head of TPRM) accepts the story in sprint review

## Import into Jira

1. Create a free Jira Cloud site and a Scrum project with key `NP`.
2. Settings → System → External system import → CSV → upload `jira_import.csv`.
3. Map *Issue Id*, *Summary*, *Description*, *Priority*, *Story Points*, *Labels*, *Sprint* and *Parent Id* (to link stories to the epic).
4. Screenshot the backlog and the Sprint 1 board into `screenshots/` and add them to this page.
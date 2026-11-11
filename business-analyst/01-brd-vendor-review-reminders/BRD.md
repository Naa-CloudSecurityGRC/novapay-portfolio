# Business Requirements Document: Automated Vendor-Review Reminders

| Item | Detail |
|---|---|
| Company | NovaPay (fictional U.S. card-payments fintech) |
| Document owner | Business Analyst, Risk Technology |
| Business sponsor | Head of Third-Party Risk Management (TPRM) |
| Version | 1.0 (approved for build) |
| Related artifacts | [Requirements Traceability Matrix](RTM_Vendor_Review_Reminders.xlsx), [Agile backlog](../03-agile-backlog/) |

## 1. Problem statement

NovaPay's TPRM team tracks 140 vendor reviews in a shared spreadsheet. Review due dates are checked by hand, so reviews are missed or completed late.

- In the last audit cycle, **23% of critical-vendor reviews were completed after their due date**.
- The bank sponsor's exam flagged late vendor reviews as a finding, citing the 2023 Interagency Guidance on Third-Party Relationships (ongoing monitoring).
- Analysts spend about **6 hours a week** chasing vendor owners by email.

## 2. Business objectives

| ID | Objective | Measure of success |
|---|---|---|
| BO-1 | Complete reviews on time | 95% of critical and high-risk vendor reviews completed by due date within 2 quarters of go-live |
| BO-2 | Reduce manual follow-up | Analyst follow-up time down from ~6 to under 1 hour per week |
| BO-3 | Give leadership and auditors evidence | Overdue reviews visible on a dashboard; full reminder and escalation history kept for audit |

## 3. Stakeholders

| Stakeholder | Role | Interest |
|---|---|---|
| Head of TPRM | Sponsor, approver | Exam-ready program, on-time reviews |
| TPRM analysts | Primary users | Less manual chasing, clear queue |
| Vendor (business) owners | Receive reminders, complete reviews | Clear asks, few emails |
| Information Security | Performs security assessments | Enough lead time |
| Internal Audit | Tests the control | Complete, unaltered evidence |
| IT / GRC platform team | Builds and supports | Clear, testable requirements |

## 4. Scope

**In scope**
- Reminder schedule driven by vendor risk tier and review due date
- Escalation to the vendor owner's manager and to TPRM leadership
- Overdue dashboard and audit log
- Integration with the vendor inventory (system of record) and email / Microsoft Teams

**Out of scope**
- Vendor-facing portal and questionnaire distribution (Phase 2)
- Changes to the vendor tiering methodology
- Contract management

## 5. Assumptions and constraints

- The vendor inventory holds an accurate risk tier, owner, and next-review date for every active vendor.
- Reminders are sent from the existing GRC platform; no new tool is purchased.
- Go-live before the next bank-sponsor exam (two sprints of build, see backlog).

## 6. Current state vs. future state

| | Current (as-is) | Future (to-be) |
|---|---|---|
| Due-date tracking | Analyst filters spreadsheet weekly | System calculates due dates from tier |
| Reminders | Manual email, inconsistent timing | Automatic at 60 / 30 / 7 days and on due date |
| Escalation | Ad hoc | Automatic at 7 and 30 days overdue |
| Reporting | Built by hand before committees | Live dashboard |
| Audit evidence | Email searches | Immutable reminder log |

## 7. Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | The system shall calculate each vendor's next review date from its risk tier: Critical 12 months, High 12 months, Medium 24 months, Low 36 months. | Must |
| FR-02 | The system shall send the vendor owner a reminder 60, 30 and 7 days before the review due date. | Must |
| FR-03 | The system shall send a reminder on the due date if the review is not marked complete. | Must |
| FR-04 | The system shall escalate to the vendor owner's manager when a review is 7 days overdue. | Must |
| FR-05 | The system shall escalate Critical and High vendors to the Head of TPRM when a review is 30 days overdue. | Must |
| FR-06 | The system shall stop all reminders for a vendor once its review status is "Complete". | Must |
| FR-07 | The system shall let a TPRM analyst pause reminders for a vendor with a documented reason and an end date. | Should |
| FR-08 | The system shall log every reminder and escalation (recipient, timestamp, channel, vendor ID). | Must |
| FR-09 | The system shall show a dashboard of upcoming, due and overdue reviews, filterable by tier and owner. | Must |
| FR-10 | The system shall let users export the reminder log and dashboard data to CSV. | Should |
| FR-11 | The system shall deliver reminders by email and Microsoft Teams based on user preference. | Could |
| FR-12 | The system shall send the vendor owner a weekly digest instead of separate emails when they own more than 3 vendors with open reviews. | Could |

## 8. Non-functional requirements

| ID | Requirement | Priority |
|---|---|---|
| NFR-01 | Reminder jobs shall run daily by 07:00 ET with 99.5% monthly success rate. | Must |
| NFR-02 | Reminder log entries shall be read-only for all users, including administrators, and retained for 7 years. | Must |
| NFR-03 | Access shall use NovaPay single sign-on (SSO); only the TPRM role can pause reminders or edit due dates. | Must |
| NFR-04 | The dashboard shall load in under 3 seconds for up to 1,000 vendors. | Should |

## 9. Acceptance criteria (samples; full set in the backlog)

**FR-02 Reminder schedule**
```gherkin
Given a vendor with risk tier "Critical" and review due date 2026-03-31
And its review status is "Not started"
When the daily reminder job runs on 2026-01-30
Then the vendor owner receives a "60 days to due date" reminder
And the reminder is written to the reminder log
```

**FR-06 Stop on completion**
```gherkin
Given a vendor review marked "Complete" on 2026-03-10
When the daily reminder job runs on 2026-03-24
Then no reminder is sent for that vendor
```

**FR-04 Escalation**
```gherkin
Given a vendor review due on 2026-03-31 that is not complete
When the daily reminder job runs on 2026-04-07
Then the vendor owner's manager receives an escalation email
And the escalation is written to the reminder log
```

## 10. Risks and dependencies

| Risk / dependency | Impact | Mitigation |
|---|---|---|
| Vendor owners missing or out of date in the inventory | Reminders go to the wrong person | One-time data clean-up before go-live; monthly owner-validation report |
| Email fatigue | Reminders ignored | Weekly digest (FR-12); escalations only after due date |
| HR feed needed for manager lookup | No escalation path | Dependency on HR integration; fallback to TPRM analyst |

## 11. Sign-off

| Name / role | Decision | Date |
|---|---|---|
| Head of TPRM | Approved | (on approval) |
| GRC Platform Lead | Approved | (on approval) |
| Internal Audit (advisory) | Reviewed, no objection | (on approval) |

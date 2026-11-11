# Continuous Monitoring: Vendor Incident Alerts

Three internal alerts written the way TPRM would send them to risk owners in the first hours of a vendor incident.

> **Tabletop scenarios.** The vendors are fictional (from the [fourth-party map](../03-fourth-party-concentration/)). Scenarios are modeled on common real-world vendor incidents: ransomware at a service provider, a breach of a SaaS customer-support tool through stolen credentials, and a cloud-region outage. To strengthen this project, swap in 3 real public incidents from the last 12 months and cite the vendor's own statements.

---

## Alert 1: Ransomware at VerifyCo (KYB screening): SEVERITY HIGH

| Field | Detail |
|---|---|
| Source | Vendor notice to NovaPay security contact, 2026-10-14 06:40 ET; vendor status page |
| What happened | VerifyCo detected ransomware in its corporate network and took its screening API offline as a precaution. Data theft not yet ruled out. |
| Vendor tier | Critical |

**NovaPay exposure**
- **Data:** VerifyCo holds owner names, dates of birth, SSNs and ID images for ~18,000 merchant owners (RoPA PA-01).
- **Service:** merchant onboarding cannot complete sanctions/KYB screening while the API is down (~40 applications a day).
- **Controls:** BSA/AML onboarding control depends on VerifyCo; no automated fallback.

**Immediate actions (first 24 hours)**
1. Pause automatic onboarding approvals; switch to the manual screening procedure for priority merchants (Compliance).
2. Rotate the API keys and SFTP credentials NovaPay uses with VerifyCo; block VerifyCo connections at the firewall until cleared (Security).
3. Open a NovaPay incident (SEV-2) under POL-04; Legal and Privacy start the breach-notification assessment.

**Questions for VerifyCo**
- Is NovaPay data on affected systems? Is there evidence of exfiltration?
- Which forensic firm is engaged, and when will initial findings be shared?
- Are backups unaffected, and what is the restore timeline (versus the contract RTO)?
- Have law enforcement and your regulators been notified?
- What indicators of compromise should NovaPay check for?

**Notification considerations:** if NovaPay data was taken, state breach-notification laws (SSNs trigger notice in all U.S. states), the bank partner's contract, and GDPR (72 hours to the supervisory authority for EU merchant owners) may apply.

**Follow-ups:** daily vendor calls until restored · post-incident assessment before reconnecting · accelerate the second screening vendor in the exit plan.

---

## Alert 2: Stolen credentials used to access HelpDeskly customer instances: SEVERITY MEDIUM

| Field | Detail |
|---|---|
| Source | HelpDeskly security advisory to all customers, 2026-09-03; threat-intelligence feed |
| What happened | Attackers used credentials stolen by infostealer malware to log into some customers' HelpDeskly instances that did not enforce SSO/MFA, and exported support tickets. HelpDeskly's own systems were not breached. |
| Vendor tier | Medium |

**NovaPay exposure**
- **Data:** support tickets can contain merchant contact details and, against policy, occasional bank details or screenshots.
- **Control check:** NovaPay's HelpDeskly instance uses Okta SSO with MFA (CUEC in place), so the attack path likely does not apply.

**Immediate actions**
1. Confirm SSO enforcement and that local (non-SSO) logins are disabled; review the HelpDeskly audit log for exports or logins from unusual IPs in the last 90 days (Security).
2. Rotate HelpDeskly API tokens used by integrations.
3. Search tickets for bank account numbers or card data and redact them (Support + Privacy).

**Questions for HelpDeskly**
- Can you confirm NovaPay's instance was not among those accessed?
- Will you enforce MFA for all customer admin accounts by default?
- Can you provide export and login logs for our instance for the last 90 days?

**Follow-ups:** add an automated redaction rule for card and bank numbers in tickets · add "SSO enforced for all users" to the vendor's annual review.

---

## Alert 3: AWS us-east-1 regional outage affecting 4 vendors: SEVERITY HIGH

| Field | Detail |
|---|---|
| Source | AWS Health Dashboard and vendor status pages, 2026-08-21 10:05 ET |
| What happened | A regional outage degraded several AWS services in us-east-1 for about 7 hours. |
| Vendors affected | VerifyCo, DeviceSure, LedgerLink, MailNest (and NovaPay's own platform) |

**NovaPay exposure**
- Payments platform degraded; fraud scoring fell back to rules-only mode (designed fallback worked).
- Onboarding screening unavailable for 7 hours (VerifyCo).
- LedgerLink unavailable on business day 2 of month-end close.
- No data loss reported.

**Immediate actions**
1. Activate the incident bridge; confirm fraud rules-only fallback limits are in force (Fraud Ops).
2. Controller decides whether to use the manual reconciliation procedure or delay the close step by one day.
3. Send merchant status-page update (Communications).

**Questions for vendors**
- Did you fail over to another region? If not, why not, and is multi-region on your roadmap?
- Did you meet your contractual RTO and SLA? Will service credits apply?
- Was any data lost or delayed (e.g., queued screening requests)?

**Follow-ups:** concentration risk reported to the Risk Committee as a realized risk · track vendor SLA credits · prioritize the multi-region assessment from the [concentration review](../03-fourth-party-concentration/).

---

## Monitoring sources NovaPay uses
| Source | What it tells us |
|---|---|
| Vendor status pages and security advisories | Outages and incidents, often first |
| Security-rating services | Changes in a vendor's external security posture |
| Threat-intelligence and news alerts on vendor names | Breaches, ransomware leak-site listings |
| Annual reassessments, SOC reports, bridge letters | Control changes and exceptions |
| Financial and adverse-media alerts | Vendor financial distress, litigation, regulatory action |

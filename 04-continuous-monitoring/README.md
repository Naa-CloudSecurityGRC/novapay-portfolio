# Continuous Monitoring: Vendor Incident Alerts

**Skills shown:** ongoing monitoring, rapid impact assessment (data, service, controls), vendor questioning, breach-notification triggers, linking incidents to exit plans and concentration risk.

## Case study

| | |
|---|---|
| **Why I built this** | Third-party risk doesn't stop at onboarding; I wanted to show how to react when a vendor is breached. |
| **Explain** | Three incident alerts written as I'd send them internally: impact, actions, questions for the vendor. |
| **What was broken** | A ransomware attack on a critical vendor halted onboarding and may have exposed sensitive data. |
| **What was fixed** | First-24-hour actions: pause automation, rotate credentials, start breach assessment, switch to manual screening. |
| **Business impact** | Limits exposure and keeps onboarding compliant during the outage. |
| **Remediation still open** | Accelerate the backup vendor from the exit plan. |
| **Decisions and trade-offs** | I paused automatic approvals rather than all onboarding, so priority merchants could still be screened manually. |

## Details

Three internal alerts, each with severity, NovaPay exposure, first-24-hour actions, questions for the vendor, notification considerations and follow-ups:

| Alert | Scenario | Severity |
|---|---|---|
| 1 | Ransomware at the KYB screening vendor; SSNs and ID images possibly exposed; onboarding halted | High |
| 2 | Stolen credentials used to export tickets from a support SaaS (customer instances without MFA) | Medium |
| 3 | Cloud-region outage hits 4 vendors at once during month-end close | High |

File: [Monitoring_Alerts.md](Monitoring_Alerts.md). Scenarios are tabletop exercises with fictional vendors, modeled on common incident types.

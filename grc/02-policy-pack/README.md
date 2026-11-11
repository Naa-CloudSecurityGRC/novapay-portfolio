# Policy Pack: 5 Core Security Policies

**Skills shown:** policy writing, roles and accountability, mapping policy to frameworks (SOC 2, ISO 27001:2022, NIST CSF 2.0, PCI DSS v4.0).

## Case study

| | |
|---|---|
| **Why I built this** | GRC analysts write and maintain policies; I wanted samples that map to frameworks, not generic templates. |
| **Explain** | Five core policies, each with roles, specific requirements, exceptions and framework references. |
| **What was broken** | Incident Response and Data Retention policies were drafts and never approved (SOC 2 CC5.3 gap). |
| **What was fixed** | Approved policy set with concrete timelines (e.g., access removed within 24 hours, critical patches in 15 days). |
| **Business impact** | Gives auditors testable statements and gives staff clear rules. |
| **Remediation still open** | Annual review; align retention schedule with legal counsel. |
| **Decisions and trade-offs** | I wrote measurable requirements instead of 'should' language, because a policy you can't test can't be audited. |

## Details

| Policy | Highlights |
|---|---|
| [POL-01 Information Security](POL-01_Information_Security_Policy.md) | Program framework, classification, patch SLAs, exception process |
| [POL-02 Acceptable Use](POL-02_Acceptable_Use_Policy.md) | Approved tools, AI tool use with Restricted data, device rules |
| [POL-03 Access Control](POL-03_Access_Control_Policy.md) | Joiner/mover/leaver timelines, MFA, privileged access, SoD, quarterly reviews |
| [POL-04 Incident Response](POL-04_Incident_Response_Policy.md) | Severity matrix, notification decisions, post-incident reviews, annual tabletop |
| [POL-05 Data Retention & Disposal](POL-05_Data_Retention_and_Disposal_Policy.md) | Retention schedule (BSA, SOX, PCI), legal holds, NIST 800-88 disposal |

Each policy follows one structure: purpose · scope · roles · policy statements · exceptions · enforcement · framework references. These policies close the CC5.3 gap in the [SOC 2 readiness assessment](../01-soc2-readiness/).

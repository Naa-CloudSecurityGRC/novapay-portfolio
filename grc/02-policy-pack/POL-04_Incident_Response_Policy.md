# Incident Response Policy

| Field | Value |
|---|---|
| Policy ID | POL-04 |
| Owner | CISO |
| Approved by | Chief Information Security Officer (CISO); Audit & Risk Committee notified |
| Effective date | 2026-12-01 |
| Review cycle | Annual, or after a significant change |
| Applies to | All NovaPay employees, contractors and third parties with access to NovaPay systems or data |

> NovaPay is a fictional company. This policy is a portfolio sample.

## 1. Purpose
Make sure NovaPay detects, contains and recovers from security incidents quickly, and meets its legal, regulatory and contractual notification duties.

## 2. Scope
All suspected or confirmed security incidents affecting NovaPay systems, data or services, including incidents at vendors that affect NovaPay data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Incident Commander (Security Operations lead on call) | Leads the response; sets severity; coordinates the team |
| CISO | Approves severity 1-2 decisions; briefs executives and the board |
| Legal and Privacy | Decide on notification to regulators, card brands, bank partners and individuals |
| Communications | Prepares customer and media statements |
| System owners and Engineering | Contain, eradicate and restore |
| All workforce members | Report suspected incidents immediately |

## 4. Severity levels
| Severity | Definition (examples) | Response target |
|---|---|---|
| SEV-1 Critical | Confirmed breach of Restricted data, or payments platform down | Incident team engaged within 15 minutes; executives within 1 hour |
| SEV-2 High | Likely data exposure or major service degradation | Engaged within 1 hour |
| SEV-3 Medium | Contained malware, single compromised account, no data loss | Engaged within 4 hours |
| SEV-4 Low | Policy violation or suspicious event with no impact | Next business day |

## 5. Policy statements
1. NovaPay keeps an Incident Response Plan with playbooks for common scenarios (ransomware, account compromise, data exposure, vendor breach, DDoS).
2. Response follows the phases: **prepare → detect and analyze → contain → eradicate → recover → post-incident review.**
3. Evidence is preserved (logs, images, tickets) with a chain of custody when legal action or regulatory reporting is possible.
4. Legal and Privacy assess notification duties for every SEV-1 and SEV-2, including state breach-notification laws, card brand rules, bank partner contracts and, where applicable, SEC disclosure.
5. Every SEV-1 and SEV-2 has a written post-incident review within 10 business days, with root cause and tracked actions.
6. The plan is tested with at least one tabletop exercise per year and updated after tests and real incidents.
7. Vendors must notify NovaPay of incidents affecting NovaPay data within the time set in their contract (72 hours or less).

## 6. Exceptions
None. Deviations during an incident are recorded by the Incident Commander and reviewed afterwards.

## 7. Framework references
| Framework | Reference |
|---|---|
| SOC 2 | CC7.3, CC7.4, CC7.5 |
| ISO/IEC 27001:2022 | Annex A 5.24, 5.25, 5.26, 5.27, 5.28, 6.8 |
| NIST CSF 2.0 | RS.MA, RS.AN, RS.CO, RS.MI, RC.RP |
| NIST SP 800-61 | Incident handling guide |
| PCI DSS v4.0 | Requirement 12.10 |

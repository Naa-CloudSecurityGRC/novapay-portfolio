# Access Control Policy

| Field | Value |
|---|---|
| Policy ID | POL-03 |
| Owner | Director of IT Operations |
| Approved by | Chief Information Security Officer (CISO); Audit & Risk Committee notified |
| Effective date | 2026-12-01 |
| Review cycle | Annual, or after a significant change |
| Applies to | All NovaPay employees, contractors and third parties with access to NovaPay systems or data |

> NovaPay is a fictional company. This policy is a portfolio sample.

## 1. Purpose
Make sure only authorized people have access to NovaPay systems and data, with no more access than their role needs.

## 2. Scope
All user, privileged, service and third-party accounts on NovaPay systems, including cloud infrastructure, production databases, the payments platform, financial systems (ERP) and SaaS tools.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| System owners | Define roles; approve access requests; complete access reviews |
| Managers | Request and approve access for their team; notify HR of role changes |
| HR | Send joiner, mover and leaver events to IT on the effective date |
| IT Operations / Identity team | Provision and remove access; run access reviews; manage SSO and MFA |

## 4. Policy statements
1. **Least privilege and role-based access:** access is granted by role; additional access requires business justification and system-owner approval.
2. **Unique IDs:** every user has a unique ID. Shared accounts are not allowed unless approved as an exception and tied to a named owner.
3. **Single sign-on and MFA:** all supported applications use NovaPay SSO. MFA is required for all remote access, all privileged access, and all access to systems holding Restricted data.
4. **Passwords:** where SSO isn't possible, passwords are at least 12 characters and are not reused; default passwords are changed before go-live.
5. **Joiners:** access is provisioned only after a manager-approved request.
6. **Movers:** access no longer needed for the new role is removed within 5 business days of the change.
7. **Leavers:** all access is disabled within 24 hours of termination (immediately for involuntary terminations).
8. **Privileged access:** administrator rights are limited to named individuals, use separate admin accounts, and are granted just-in-time where the platform supports it. Privileged activity is logged.
9. **Segregation of duties:** no single user may both create and approve a payment, a vendor master change, or a manual journal entry. Conflicts are identified through a documented SoD rule set.
10. **Access reviews:** system owners review user access to in-scope systems quarterly and privileged access monthly. Removals are completed within 5 business days of review sign-off.
11. **Service accounts:** have a named owner, cannot be used for interactive login, and have credentials rotated at least annually.
12. **Third-party access:** is time-limited, approved by the system owner and reviewed quarterly.

## 5. Exceptions
Through the POL-01 exception process; exceptions involving privileged or SoD access also need the CFO's approval if financial systems are affected.

## 6. Enforcement
Unauthorized access attempts or misuse of privileges may lead to disciplinary action, up to termination.

## 7. Framework references
| Framework | Reference |
|---|---|
| SOC 2 | CC6.1, CC6.2, CC6.3 |
| ISO/IEC 27001:2022 | Annex A 5.3, 5.15, 5.16, 5.17, 5.18, 8.2, 8.5 |
| NIST CSF 2.0 | PR.AA |
| PCI DSS v4.0 | Requirements 7 and 8 |
| SOX ITGC | User access provisioning, termination, periodic review, privileged access |

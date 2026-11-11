# Data Retention and Disposal Policy

| Field | Value |
|---|---|
| Policy ID | POL-05 |
| Owner | Chief Privacy Officer |
| Approved by | Chief Information Security Officer (CISO); Audit & Risk Committee notified |
| Effective date | 2026-12-01 |
| Review cycle | Annual, or after a significant change |
| Applies to | All NovaPay employees, contractors and third parties with access to NovaPay systems or data |

> NovaPay is a fictional company. This policy is a portfolio sample.

## 1. Purpose
Keep records as long as law, regulation and business need require, and no longer, then dispose of them securely.

## 2. Scope
All records and data NovaPay holds, in any format or location, including backups, SaaS tools and records held by vendors for NovaPay.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Privacy Officer | Owns the retention schedule and this policy |
| Legal | Issues and releases legal holds; confirms legal retention periods |
| Data owners | Apply the schedule to their systems; approve disposal |
| IT Operations | Configure automated deletion; securely wipe and destroy media |

## 4. Retention schedule (summary)
| Record type | Retention | Basis |
|---|---|---|
| Customer identification (KYC) records | 5 years after account closed | BSA / FinCEN CDD rule |
| Transaction records | 5 years | BSA recordkeeping |
| Financial statements and general ledger | 7 years | SOX / audit and tax requirements |
| SOX control evidence and audit workpapers | 7 years | SOX Section 802 / SEC rules |
| Full card numbers (PAN) | Only as long as needed for settlement and disputes; then deleted or rendered unreadable | PCI DSS Requirement 3 |
| Sensitive authentication data (CVV, PIN, full track data) | Never stored after authorization | PCI DSS Requirement 3.3 |
| Marketing contact data | Until consent withdrawn or 24 months of inactivity | GDPR / CCPA data minimization |
| Security logs | 1 year (90 days immediately available) | PCI DSS Requirement 10 |
| HR and payroll records | 7 years after employment ends | Federal and state employment law |

## 5. Policy statements
1. Data owners must follow the retention schedule; data is not kept "just in case".
2. **Legal holds override the schedule.** Legal notifies data owners in writing, and deletion stops until Legal releases the hold.
3. Disposal must make data unrecoverable: cryptographic erasure or NIST SP 800-88 methods for media; cross-cut shredding for paper.
4. Disposal of Restricted data is recorded (what, when, how, who approved).
5. Automated deletion is configured where systems support it; data owners confirm it works at least annually.
6. Contracts require vendors to return or delete NovaPay data at the end of the relationship and to certify deletion.
7. Requests from individuals to delete personal data are handled under the DSAR procedure, subject to legal retention duties.

## 6. Exceptions
Any longer retention requires a written business or legal reason approved by the Chief Privacy Officer and Legal.

## 7. Framework references
| Framework | Reference |
|---|---|
| SOC 2 | CC6.5 (and Confidentiality C1.2 if in scope) |
| ISO/IEC 27001:2022 | Annex A 5.33, 5.34, 7.10, 7.14, 8.10 |
| NIST CSF 2.0 | PR.DS, GV.OC |
| PCI DSS v4.0 | Requirement 3.2 |
| GDPR / CCPA | Storage limitation (GDPR Art. 5(1)(e)); CCPA retention disclosure |

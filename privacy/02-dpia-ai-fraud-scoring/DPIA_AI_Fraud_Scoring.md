# Data Protection Impact Assessment: AI-Based Fraud Scoring

| Field | Detail |
|---|---|
| Project | "SmartScore": machine-learning fraud score using transaction, device and location signals |
| Business owner | VP Fraud & Risk |
| DPIA author | Privacy Analyst (Naa Aboagye, portfolio sample) |
| Reviewed by | Data Protection Officer; Information Security; Model Risk Management |
| Status | Approved with conditions |
| Related | [RoPA activity PA-03](../01-ropa-data-inventory/) |

> NovaPay and SmartScore are fictional. This DPIA follows GDPR Article 35 and the structure of common regulator templates.

## 1. Why a DPIA is needed
SmartScore meets several high-risk criteria: **systematic profiling** of cardholders, **innovative technology** (machine learning), **large scale** (about 40 million transactions a month), and outputs that can **block a payment**. Under GDPR Article 35 and EDPB guidance, two or more of these criteria normally require a DPIA.

## 2. Description of the processing

| Element | Detail |
|---|---|
| Purpose | Detect and stop fraudulent card transactions in real time; reduce fraud losses and chargebacks |
| Data subjects | Cardholders paying NovaPay merchants (EU and U.S.) |
| Data | Transaction amount, time and merchant; tokenized card number; device ID and browser fingerprint; IP address; **approximate** location (city level, derived from IP); 90-day transaction velocity |
| Not used | Name, precise GPS location, demographic data, or any special category data |
| Output | Risk score 0-100 → approve (0-59), step-up authentication such as 3-D Secure (60-89), decline (90-100) |
| Volume | ~40 million transactions a month; ~1.5% stepped up, ~0.3% declined |
| Systems and vendors | Payments platform, fraud engine on AWS (U.S.), device-intelligence vendor (fictional DeviceSure) as processor |
| Retention | Model features 13 months; fraud case records 5 years |
| Transfers | EU data to U.S. under the EU-U.S. Data Privacy Framework or SCCs |

## 3. Consultation
- Fraud Operations, Data Science, Information Security, Legal, Customer Support (who handle declined-payment complaints), and Model Risk Management.
- Two merchant advisory-board members gave feedback on the cardholder experience of step-up checks.

## 4. Necessity and proportionality

| Question | Assessment |
|---|---|
| Lawful basis | Legitimate interests (Art. 6(1)(f)): preventing fraud is a recognized legitimate interest (GDPR Recital 47). A legitimate interests assessment (LIA) is attached to the project file. |
| Necessary? | Rules-only screening missed 38% of confirmed fraud in the pilot; the model is needed to reach target loss rates. |
| Data minimization | Name and precise location excluded; city-level location only. Precise geolocation would be **sensitive personal information under CPRA**, so it was deliberately left out. |
| Automated decisions (Art. 22) | Most high scores trigger step-up authentication, not a final decision. Declines (score 90+) can significantly affect cardholders, so: cardholders can retry with step-up or contact the merchant / NovaPay support, declined transactions can be reviewed by a human analyst on request, and the logic is explained in the privacy notice. Legal confirms reliance on Art. 22(2) for the remaining automated declines. |
| Transparency | Privacy notice updated to describe fraud scoring, the data used and how to challenge a decline. |
| Data subject rights | Access and objection requests handled under the [DSAR playbook](../03-dsar-playbook/); objections to fraud screening are assessed case by case because fraud prevention is a compelling interest. |
| Processors | DeviceSure DPA signed (Art. 28), SOC 2 Type II report reviewed, no onward use of NovaPay data. |

## 5. Risks to individuals

| # | Risk | Likelihood | Severity | Inherent risk |
|---|---|---|---|---|
| R1 | Legitimate payments wrongly declined (false positives), causing financial hardship or embarrassment | Probable | Significant | **High** |
| R2 | Model bias: higher decline rates for cardholders in certain locations or using certain devices (proxy discrimination) | Possible | Significant | **High** |
| R3 | Cardholders unaware they are profiled or how to challenge a decline | Possible | Moderate | Medium |
| R4 | Device and IP data breached or reused for other purposes (e.g., marketing) | Remote | Significant | Medium |
| R5 | Data kept longer than needed for model training | Possible | Minimal | Low |

## 6. Measures to reduce risk

| Risk | Measures | Residual risk |
|---|---|---|
| R1 | Step-up authentication instead of decline for scores 60-89; decline threshold reviewed monthly; false-positive rate target under 0.1% of transactions; fast-track review for declined-payment complaints | Medium |
| R2 | Pre-launch and quarterly fairness testing of decline rates by region and device type; model features reviewed to remove obvious proxies; Model Risk Management validation before launch | Medium |
| R3 | Updated privacy notice; plain-language explanation on decline screens; support script for challenges | Low |
| R4 | Purpose limitation written into DPA and internal policy; access to features restricted to Fraud and Data Science roles; encryption at rest and in transit | Low |
| R5 | Automated deletion of model features after 13 months; training data snapshots documented | Low |

## 7. Residual risk and sign-off

| Decision | Detail |
|---|---|
| Residual risk | **Medium**: acceptable with the conditions below. No high residual risk remains, so prior consultation with a supervisory authority (Art. 36) is not required. |
| Conditions | (1) Fairness test results presented to the DPO before launch and quarterly. (2) False-positive rate reported monthly to the Risk Committee. (3) DPIA reviewed if the model adds new data types or moves from step-up to automatic declines at lower scores. |
| DPO advice | Approve with the conditions above. |
| Approved by | VP Fraud & Risk (risk owner) · Data Protection Officer |
| Next review | 12 months after launch, or on material change |

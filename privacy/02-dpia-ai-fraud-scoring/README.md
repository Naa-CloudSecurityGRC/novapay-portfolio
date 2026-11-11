# Data Protection Impact Assessment: AI Fraud Scoring

**Skills shown:** GDPR Article 35 DPIA, necessity and proportionality, legitimate interests, automated decision-making (Article 22), CPRA sensitive data, model fairness risk, residual-risk sign-off.

## Case study

| | |
|---|---|
| **Why I built this** | AI-driven decisions are a fast-growing privacy and governance risk; I wanted to show a structured assessment. |
| **Explain** | A privacy impact assessment for a machine-learning fraud score that can block payments. |
| **What was broken** | Two high risks: legitimate payments wrongly declined, and possible bias against certain locations or devices. |
| **What was fixed** | Step-up checks instead of declines for mid scores, fairness testing, human review on request, coarse location only. |
| **Business impact** | Residual risk reduced to medium and the project approved with conditions. |
| **Remediation still open** | Quarterly fairness results to the DPO; monthly false-positive reporting. |
| **Decisions and trade-offs** | I excluded precise GPS location: it's sensitive data under CPRA and city-level was enough for the model. |

## Details

NovaPay plans "SmartScore", a machine-learning fraud score using transaction, device and location data on ~40 million transactions a month. The DPIA finds two high inherent risks (wrongful declines and model bias), reduces both to medium with step-up authentication, fairness testing and a human review route, and approves the project with three conditions.

File: [DPIA_AI_Fraud_Scoring.md](DPIA_AI_Fraud_Scoring.md)

# Full-Population Journal Entry Testing (NovaPay FY2025)

**Evidence:** [step-by-step screenshots from build to remediation](EVIDENCE.md)

## Case study

| | |
|---|---|
| **Why I built this** | Sample-based SOX testing can miss the one bad journal entry. I wanted to show I can combine 10 years of SOX judgment with data skills to test 100% of a population. |
| **Explain** | Journal entries are where management override and errors hide. Instead of picking 25, I ran 6 SQL risk tests over all 24,000 entries. |
| **What was broken** | 198 high-risk manual entries, including 17 self-approved entries (a segregation-of-duties failure) and 42 entries sitting just under the $50k approval limit. |
| **What was fixed** | Traced the self-approvals to a disabled ERP approval block for one admin role; the block was re-enabled and the 6 tests became a monthly Controller review. |
| **Business impact** | Every risky entry gets reviewed, not just the lucky picks; the SoD gap was found before the external auditor found it. |
| **Remediation still open** | Review the 42 near-threshold entries for splitting; add the monthly report as a documented detective control (C09). |
| **Decisions and trade-offs** | I did not flag every round-dollar entry as an issue: many are legitimate accruals. I kept them as 'review' items and only escalated the SoD and threshold patterns. |

## Details

**Goal:** test 100% of journal entries for SOX/ICFR risk indicators, instead of a sample of 25-40.

## Results

| Test | Entries flagged | Amount ($) |
|------|----------------:|-----------:|
| Round-dollar manual JE >= $10k | 58 | 4,785,002 |
| Just below $50k approval threshold | 42 | 2,048,548 |
| Weekend manual posting | 38 | 391,521 |
| Posted to a closed prior period | 24 | 251,918 |
| Suspense account posting | 21 | 1,735,445 |
| Self-approved manual JE (segregation of duties) | 17 | 226,716 |

198 unique manual entries flagged out of 5,293 manual entries (3.7%). 2 entries hit more than one test.

**Control finding:** the 17 self-approved entries show the ERP approval block was not enforced for one role: a design deficiency in the key manual JE control (see project 2, deficiency D03).

## Files

| File | What it is |
|------|------------|
| `je_tests.sql` | The 6 SQL tests, commented |
| `NovaPay_JE_Full_Population_Testing.xlsx` | Summary (formulas), every exception, full population |
| `novapay_journal_entries_FY2025.csv` | Synthetic dataset, 24,000 lines |
| `generate_synthetic_je_data.py` | Builds the dataset (fixed random seed, reproducible) |
| `run_tests.py` | Loads the CSV into SQLite and runs the tests |
| `carousel_je_analytics.pdf` | Slide summary |

## Run it

```bash
cd 01-je-full-population-testing
pip install pandas numpy
python generate_synthetic_je_data.py
python run_tests.py
```

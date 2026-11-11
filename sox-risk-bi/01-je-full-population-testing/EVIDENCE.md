# Evidence: Full-Population Journal Entry Testing

From raw data to a fixed control, in the order the work was done.

> Screenshots are taken from the files in this repository. Data is fictional or simulated.

## Step 1 · Built: the full population

24,000 FY2025 journal entry lines loaded for testing (first rows shown).

![the full population](evidence/01_built.png)

## Step 2 · Built: the SQL risk tests

Six tests written in SQL; each one targets a known journal-entry risk.

![the SQL risk tests](evidence/02_built.png)

## Step 3 · Broken: what the tests found

198 unique manual entries flagged across the six tests.

![what the tests found](evidence/03_broken.png)

## Step 4 · Broken: the segregation-of-duties failures

17 manual entries posted and approved by the same person.

![the segregation-of-duties failures](evidence/04_broken.png)

## Step 5 · Fixed: control finding and remediation

Root cause: ERP approval block disabled for one admin role. Logged as deficiency D03, remediated and validated.

![control finding and remediation](evidence/05_fixed.png)

## Step 6 · Remediation: tests become a monthly control

The six tests now feed control C09, the Controller's monthly review of risky manual entries.

![tests become a monthly control](evidence/06_remediation.png)

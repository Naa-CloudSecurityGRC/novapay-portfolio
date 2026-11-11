-- NovaPay FY2025 | Full-population journal entry testing (SOX / ICFR)
-- Dataset: novapay_journal_entries_FY2025.csv loaded as table je (synthetic data)
-- Approval threshold for manual JEs: $50,000 (dual approval above)

-- T1: Manual JEs posted on a weekend
SELECT 'T1 Weekend manual posting' AS test, je_id, post_date, account, amount, posted_by, approved_by
FROM je WHERE source='Manual' AND strftime('%w', post_date) IN ('0','6');

-- T2: Self-approved manual JEs (segregation of duties)
SELECT 'T2 Self-approved (SoD)' AS test, je_id, post_date, account, amount, posted_by, approved_by
FROM je WHERE source='Manual' AND posted_by = approved_by;

-- T3: Just below the $50,000 approval threshold (95-100% of limit)
SELECT 'T3 Just below approval threshold' AS test, je_id, post_date, account, amount, posted_by, approved_by
FROM je WHERE source='Manual' AND amount >= 47500 AND amount < 50000;

-- T4: Round-dollar manual JEs >= $10,000
SELECT 'T4 Round-dollar >= $10k' AS test, je_id, post_date, account, amount, posted_by, approved_by
FROM je WHERE source='Manual' AND amount >= 10000 AND amount % 1000 = 0;

-- T5: Postings to the suspense account
SELECT 'T5 Suspense account posting' AS test, je_id, post_date, account, amount, posted_by, approved_by
FROM je WHERE account LIKE '1999%';

-- T6: Late posting to a prior (closed) period: posted after day 5 of the following month
SELECT 'T6 Posted to closed period' AS test, je_id, post_date, account, amount, posted_by, approved_by
FROM je WHERE gl_period < substr(post_date,1,7) AND CAST(strftime('%d', post_date) AS INT) > 5;

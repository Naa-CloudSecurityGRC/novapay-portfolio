# Framework Crosswalk: Test Once, Satisfy Many

**Skills shown:** fluency in NIST CSF 2.0, ISO/IEC 27001:2022, SOC 2 and PCI DSS v4.0; control rationalization; evidence planning.

## Case study

| | |
|---|---|
| **Why I built this** | Companies face several frameworks at once; I wanted to show 'test once, satisfy many'. |
| **Explain** | 30 controls mapped across NIST CSF 2.0, ISO 27001, SOC 2 and PCI DSS, each with one piece of evidence. |
| **What was broken** | Separate audits asking for the same evidence in different formats. |
| **What was fixed** | One control set, one evidence item per control; 26 of 30 controls satisfy all four frameworks. |
| **Business impact** | Less audit fatigue for control owners and lower audit cost. |
| **Remediation still open** | Validate mappings against official texts before relying on them. |
| **Decisions and trade-offs** | I mapped CSF at category level, not subcategory, to keep it maintainable. |

## Details

30 NovaPay controls mapped across four frameworks, with the single piece of evidence that serves all of them.

| Result | Value |
|---|---:|
| Controls mapped | 30 |
| Controls covering all 4 frameworks | 26 |
| Average frameworks per control | 3.9 |

**Why it matters:** NovaPay faces SOC 2 (customers), PCI DSS (card brands), and ISO 27001 / NIST CSF expectations (bank partner). Testing each control once and reusing the evidence avoids three separate audit efforts.

**Mapping approach:** NIST CSF 2.0 at category level; ISO 27001:2022 Annex A control numbers; SOC 2 Common Criteria and Availability; PCI DSS v4.0 at requirement level. Coverage by CSF function is on the Coverage tab.

File: [Framework_Crosswalk.xlsx](Framework_Crosswalk.xlsx)

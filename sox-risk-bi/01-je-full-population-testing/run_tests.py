import pandas as pd, sqlite3, re
d=pd.read_csv("novapay_journal_entries_FY2025.csv")
con=sqlite3.connect(":memory:"); d.to_sql("je",con,index=False)
sql=open(__import__("os").path.join(__import__("os").path.dirname(__file__),"je_tests.sql")).read()
stmts=[s.strip() for s in sql.split(";") if "SELECT" in s]
res=pd.concat([pd.read_sql(re.sub(r"^(--.*\n)+","",s),con) for s in stmts])
res.to_csv("je_exceptions.csv",index=False)
print(res.groupby("test").agg(n=("je_id","count"),amt=("amount","sum")))
print("unique JEs flagged",res.je_id.nunique(),"multi-flag",(res.je_id.value_counts()>1).sum())
print(res.groupby("posted_by").je_id.nunique().sort_values(ascending=False).head(5))

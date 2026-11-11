import numpy as np, pandas as pd, sqlite3, datetime as dt
rng=np.random.default_rng(42)
N=24000
users=[f"U{i:03d}" for i in range(1,41)]
approvers=[f"A{i:02d}" for i in range(1,9)]
accts={"1010 Cash - Operating":"Asset","1200 Card Receivables":"Asset","1250 Chargeback Receivable":"Asset","1300 Settlement Clearing":"Asset","1999 Suspense":"Asset","2100 Merchant Payables":"Liability","2300 Accrued Expenses":"Liability","2450 Chargeback Loss Reserve":"Liability","4000 Interchange Revenue":"Revenue","4100 Processing Fee Revenue":"Revenue","5000 Network Fees":"Expense","5200 Fraud & Chargeback Losses":"Expense","6100 Payroll":"Expense","6400 Professional Fees":"Expense"}
days=pd.date_range("2025-01-01","2025-12-31")
wd=days[days.dayofweek<5]
d=pd.DataFrame({
 "je_id":[f"JE{100000+i}" for i in range(N)],
 "post_date":rng.choice(wd,N),
 "account":rng.choice([a for a in accts if not a.startswith("1999")],N),
 "source":rng.choice(["Automated","Manual"],N,p=[0.78,0.22]),
})
d["amount"]=np.round(np.exp(rng.normal(8.2,1.6,N)),2)
d["posted_by"]=np.where(d.source=="Automated","SYS_BATCH",rng.choice(users,N))
d["approved_by"]=np.where(d.source=="Automated","AUTO",rng.choice(approvers,N))
# GL period = month of post date by default
d["gl_period"]=d.post_date.dt.strftime("%Y-%m")
man=d.index[d.source=="Manual"]
def pick(k): return rng.choice(man,k,replace=False)
# anomalies
i=pick(38); d.loc[i,"post_date"]=rng.choice(days[days.dayofweek>=5],len(i)); d.loc[i,"gl_period"]=pd.to_datetime(d.loc[i,"post_date"]).dt.strftime("%Y-%m")
i=pick(55); d.loc[i,"amount"]=rng.choice([10000,25000,50000,75000,100000,250000],len(i)).astype(float)
i=pick(17); d.loc[i,"approved_by"]=d.loc[i,"posted_by"]
i=pick(29); d.loc[i,"amount"]=np.round(rng.uniform(47500,49999.99,len(i)),2)
i=pick(21); d.loc[i,"account"]="1999 Suspense"; d.loc[i,"amount"]=np.round(rng.uniform(5000,180000,len(i)),2)
# late postings: posted >5 business days after month end to prior period
i=pick(24)
r=pd.date_range("2025-02-08","2025-12-28"); r=r[(r.dayofweek<5)&(r.day>=8)]; pd_=pd.to_datetime(rng.choice(r,len(i)))
pd_=[x if x.day>=8 else x+pd.Timedelta(days=8) for x in pd_]
d.loc[i,"post_date"]=pd_
d.loc[i,"gl_period"]=[(x.replace(day=1)-pd.Timedelta(days=1)).strftime("%Y-%m") for x in pd_]
d["post_date"]=pd.to_datetime(d.post_date).dt.strftime("%Y-%m-%d")
d["account_type"]=d.account.map(accts)
d=d.sort_values(["post_date","je_id"])
d[["je_id","post_date","gl_period","account","account_type","amount","source","posted_by","approved_by"]].to_csv("novapay_journal_entries_FY2025.csv",index=False)
print(len(d), d.source.value_counts().to_dict())

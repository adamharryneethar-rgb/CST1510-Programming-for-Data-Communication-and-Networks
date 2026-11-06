"""
RECORD CHECK  -  my version
===========================

Name  : Adam Harry
Lane  :  AI 
Date  :6/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

df =pd.read_csv("C:\Users\M01143732\Downloads\Week 06 - Pandas\Week 06 - Pandas\LAB\records_sample.csv")

value["percent"] = (value["value"] / value["limit"]) * 100
value["status"]=value["percent"].apply(lambda p:"overlimit" if p>=100 else 'warning'if p>=90 else "ok")

print(df)
print(df[(df["status"]!="ok")])
avg=df.groupby("status").size()
print(avg)
df.to_csv("status.csv", index=False)
import matplotlib.pyplot as plt
avg.plot(kind="bar")
plt.title("Status")
plt.savefig("status_counts.png")
plt.show()
# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case

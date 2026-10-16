"""
RECORD CHECK  -  my version
===========================

Name  :Adam Harry
Lane  :  AI
Date  :16/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check(value,limit):

    if value>limit:

      return "over limit"
    else:
      return "ok"
def percent(value, limit):
    percentage=(value/limit)*100
    diff= value-limit
    return percentage, diff


def print_report(dataset, rowloaded, rowsexcepted,
                 diff, percentage, status):
  print("*"*34)
  print(f"Dataset Name- {dataset}")
  print("*"*34)
  print(f"Rows Loaded: {rowloaded:>10}")
  print(f"Rows Excepted {rowsexcepted:>10}")
  print(f"Free: {diff:>10}")
  print(f"Percentage:{percentage:>10.2f} %")
  print(f"Status:{status:>10}")

  print("*"*34)
  print("*"*34)

rowloaded= int(input("Enter the rows loaded:"))
rowsexcepted=int(input("Enter the rows excepted:"))

percentage,diff=percent(rowloaded,rowsexcepted)
status=check(rowloaded,rowsexcepted)

print_report(dataset, rowloaded, rowsexcepted,
                 diff, percentage, status)



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : als((o write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = [
       {"label": "R-001", "value": 87.0, "limit": 100.0},
       {"label": "R-002", "value": 120.0, "limit": 100.0},
       {"label": "R-003", "value": 45.0, "limit": 100.0},]
def loadpath(path):
   dict=[]
   with open(path,"r") as f:
      for i in f:
        label,value,limit=i.strip().split(",")
        dict.append(label, float(value),float(limit))
        return dict
def check(value,limit):

    if value>limit:

      return "over limit"
    else:
      return "ok"
loadpath("sample.txt")
results = check(value,limit)
for label, limit in result:
   print(label,limit)
with open ("sample.txt","w") as ad:
   for label,limit in results:
      file.write(label,limit\n)


        
         



# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
def check(value,limit):

    if value>limit:

      return "over limit"
    else:
      return "ok"
def print_report(dataset, rowloaded, rowsexcepted,
                  status):
  print("*"*34)
  print(f"Dataset Name- {dataset}")
  print("*"*34)
  print(f"Rows Loaded: {rowloaded:>10}")
  print(f"Rows Excepted {rowsexcepted:>10}")
  print(f"Status:{status:>10}")

  print("*"*34)
  print("*"*34)
while True:

  dataset=input("Enter the record ID:")
  if dataset=="quit":
    break
  rowloaded= int(input("Enter the rows loaded:"))
  rowsexcepted=int(input("Enter the rows excepted:"))

  status=check(rowloaded,rowsexcepted)

  print_report(dataset, rowloaded, rowsexcepted,
                 status)
  if status=="over limit":
    over=over+1
print(f"overlimit: {over}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job

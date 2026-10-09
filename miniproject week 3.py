"""
RECORD CHECK  -  my version
===========================

Name  : Adam Harry Neethar
Lane  :  AI 
Date  :09/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



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
over=0
while True:
  
  dataset=input("Enter the record ID:")
  if dataset=="quit":
    break
  rowloaded= int(input("Enter the rows loaded:"))
  rowsexcepted=int(input("Enter the rows excepted:"))

  percentage,diff=percent(rowloaded,rowsexcepted)
  status=check(rowloaded,rowsexcepted)

  print_report(dataset, rowloaded, rowsexcepted,
                 diff, percentage, status)
  if status=="over limit":
    over=over+1
print(f"overlimit: {over}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it

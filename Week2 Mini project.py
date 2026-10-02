"""
RECORD CHECK  -  my version
===========================

Name  :Adam Harry Neethar
Lane  :  AI    (delete two)
Date  :2/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
over=0
while True:

  #threshold
  data_name=input("Enter the data set name:")
  if data_name=="quit":
    break
  rows_loaded=int(input("Enter the rows loaded:"))
  rows_excepted=int(input("Enter the rows excepted:"))
  print("*"*30)
  print(f"DataSet Name:{data_name}")
  print("*"*30)
  print(f"rows loaded :{rows_loaded}")
  print(f"rows excepted: {rows_excepted }")


  if rows_loaded>rows_excepted:
    print(f"Status: OK")
  print("*"*30)

  #typical
  print("*"*30)
  print(f"DataSet Name:{data_name}")
  print("*"*30)
  print(f"rows loaded :{rows_loaded:.2f}")
  print(f"rows excepted: {rows_excepted:.2f}")
  print(f"Free: {rows_excepted-rows_loaded:.2f}")
  per= (rows_loaded/rows_excepted)*100
  print(f"Percentage:{per:.2f}")
  if per>100:
    over=over+1
    print("Status: Overtime")
  elif per<90 and per>100:
    print("Status: Warning")
  else:
    print("Status: Ok")
  print("*"*30)
  print(over)
  



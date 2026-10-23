"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit
    def percent(self):
        return (self.value/self.limit)*100
        
    def status(self):
        per=self.percent()
        if per>=100:
            return "OVERLIMIT"
        elif per>90 :
            return "WARNING"
        else:
            return "OK"
    def is_over(self):
        return self.status() == "OVERLIMIT"
def loadd(path):
        records=[]
        with open(path,"r") as f:
            for i in f:
                label, value, limit = i.strip().split(",")
                records.append(Record(label, float(value), float(limit)))
        return records
count=0
load= loadd("C:/Users/M01143732/Downloads/Week 05 - Classes and Objects/Week 05 - Classes and Objects/LAB/records_sample.txt")
for i in load:
    if i.is_over():
        count+=1


for record in load:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Value: {record.value}")
    print(f"Limit: {record.limit}")
    print(f"percent: {record.percent()}%")
    print(f"status: {record.status()}")
    print("=" * 34)
print("The number of overlimit",count)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring

"""
RECORD CHECK  -  my version
===========================

Name  :Ntihemuka Migambi Darren
Lane  :  AI 
Date  :23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""




class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def summary(self):
        return f"{self.label} : {self.value}/{self.limit}"

    def percent(self):
        return (self.value)/(self.limit)*100

    def status(self):
        if self.percent() > 100.0:
            return "OVER LIMIT"
        elif self.percent() >= 90.0:
            return "Warning"
        else:
            return "OK"
def load_records(path):
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            record = Record(label, int(value), int(limit))
            records.append(record)
    return records
records = load_records("C:/Users/PC/OneDrive/Python MDX/Week 05 - Classes and Objects/LAB/Class_temp.txt")
over_limit_count = 0
for record in records:
     print()
     print("=" * 34)
     print(f"  RECORD CHECK  -  {record.label}")
     print("=" * 34)
     print(f"{record.summary()},{record.status()}")
     if record.status() == "OVER LIMIT":
        over_limit_count += 1
     print(f"Over limit counts : {over_limit_count}")
     
     print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring

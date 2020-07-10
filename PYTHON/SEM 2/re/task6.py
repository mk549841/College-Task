import re
a=input("ENter float number")
r=re.match(r'\d+.\d+',a)
if r:
    print("Correct FOrmat")
else:
    print("Incorrect")

import re
a=input("Enter roll")
e=re.findall(r'[1-9]+[1-9]+[A-Z]+[1-9]+[1-9]+[1-9]',a)
if e==[a]:
    print("Found")

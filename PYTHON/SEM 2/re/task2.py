a=input("ENter string")
import re
r1=re.findall("\d+",a)
print(max(map(int,r1)))

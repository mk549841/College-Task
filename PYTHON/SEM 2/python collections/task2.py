from collections import defaultdict
import math
c=0
s=input("Enter the String without White space")
li=[]
li2=[]
d=defaultdict(int)
for i in s:
    d[i]+=1
for i,j in d.items():
    li.append(j)
for i in li:
    if i>=2:
        li2.append(i)
for i in range(len(li2)):
    c=c+math.factorial(li2[i])
x=len(s)

print("Total possible is {}".format(int(math.factorial(x)/c)))

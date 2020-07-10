li=[]
li2=[]
n=eval(input("Enter the no of inputs"))
for i in range(n) :
    li.append(eval(input("Enter the value")))
for j in range(n):
    li[j]=li[j]*5
for k in range(n):
    li2.append(li.count(li[k]))
for k in range(n):
    print(li[k],'-',li2[k])

for k in range(n-5,n):
    print("Lastfive",li[k],'-',li2[k])
li.sort()
for k in range(n-5,n):
    print("Sorted Element are..",li[k])
print("Second Largest is",li[-2])
print("Smallest Element is ",li[0])

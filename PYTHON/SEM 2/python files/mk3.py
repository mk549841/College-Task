try:
    fp1=open("mk.txt",'r')
    li=fp1.read().split()
    li2=set(li)
    for i in sorted(li2):
        print(i,':',li.count(i))
except Exception as e:
    print(e)
        

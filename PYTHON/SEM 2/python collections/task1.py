from collections import OrderedDict
import re
li=[]
a=OrderedDict()
x=int(input("Enter how many records"))
for i in range(x):
    li.append((input(),int(input())))
li1=OrderedDict(li)
a=int(input("Enter any key to check value exists or not"))
for key in li1.values():
    print(key)
    if key==a:
        print("Value found {}".format(key) )
    

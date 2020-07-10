'''
Created on 23-Nov-2018

@author: student
'''
import threading
import random
def fun(string,n):
    for i in range(len(string)):
        a=random.randrange(1,n)
        if(string[a-1]=='red'):
            break
        elif string[a-1] not in string[i]:
            print(string[i])
li=[]
n=int(input("Enter n"))
for i in range(n):
    li.append(input("Enter the colour "))
t=threading.Thread(target=fun,args=(li,n,))
t.start()
t.join()

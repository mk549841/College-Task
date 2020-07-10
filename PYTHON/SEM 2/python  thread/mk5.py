'''Create two threads, one thread to display all even numbers between 1 & 20, another to display
odd numbers between 1 & 20.
Note: Display all even numbers followed by odd numbers
Hint: use join'''

import threading
from time import sleep
def fun(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)
def fun1(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i)
n=int(input("Enter the n"))
t=threading.Thread(target=fun,args=(n,))
t1=threading.Thread(target=fun1,args=(n,))
print("Even nos are ")
t.start()
t.join()
print("odd nos are ")
t1.start()
t1.join()

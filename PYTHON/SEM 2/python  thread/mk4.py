'''Create a thread which prints 1 to 10. After printing 5, there should be a delay of 5000
milliseconds before printing 6'''

import threading
from time import sleep
def fun(n):
    for i in range(n):
        if i==6:
            sleep(5)
        print(i)
    print(n)
n=int(input("Enter the n"))
t=threading.Thread(target=fun,args=(n,))
t.start()

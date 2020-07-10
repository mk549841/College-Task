import math
class error(Exception):
    def prin():
        print("Negative value")
def fact(n):
    print("Factorial")
    print(math.factorial(n))
def fibo(x):
    print("Fibb series")
    a=0
    b=1
    c=0
    print(a)
    print(b)
    while(a<=x):
        c=a+b
        print(c)
        a=b
        b=c
def check(fun):
    print('going to check positive or negative')
    fun(int(input('enter the value')),int(input('enter the value')))
@check
def funcheck(x,y):
    try:
        if x>0 and y>0:
            fact(x)
            fibo(y)
        else:
            raise error
    except error as y:
        y.prin()
        
        

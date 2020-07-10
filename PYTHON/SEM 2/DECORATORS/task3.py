import math
class d_c(object):
    def __init__(self,fun):
        self.fun=fun
        print('going to check positive or negative')
    def __call__(self,a):
        try:
            if(a>0):
                return self.fun(a)
            else:
                raise Exception("Negative Value")
        except Exception as e:
            print(e)

@d_c
def fact(n):
    print("Factorial")
    print(math.factorial(n))
@d_c
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
fact(int(input("Enter Value")))
fibo(int(input('Enter value')))



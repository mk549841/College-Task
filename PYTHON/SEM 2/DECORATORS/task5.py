class mk(object):
    def __init__(self,fun):
        self.fun=fun
    def __call__(self,a,b):
        return self.fun(a,b)
global bal
bal=25000
@mk
def bank(damt,wamt):
    global bal
    x=input("1(Deposit) or 2(Withdraw)")
    if  x=="1":
        y=int(input("How much"))
        bal=bal+y
    if x=="2":
        y=int(input("How much"))
        bal=bal-y
    print("{} YOur Final balance ".format(bal))
    
    print("Do u want again this process?")
    t=input('Enter y or n ')
    if t=="y":
        bank(0,0)
    else:
        print("Thank you")
bank(0,0)
    

















global bal
bal=25000
class SBI:
    def __init__(self,damt,wamt):
        self.bal=bal
        self.damt=damt
        self.wamt=wamt
    def dep(self,damt):
        global bal
        damt1=int(input('Enter Money to Deposit'))
        bal=bal+damt1
        print(bal)
        i=input("Do u want withdraw?? y/n")
        if i=='y':
            self.wid(bal)
        else:
            print("Thank you")
            self.display()
    def wid(self,ba):
        global bal
        w=int(input('Enter Money to Withdraw'))
        bal=ba-w
        print(bal)
        i=input("Do u want deposit?? y/n")
        if i=='y':
            self.dep(bal)
        else:
            print("Thank you")
            self.display()
    def c(self):
        global bal
        print("Want do u want Deposit(click 1) or Withdraw(click 2)")
        x=int(input('Enter'))
        if (x==1):
            self.dep(bal)
        if(x==2):
            self.wid(bal)
    def display(self):
        print("Your balance is",self.bal)       
obj=SBI(0,0)
obj.c()
        

class Fund(Exception):
    def a1(self):
        print('InSufficientFund')
class Balance(Exception):
    def a2(self):
        print('InSufficientBalance')
b=int(input('enter the amount to be deposited'))
try:
    a=int(input('ENTER THE AMOUNT TO BE WITHDRAWED'))
    if (b-a) < 0:
        raise Fund
    else:
        b-=a
    if b<500:
        raise Balance
    print('BALANCE AMOUNT IS',b)
except Balance as e:
    e.a2()
except Fund as e:
    e.a1()

def prime(fun):
    fun(int(input('Enter starting value')),int(input("Enter stop value")))
@prime
def prin(m,m1):
    li=[]
    for i in range(m,m1+1):
        c=0
        for j in range(2,(i//2+1)):
            if i %j==0:
                c=c+1
        if (c==0 and i!=1):
            li.append(i)
    for i in li:
        if(i%5!=3):
            print(i)

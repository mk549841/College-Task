c1=0
c2=0
c3=0
c4=0
n=input("Enter the password")
if len(n)>=6 or len(n)<=25:
    for i in range(len(n)):
        if (n[i].isdigit()==True):
            c1=c1+1
        elif (n[i].isupper()==True):
            c2=c2+1
        elif (n[i].islower()==True):
            c3=c3+1
        elif n[i]=='$' or n[i]=='@' or n[i]=='#' :
            c4=c4+1
if c1>0 and c2>0 and c3>0 and c4>0:
    print("Valid password")
else:
    print("invalid...try again")

          

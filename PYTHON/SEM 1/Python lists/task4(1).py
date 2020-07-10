c1=0
c2=0
c3=0
c4=0
n=input("Enter the password")
if len(n)>=6 or len(n)<=12:
    for i in range(len(n)):
        if ord(n[i]) >=97 and ord(n[i])<=122:
            c1=c1+1
        elif ord(n[i])>=65 and ord(n[i])<=90:
            c2=c2+1
        elif ord(n[i])>=48 and ord(n[i])<=57:
            c3=c3+1
        elif n[i]=='$' or n[i]=='@' or n[i]=='#' :
            c4=c4+1
if c1>0 and c2>0 and c3>0 and c4>0:
    print("Valid password")
else:
    print("invalid...try again")

first=0
b=eval(input("Enter the limit"))
neg=-1
for i in range(b):
    a=eval(input("Enter the Number"))
    if (a>first):
        print(neg)
    else :
        print(first)
    first=a

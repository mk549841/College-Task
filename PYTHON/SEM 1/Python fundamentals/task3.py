a=eval(input("Enter The Size:"))
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end =" ")
    print()
for k in range(6,1,-1):
    for l in range(1,k-1):
        print("*",end =" ")
    print()

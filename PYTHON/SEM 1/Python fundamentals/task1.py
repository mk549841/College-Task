a=input("Enter the Number")
count=0
for i in range(10):
    for j in range(len(a)):
        if i== int(a[j]):
            count=count+1
            print(i,'-',count)
        
        count=0

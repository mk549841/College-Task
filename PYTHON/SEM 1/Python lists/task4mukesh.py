li=[]
li1=[]
for i in range (1,11):
    x=eval(input("Enter The nUmber"))
    if(x%2==0 or x % 3 ==0 or x%5 ==0):
        li.append(x)
    else:
        li1.append(x)
print("Ugly number is",li)
print("Non Ugly number is",li1)


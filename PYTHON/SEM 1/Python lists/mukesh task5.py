mk1=[]
mk2=[]
count=0
n=eval(input("Enter the n value to chack the prime numbers"))
for i in range(1,n):
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        mk1.append(i)
    count=0

for i in range(1,n):
    mk2.append(i*5)
val=input('Type prime or multiply')
if(val=='prime' or val=='PRIME'):
    print(mk1)
elif(val=='multiply' or val=='MULTIPLY'):
    print(mk2)
else:
    print('invalid')

list1=[ ]
list2=[  ]
list3=[   ]
list4=[ ]
tup=tuple()
nl=[]
count=0
su=0
n=eval(input("No of machine"))
for i  in range (n):
    list1.append(input("Enter the machine name "))
    list4.append(eval(input("Enter the price range please")))
    list2.append(i)
    list3.append(eval(input("Enter the  machine quantity")))
for i in range(n):
    print('serial nos is','=',list2[i],'machineis','=',list1[i],'qunatity is',list3[i])
nl=list1,list4
#print(nl)
for i in range (n):
    if list3[i]>3 :
        print(list1[i])
print(" The number of machines in company")
print(len(list2))
if 'superdrill' in list1:
    print("Superdrill is here ;)")
else:
    print("Super drill is not found")
print("The maximum no of machine is ",list1[list3.index(max(list3))])
print("The minimum no of machine is ",list1[list3.index(min(list3))])
for i in range(n):
    su=su+list3[i]
print('Total number of machineries',su)
list1.sort()
print(" The machineries name in ascending order is",list1)

    

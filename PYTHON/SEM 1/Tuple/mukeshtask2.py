tuple1=[ ]
tuple2=[ ]
tuple3=[ ]
c=[ ]
d=[ ]
e=[ ]
n=eval(input("ENter the n value"))
for i in range (n):
    tuple1.append(eval(input("enter the element")))
for i in range (len(tuple1)):
                  tuple2.append(eval(input("Enter the element for tuple2")))
for i  in range (len(tuple2)):
                tuple3.append(eval(input("Enter the element  for tuple 3")))
print('Sorted tuples is........ ')
tuple1.sort()
c=tuple1
tuple2.sort()
d=tuple2
tuple3.sort()
e=tuple3               
print(tuple(zip(c,d,e)))
print("The maximum of tupple one",max(tuple1))
print("The maximum of tupple two",max(tuple2))
print("The maximum of tupple three",max(tuple3))
print("The manimum of tupple one",min(tuple1))
print("The manimum of tupple two",min(tuple2))
print("The manimum of tupple three",min(tuple3))

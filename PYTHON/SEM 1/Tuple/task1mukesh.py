'''In a school, a teacher has to create a list of students and their class subjects. Each staff is given
only one class so that the list of students and subjects will not change (no modification and
deletion).'''
name=()
sub=()
list1=[ ]
sub=0
list2=[]
roll=0
lastlist=[]
list3=[]
c=0
count=0
abc=[]
tu=tuple()
n=eval(input("Enter the n value"))
for i in range(n):
    nam=input("Enter the students name")
    sub=input("Enter the subject")
    list1.append(nam)
    list2.append(sub)
for i in range (n):
    roll=eval(input('Enter the roll nos'))
    list3.append(roll)
lastlist=[  roll,list1  ]
tu=tuple()
for i  in range (n):
    if(list1[i][0]=='a'):
        print('             ')
        print("The name  start with a is...",list1[i])
c=len(list1)
print(                    )
print("The  number of students in student_name_tup ",c)
print()
for i in range (n):
    if(list2[i]=="maths"):
        print('Maths subject is available ')
	count=count+1
print(count)
print("Now display the each student’s name along with their subjects they are studying")
print('                                   ')
zip(list1,list2)
tu=tuple(zip(list1,list2))
print(tu)
    
    
    

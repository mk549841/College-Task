import collections
li=[]
n=int(input("Enter how many  records upto "))
u=collections.namedtuple('User','Name Age Height')
for i in range(n):
    li.append(u(input(),int(input("Enter age")),int(input("Enter Heigth"))))
for i in sorted(li):
    print(i)


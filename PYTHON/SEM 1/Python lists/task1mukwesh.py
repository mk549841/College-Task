list2=[]
a=[['East Khasi','Lower Dibang valley','East Ssiang','Chiranjg','kokrajhar']]
b=[['Assam and Ghalaya','Arnacahl Pradesh','Arnacahl Pradesh','assam and maghalaya','assam and maghalkaya']]
c=[[5790.7,3581,3309,3219,3020]]
d=[[4277.2,888.4,2661.4,2048.0,2544.1]]
e=[[35,303,24,57,19]]
print(a[0][1],',',b[0][1],',',b[0][1],',',d[0][1],',',e[0][1])
print(b[0][0],b[0][1])
print(a[0][4])
print(5* a[0][4])
print(a[0][2]+a[0][3])

#Answer B
if (d[0][0]==4277.2):
    print("YES  normal value in List District_1 is 4277.2")
else:
    print("NO normal value in List District_1 is 4277.2 ")
if (e[0][1]==26):
    print("YES    variance is 26 in  District_2")
else:
    print("no    variance is 26 in  District_2")

#Answer c
a[0].remove('East Ssiang')
print(a[0][3],b[0][4],c[0][4],d[0][4],e[0][4])

#answer d
a[0][1]='Nilgris'
e[0][4]=68

#answer e
print("The length of dist 1")
print(len(a[0]))
print("The lenght of dist 5")
print(len(d[0]))
print(a[0])

#answer g and h
print('district 1',all(a[0][0]))
print('district 2',all(a[0][1]))
print('district 4',any(a[0][2]))
print('district 5',all(a[0][3]))

#answer i
list1=[a[0][2],b[0][2],c[0][2],d[0][2],e[0][2]]
list3=list1
list2=[a[0][3],b[0][4],c[0][4],d[0][4],e[0][4]]
list4=list2
print(list3)
print(list4)


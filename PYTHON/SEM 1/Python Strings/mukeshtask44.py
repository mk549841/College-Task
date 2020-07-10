string=input("enter the stringto remove duplicate      ")
string=string.split(" ")
string=list(string)
li=[]
for i in range(len(string)):
    if (string[i] not in li):
               li.append(string[i])
p=sorted(li)
print("Sorted order is .....")
print(p)

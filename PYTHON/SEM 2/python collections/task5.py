from collections import defaultdict
c=c1=0
s=defaultdict(lambda:'key not found')
s=[{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3,
'success': True, 'name': 'Alex'}]
x=input("Enter key")
y=bool(input("ENter value"))
for i in range(len(s)):
    for j,j1 in s[i].items():
        if (j,j1)==(x, y):
            c=c+1
        elif (j,j1)!=(x,y):
            c1+=c1
if c1>=1 or c==0:
    print('Key not found')
else:
    print(s[x])

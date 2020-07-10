import collections
name=collections.deque(input('Enter the string'))
print('deque,:',name)
s=''
s1=''
name1=collections.deque()
for i in name:
    if str(i)!='#':
        name1.append(i)
    else:
        name1.pop()
print(name1)
for i in range(len(name1)):
    s1=str(name1.popleft())
    s=s+s1
print('New string is {}'.format(s))

import re
s=' '
text=input("ENter string")
l=re.findall("[A-Z][^A-Z]*",text)
print(' '.join(l))


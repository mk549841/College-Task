str1=input("Enter the input string")
b=" "
c=" "
d=" "
if(len(str1)<3):
    print(-1)
else:
    b=str1[0:2]
    c=str1[len(str1)-2::1]
    d=b+c
    print(d)
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    print(str1)

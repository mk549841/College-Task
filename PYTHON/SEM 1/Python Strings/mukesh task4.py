a=input("Enter the input string")
f=" "
g=" "
if a[-3:] == 'ing':
    b=a[-3:]
    c=a[0:len(a)-3:1]
    b=b.replace("ing","ly")
    d=c+b
    print(d)
else:
    if a.find('not') and a.find('poor'):
        if a.index('not') < a.index('poor'):
            a=a.replace(a[a.find("not"):a.find("poor")+4],"good")
            print(a)
                                

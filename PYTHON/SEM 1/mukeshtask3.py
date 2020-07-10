def text():
    x,y=0,0
    n=int(input("Enter the no of lines"))
    li=[]
    fp=open('from.txt','r')
    for i in range(n):
        li=li+(fp.readline())[:-1].split()
    li=list(set(li))
    fp.close()
    fp1=open('vowelssample.txt','w')
    fp2=open('consonantscopy.txt','w')
    for i in range(len(li)):
        if li[i][0] in ['a','e','i','o','u','A','E','I','O','U']:
            fp1.write(li[i])
            fp1.write('-')
            fp1.write(str(x))
            x=x+1
            fp1.write(' ')
        else:
            fp2.write(li[i])
            fp2.write('-')
            fp2.write(str(y))
            y=y+1
            fp2.write(' ')
    print(x+y)
    fp1.close()
    fp2.close()
text()

li=[]
n=0
def fn_write():
    fp=open("number.txt",'w')
    n=int(input("Enter the number of values"))
    for i in range(n):
        fp.write(input())
    fp.close()
def fn_read():
    fp=open("number.txt",'r')
    for i in fp.read():
        li.append(i)
    fp.close()
def dup():
    k=0
    fp=open("result.txt",'w')
    for i in range(len(li)):
        print(li[:k+1].count(li[i]))    
        if li[:k+1].count(li[i])%2==0 :
            fp.write('no beep\n')
        else:
            fp.write('beep\n') 
        k=k+1
    fp.close()       
fn_write()
fn_read()
dup()
fp=open("result.txt",'r')
for i in range(len(li)):
        print(fp.readline())
fp.close()

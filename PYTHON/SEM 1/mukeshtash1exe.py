class nonintError(Exception):
    def pt(self,i):
        print("You entered a Non Integer value")
li=[]
def call(*arg):
    try:
        for i in arg:
            if i.isdigit():
                if int(i) not in li:
                    li.append(int(i))
            else:
                raise nonintError
        print(li)
    except nonintError as e:
        e.pt()

l1=[]
for i in range(int(input('Enter the n'))):
    l1.append(input("Enter the value for n number"))
call(*l1)

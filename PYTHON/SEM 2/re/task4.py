import re 
p =input("Enter password")
flag = 0
while(1):   
    if (len(p)<4 and len(p)>16): 
        flag = -1
        break
    elif not re.search("[a-z]", p): 
        flag = -1
        break
    elif not re.search("[A-Z]", p): 
        flag = -1
        break
    elif not re.search("[0-9]", p): 
        flag = -1
        break
    elif not re.search("\W+", p): 
        flag = -1
        break
    elif re.search("\s", p): 
        flag = -1
        break
    else: 
        flag = 0
        print("Valid password") 
        break
if flag ==-1: 
    print("Not a Valid password") 

try:
    fp=open("mukesh.txt",'w')
    print("Enter the content")
    fp.write(input())
    fp.close()
    fp=open("mukesh.txt",'r')
    char=str(input("Enter the character want to count"))
    import re
    if char.isupper():
        char=char.casefold()
    string=fp.read().casefold()
    print(len(re.findall(char,string)))
    fp.close()
except Exception as e:
    print(e)  
        

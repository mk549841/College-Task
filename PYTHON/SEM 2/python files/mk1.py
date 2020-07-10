try:
    fp=open("original.txt","w+")
    fp.write(input("Enter content"))
    fp1=open("copy.txt","w+")
    fp.seek(0,0)
    fp1.write(fp.read())
    fp1.seek(0,0)
    print(fp1.read())
    fp.close()
    fp1.close()
except Exception as e:
    print(e)  

string=input("Enter string:")
if(string==string[::-1]):
      print("The string is a palindrome")
else:
    count1=0
    count2=0
    count3=0
    count4=0
    for i in string:
      if(i.islower()):
          count1=count1+1
      elif(i.isupper()):
            count2=count2+1
      elif(i.isnumeric()):
            count3=count3+1
      else:
          count4=count4+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
print("The number of digit characters is:")
print(count3)
print("The number of special char is:")
print(count4)


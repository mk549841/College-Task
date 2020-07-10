chars = "abcdefghijklmnopqrstuvwxyz"
check_string = input("Enter the input")

for i in chars:
  count = check_string.count(i)
  if count > 1:
    print (i, count)

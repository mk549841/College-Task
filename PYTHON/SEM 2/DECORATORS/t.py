import re
w="Welcome to python"
p="^[A-Z]\w*[a-z]$"
l=re.findall(w,p)

import re  
def removeZeros(ip): 
	new_ip = re.sub(r'\b0+(\d)', r'\1', ip)
	return new_ip 
ip =input("Enter ip")
print(removeZeros(ip)) 

import random
import string





a=""

while True:

	a += random.choice(string.ascii_letters)
	sum=0
	for b in a:
		sum+=ord(b)
			
	
	
	if sum > 916:
		a=''

	elif sum == 916:
		print("found ",a)

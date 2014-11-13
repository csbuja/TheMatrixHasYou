import random
x = 200

while (True):
	count = 0
	s = ''
	while count < x:
		r = random.randint(0, 2)
		if r == 0:
			s+=' '
		elif r == 1:
			s+='1'
		else:
			s+='0'
		count +=1
	print "\033[1;32m" + s +"\033[0m"

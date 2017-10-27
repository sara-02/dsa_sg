from math import floor, sqrt

def check_prime(p):
	if p < 2:
		return 0
	elif p < 4:
		return 1
	elif p%2 == 0:
		return 0
	elif p < 9:
		return 1
	elif p%3 == 0:
		return 0
	else:
		i = 5
		j = int(floor(sqrt(p)))
		while i<=j:
			if p%i == 0:
				return 0
			elif p%(i+2) ==0:
				return 0
			i = i + 6
		return 1

c = 0
p = 2
while c<10001:
	if check_prime(p):
		c=c+1
	if p==2:
		p=3
	else:
		p=p+2

p = p - 2
print p


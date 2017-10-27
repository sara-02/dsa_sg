def prime (a):
	if a == 0 or a == 1:
		return 0
	elif a == 2:
		return 1
	elif a%2 == 0:
		return 0
	else:
		i = 3
		while i<a:
			if a%i == 0:
				return 0
			i = i + 2



n = 600851475143
i = n - 1

while i>2:
	if n%i == 0 and prime(i):
		print i
		break
	i = i - 1



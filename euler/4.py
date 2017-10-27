def palin(s):
	while s!='':
		if s[0] != s[-1]:
			return 0
		s = s[1:-1]
	return 1

l = 10000
for i in range(100, 1000):
	for j in range(100, 1000):
		c = i * j
		if palin(str(c)) and c > l:
			l = c

print l

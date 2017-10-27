a = 1
b = 2
c = a + b
sum = 2
while c <= 4000000:
	if c%2 == 0:
		sum =sum + c
	a = b
	b = c
	c = a + b

print sum
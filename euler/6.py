def squared_sum(n):
	a = (n * (2 * n + 1) * (n + 1))/6
	return int(a)


def sum_squared(n):
	a =(n * (n + 1 ))/2
	a = pow(a, 2)
	return int(a)

n1 = squared_sum(100)
n2 = sum_squared(100)
print(n2 - n1)
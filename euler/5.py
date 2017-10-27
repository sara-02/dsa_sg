def divi(n):
    for i in range (11,21):
        if n %i !=0:
            return 0
    return 1

i = 2520 # 1to 10 divisible already given

while True:
    if divi(i):
        print i
        break
    i =i +20
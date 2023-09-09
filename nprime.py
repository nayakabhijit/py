
import math

def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

count = 0
for i in range(1,100):
    if is_prime(i):
        count += 1
        print(ordinal(count), "prime is " + str(i))
     
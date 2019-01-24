# def superPow(a, b):
# 	res = []
# 	power = int(''.join([str(el) for el in b]))
# 	for i in range(power+1):
# 		# if a ** i < 1337:
# 		res.append(a**i % 1337)
# 		# else:
# 		# 	break
# 	# power %= len(res)

# 	return res[-1]
	
	## definitely time limit
	# return (a << int(''.join([str(el) for el in b]))-1) % 1337

## AC method
def superPow(a, b):
	from functools import reduce
	## optimize
	# return pow(a, int("".join(map(str, b))), 1337)

	## for 7^435627650 mod 13 ?
	## 435627650  mod 12=2, so 7^2 mod 13=10.
	## https://math.stackexchange.com/questions/379996/computing-bmods-with-large-exponents-by-paper-and-pencil-using-fermats-littl
	# https://leetcode.com/problems/super-pow/discuss/84466/Math-solusion-based-on-Euler's-theorem-power-called-only-ONCE-C%2B%2BJava1-line-Python
	def mod(p):
		return pow(a, reduce(lambda e, d: (10*e+d)%(p-1), b, 0) ,p) if a % p else 0

	print(mod(7), mod(191))

	return (764 * mod(7) + 574 * mod(191)) % 1337

print(superPow(2, [1,0]))

## most general case

def superPow(a, b):
	b = int(''.join(map(str, b)))
	a  = a % 1337
	return helper(a, b)

def helper(a, b):
	if a == 0: return 0
	if a == 1: return 1
	if b == 1: return a % 1337
	if b % 2 == 0:
		power = helper(a, b//2)
		return (power * power) % 1337

	else:
		power = helper(a, b //2)
		return (power * power * a) % 1337

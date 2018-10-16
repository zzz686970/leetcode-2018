import collections
from functools import reduce
def hasGroupsSizeX(deck):
	# if len(deck) < 2:
	# 	return False
	# if len(deck) % len(set(deck)):
	# 	return False
	# ans = collections.Counter(deck).values()
	def gcd(a, b):
		while b: a, b = b, a % b
		return a
	count = collections.Counter(deck).values()
	print(count)
	return reduce(gcd, count) > 1

deck = [1,1,2,2,2,2, 3,3]
print(hasGroupsSizeX(deck))


	


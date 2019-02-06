import numpy as np 
def convert_base(val, base):
	res = ''
	while val >0:
		res = str(val % base) + res 
		val //= base 

	return res  if res else '0'

def poorPigs(buckets, minutesToDie, minutesToTest):
	pigs = 0
	while (minutesToTest // minutesToDie +1) ** pigs < buckets:
		pigs += 1

	return pigs

pigs = poorPigs(25, 1, 1)
a = np.arange(1, 26).reshape(pigs, -1)
print(a.shape)

for i in range(1, 26):
	print(i, "-->", convert_base(i, pigs))
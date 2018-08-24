import timeit
def fairCandySwap(A, B):
	sum_A, sum_B, set_B = sum(A), sum(B), set(B)
	target = (sum_B - sum_A) /2 
	for v in A: 
		candidate = int(target + v)

		if candidate in set_B:
			return [v, candidate]

A= [8,73,2,86,32]
B = [56,5,67,100,31]

def test():
	fairCandySwap(A, B)

print(timeit.timeit("test()", setup="from __main__ import test"))

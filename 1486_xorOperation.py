from functools import reduce 

## time O(N)
## space O(1)
def xorOperation(n, start):
	arr = [start + 2 * i for i in range(n)]
	return reduce(lambda x,y: x^y, arr)
	## return functools.reduce(operator.xor, range(start, start + 2 * n, 2)))

def xorOperation(n, start):
    xor = 0
	for i in range(0, n):
    	xor ^= start + 2 * i
	return xor

if __name__ == '__main__':
	print(xorOperation(n = 5, start = 0))
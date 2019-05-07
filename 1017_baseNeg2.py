def baseNeg2(N):
	res = []
	while N:
		res.append(N & 1)
		N = -(N >> 1)

	return ''.join(map(str, res[::-1]) or [0])

## recursive
def baseNeg2(N):
	if N == 0 or N == 1: return str(N)
	return baseNeg2(-(N>>1)) + str(N & 1)

def base2(N):
	res = []
	while N:
		res.append(N & 1)
		N = N >> 1
	return ''.join(map(str, res[::-1]) or ['0'])

print(base2(2))
print(baseNeg2(0))
def bitwiseComplement(N):
	ans = ['0' if el =='1' else '1' for el in bin(N)[2:] ]
	return int("".join(ans), 2)

print(bitwiseComplement(5))
print(bitwiseComplement(7))
print(bitwiseComplement(0))
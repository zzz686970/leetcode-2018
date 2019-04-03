def queryString(S , N) -> bool:
	return all(bin(i)[2:] in S for i in range(N, N//2, -1))

print(queryString(S = "0110", N = 3))
print(queryString(S = "0110", N = 4))
def addToArrayForm(A, K):
	ans = int("".join(str(el) for el in A)) + K 
	return list(map(int, str(ans)))

## solution 2 
def addToArrayForm(A, K):
	## starting from add with digits, left with K + A[i] // 10
	for i in range(len(A))[::-1]:
		A[i], K = (A[i]+K) % 10, (A[i]+K) // 10

	## if len(K) is larger, then concat 
	return [int(i) for i in str(K)] + A if K else A
print(addToArrayForm([1,2,0,0], 1))
def buddyStrings(A, B):
	result = set()
	for i, value in enumerate(A):
		if A[i] != B[i]:
			result.add(A[i])
			result.add(B[i])
		elif A == B and any(A.count(value) >= 2 for value in A):
			return True

	return True if len(result) == 2 else False

A = "ab"
B = "ca"
print(buddyStrings(A, B))


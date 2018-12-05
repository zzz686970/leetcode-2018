def isMonotonic(A):

	return True if A == list(sorted(A)) or A==list(sorted(A))[::-1] else False

print(isMonotonic([1,2,2,3]))
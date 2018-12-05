def rotateString(A, B):
	if A == B: return True
	for i in range(1,len(A)):
		if A[i:]+A[:i] == B:
			return True

	return False

print(rotateString('abcde','abced'))
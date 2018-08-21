def repeatedStringMatch(A, B):
	for i in range(len(B)-2):
		if B[i:i+2] not in A*2:
			return -1
	for i in range(1, 10001):
		if B in A*i:
			return i
			break
	return -1

A = "abcd" 
B = "cdabcdab"
print(repeatedStringMatch(A, B))
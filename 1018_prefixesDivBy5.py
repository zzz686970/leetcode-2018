def prefixesDivBy5(A):
	## time limit
	res = []
	for i in range(len(A)):
		res.append(True if int("".join(map(str, A[:i+1])), 2) % 5 == 0 else False)
	return res

def prefixesDivBy5(A):
	## move one step, multiply 2 with the previous element
	## for efficiency, mod 5 in each step
	# would this affect result?
	# no because the precious element will always be even
	# eg 24 % 5 + 1 would still return true
	for i in range(1, len(A)):
		A[i] += A[i-1] * 2 % 5
	return [x % 5 == 0 for x in A]

print(prefixesDivBy5([0,1,1,1,1,1]))
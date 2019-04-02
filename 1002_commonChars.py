import collections
import functools
def commonChars(A):
	A = list(sorted(A, key= lambda x: len(x)))
	res = collections.Counter(A[0])
	for a in A:
		res &= collections.Counter(a)
	return list(res.elements())

def commonChars(A):
	A = list(sorted(A, key= lambda x: len(x)))
	res = collections.Counter(A[0])
	for a in A:
		res &= collections.Counter(a)
	return list(res.elements())


print(commonChars(["bellafsfd","label","roller"]))
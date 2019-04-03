def canThreePartsEqualSum(A):
	## TLE
	# res =
	for i in range(len(A)-2):
		for j in range(i+1, len(A)-1):
			if sum(A[:i+1]) == sum(A[i+1:j+1]) == sum(A[j+1:]):
				return True

	return False

def canThreePartsEqualSum(A):
	## TLE
	# res =
	if sum(A) % 3 != 0:  return False
	s = sum(A) // 3
	target = [2*s, s]
	result = 0
	for a in A:
		result += a
		if result == target[-1]:
			target.pop()
		if not target:
			return True

	return False

assert True == canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])
assert False == canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])
assert True ==  canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])

print(canThreePartsEqualSum([18,12,-18,18,-19,-1,10,10]))
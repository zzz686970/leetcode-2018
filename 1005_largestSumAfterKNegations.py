def largestSumAfterKNegations(A, K):
	A.sort()
	## count filp time
	i = 0
	while i < len(A) and i < K and A[i] < 0:
		A[i] = -A[i]
		i += 1

	## return part, if list turns to positive and still i < K, flip the smallest
	return sum(A) - (K-i) % 2 * min(A) * 2


import collections
def largestSumAfterKNegations(A, K):
	## get freq of each element
	# c = collections.Counter(A)
	# for i in range(-100, 0):
	# 	## stop is K is used up
	# 	if K == 0:
	# 		break
	# 	## if there are more than one c[i], flip thoses
	# 	flips = min(K, c[i])
	# 	c[i] -= flips
	# 	c[-i] += flips
	# 	K -= flips

	# return sum(c.elements()) - K % 2 * min(A, key=abs) * 2

	c = collections.Counter(A)
	for i in range(-100, 0):
		if K == 0:
			break
		flips = min(K, c[i])
		c[i] -= flips
		c[-i] += flips
		K -= flips
	return sum(c.elements()) - K % 2 * abs(min(A, key=abs) * 2)



# print(largestSumAfterKNegations(A = [4,2,3], K = 1))
# print(largestSumAfterKNegations(A = [3,-1,0,2], K = 3))
print(largestSumAfterKNegations([5,6,9,-3,3], 2))
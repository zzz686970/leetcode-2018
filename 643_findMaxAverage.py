def findMaxAverage(nums, k):
	## time limit
	# result = []
	# if len(nums) - k > 0:
	# 	for i in range(len(nums)-k+1):
	# 		result.append(sum(nums[i:i+k])/k)
	# else:
	# 	result.append(sum(nums))
	# return result

	# P=[0]
	# for x in nums:
	# 	P.append(P[-1]+x)
	# ans = max(P[i+k]-P[i] for i in range(len(nums)-k+1))

	# return ans / k 	
	import itertools
	import operator
	## way2
	sums = [0] + list(itertools.accumulate(nums))
	return max(map(operator.sub, sums[k:], sums)) / k

print(findMaxAverage([0,1,1,3,3], k = 4))
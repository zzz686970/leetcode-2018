def findDuplicates(nums):
	## 1...n, for elements appearing twice, the first time would change its index to negative,
	## we can fetch this value in second time
	## also notice other value may change x
	res = []
	for x in nums:
		if nums[abs(x)-1] < 0:
			res.append(abs(x))
		else:
			nums[abs(x)-1] *= -1

	return res 

print(findDuplicates([4,3,2,7,8,2,3,1]))
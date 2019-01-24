def productExceptSelf(nums):
	## time out
	# from functools import reduce
	# def product(nums):
	# 	return reduce(lambda x,y: x*y, nums)

	# return [product(nums[:el]+nums[el+1:]) for el in range(len(nums))]
	ans, p,  n = [], 1,  len(nums)

	for i in range(n):
		ans.append(p)
		p *= nums[i]

	p = 1
	for j in range(n-1, -1,-1):
		ans[j] *= p 
		p *= nums[j]

	return ans

	## combine into one
	if not nums: return [] 
	arr = [1] * len(nums)
	pi = pj = 1
	for i in range(len(nums)):
		j = -1-i 
		arr[i] *= pi
		arr[j] *= pj 
		pi *= nums[i]
		pj *= nums[j]

	return arr


print(productExceptSelf([1,2,3,4]))
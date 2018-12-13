def rob(nums):
	## too naive
	# return max(sum(nums[0::2]), sum(nums[1::2]), sum(nums[0::3], sum(nums[1::3])))
	l =r=0
	for n in nums:
		l, r = r, max(n+l, r)
	return r

assert 4 == rob([2,1,1,2])
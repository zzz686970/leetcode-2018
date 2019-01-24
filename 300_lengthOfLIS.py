def lengthOfLIS(nums):
	if not nums: return 0
	l = len(nums)
	dp = [1 for _ in range(l)]
	
	for i in range(1, l):
		for j in range(i):
			if nums[i] > nums[j]:
				dp[i] = max(dp[i], dp[j]+1)

	return max(dp)

## binary search
def lengthOfLIS(nums):
	## the logic behind:
	## if there is a number which is smaller than the previous one,
	## res[pos] would get replaced!!! 
	## Any number behind larger than the previous one must be larger than this one!
	def binary_search(items, l, r, target):
		if l == r: return l 
		mid = (l+r) // 2
		if items[mid] < target:
			return binary_search(items, mid+1, r, target)
		else:
			return binary_search(items, l, mid, target) 

	l = len(nums)
	res = []
	for num in nums:
		pos = binary_search(res, 0, len(res), num)
		if pos >= len(res):
			res.append(num)
		else:
			res[pos] = num 
		print(res)

	return len(res)


print(lengthOfLIS([10,9,2,5,3,7,101,18]))
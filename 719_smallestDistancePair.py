# def smallestDistancePair(nums, k):
# 	"""
# 	:type nums: List[int]
# 	:type k: int
# 	:rtype: int
# 	""" 
# 	from collections import defaultdict

# 	if not nums:
# 		return 0
# 	if len(nums) == 1:
# 		return nums[0]
	
# 	res = defaultdict(int)
# 	for i in range(len(nums)-1):
# 		for j in range(i+1, len(nums)):
# 			res[abs(nums[i]-nums[j])] += 1
	
# 	ans = sorted(res.items(), key=lambda x: x[0])
# 	while k:
# 		for (key, val) in ans:
# 			k -= res[key]
# 			if k <=0:
# 				return key 

# print(smallestDistancePair([1,3,1], 1))

def smallestDistancePair(nums, val):
	
def topKFrequent(nums, k):
	result = {}
	for el in nums:
		result[el] = nums.count(el)

	nums_2 = set(nums.sort(key=lambda x: nums.count(x)))

	return nums_2

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))

def majorityElement(nums):
	import collections
	counter = collections.Counter(nums)
	return counter.most_common(1)[0][0]

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
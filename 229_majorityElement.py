def majorityElement(nums):
	import collections
	# res = collections.Counter(nums)
	# return [el for el, freq in res.items() if freq > len(nums)//3]

	## O(1) space and O(n) time
	## remove the fewer ones, only those having the most freq remains in dict
	res = collections.Counter()
	for n in nums:
		res[n] += 1
		if len(res) == 3:
			res -= collections.Counter(set(res))

	return [n for n in  res if nums.count(n) > len(nums)//3]


print(majorityElement([3,2,3]))
print(majorityElement([1,1,1,3,3,2,2,2]))
def findLHS(nums):
	import collections
	d = collections.Counter(nums)
	return max([d[i] + d[i+1] for i in d if i+1 in d] or [0])

assert 5 == findLHS([1,3,2,2,5,2,3,7])
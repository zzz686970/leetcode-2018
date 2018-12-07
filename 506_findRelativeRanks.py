def findRelativeRanks(nums):
	s = len(nums)
	pair = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + [str(i) for i in range(4, s+1) if s>3]
	
	return list(map(dict(zip(sorted(nums)[::-1], pair)).get, nums))

nums = [100,111,111111]
print(findRelativeRanks(nums))
def dominantIndex(nums):
	# if not nums: return -1
	# if len(nums) == 1: return 0
	# result = list(sorted(nums))

	# return nums.index(result[-1]) if result[-2]==0 result[-1] // result[-2] >= 2 else -1
	if not nums: return -1
	idx, first, second = 0,-1, -1
	for i, num in enumerate(nums):
		if num >= first:
			second = first 
			first = num
			idx = i 

		elif num > second:
			second = num
	if first < second * 2:
		idx = -1

	return idx

assert 1 == dominantIndex(nums = [3, 6, 1, 0])
assert -1 ==  dominantIndex(nums = [1, 2, 3, 4])
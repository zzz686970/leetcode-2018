def permute(nums):
	# import itertools 

	# return [list(el) for el in itertools.permutations(nums)]

	## no python way
	return [[n]+p for i, n in enumerate(nums) for p in permute(nums[:i]+nums[i+1:])] or [[]]


print(permute([1,2,3]))
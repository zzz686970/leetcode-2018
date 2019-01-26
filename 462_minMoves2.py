def minMoves2(nums):
	## way 1
	# median = sum(nums) // len(nums)
	media = list(sorted(nums))[len(nums)//2]
	return sum(abs(num-median) for num in nums)

	## way 2
	## ~i reverse from backwards
	nums.sort()
	return sum(nums[~i]-nums[i] for i in range(len(nums)//2))


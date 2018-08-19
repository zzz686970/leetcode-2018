def threeSum(nums):
	nums.sort()
	n = len(nums)
	result = []

	for i in range(n):
		if i > 0 and nums[i] == nums[i-1]:
			continue
		left, right = i+1, n-1
		while left < right:
			temp = nums[i] + nums[left] + nums[right]

		if temp == 0:
			result.append([nums[i], nums[left], nums[right]])
			left += 1
			right -= 1
			while left < right and nums[left] == nums[left-1]:
				left += 1
			while right > left and nums[right] == nums[right+1]:
				right -= 1

		elif temp > 0:
			right -= 1
		else:
			left += 1
	return result
	# solutions = set()
	# i = 0
	# while i < n -2:
	# 	num = nums[i]
	# 	left = i+1
	# 	right = n -1
	# 	while left < right:
	# 		left_num = nums[left]
	# 		right_num = nums[right]
	# 		s = num + left_num + right_num
	# 		if s == 0:
	# 			solutions.add(tuple([right_num, num, left_num]))
	# 		elif s > 0:
	# 			right -= 1
	# 		else:
	# 			left += 1

	# 	i += 1

	# return list(solutions)

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
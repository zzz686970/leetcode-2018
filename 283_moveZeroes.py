def moveZeroes(nums):
	# index = []
	# for i, value in enumerate(nums):
	# 	if nums[i] == 0:
	# 		index.append(i)

	# for i in index:
	# 	del nums[i]

	# 	nums.append(0)
	i = 0
	for num in nums:
		if num != 0:
			nums[i] = num
			i += 1
	for j in range(i, len(nums)):
		nums[j] = 0


	# slow = fast = 0
	# while fast < len(nums):
	# 	if nums[fast] !=0:
	# 		if slow != fast:
	# 			nums[slow] = nums[fast]
	# 			nums[fast] = 0
	# 		slow += 1

	# 	fast += 1

	## nums.sort(key = lambda x: 1 if x == 0 else 0)




nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
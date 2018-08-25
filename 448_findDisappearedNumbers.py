def findDisappearedNumbers(nums):
	## can't ac
	# if nums == []:
	# 	return []
	# n = len(nums)
	# # max_number = max(nums)
	# # min_number = min(nums)
	# ans = []
	# for i in range(1, n+1):
	# 	if i not in nums:
	# 		ans.append(i)

	# return ans

	n = len(nums)
	if n == 0: return []
	for i in range(n):
		num = nums[i]
		while num != -1:
			nums[num-1], num = -1, nums[num-1]
	return [i+1 for i in range(n) if nums[i] !=-1]

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))
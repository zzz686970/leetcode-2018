def removeDuplicates(nums):
	cnt = 0
	for num in nums:
		if cnt < 2 or nums[cnt-1] != num or nums[cnt-2] != num:
			nums[cnt] = num 
			cnt += 1

	return cnt 
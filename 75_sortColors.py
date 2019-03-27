def sortColors(nums):
	i = j = 0
	for k in range(len(nums)):
		tmp = nums[k]
		nums[k] = 2
		if tmp < 2:
			nums[i] = 1
			i += 1
		if tmp == 0:
			nums[j] = 0
			j += 1

	return nums 

def sortColors2(nums):
	i, j, k =0,  0, len(nums)-1
	while i <= k:
		if nums[i] == 0:
			nums[i], nums[j] = nums[j], nums[i]
			j += 1
		elif nums[i] == 2:
			## move one step back since nums[i] has been replaced by nums[k]
			## need to double check
			nums[i], nums[k] = nums[k], nums[i]
			i -= 1
			k -= 1
		i += 1
	return nums

print(sortColors([2,0,2,1,1,0]))
print(sortColors2([2,0,2,1,1,0]))
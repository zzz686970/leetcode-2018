def checkPossibility(nums):
	if len(nums) < 2:
		return True
	
	cur = 0

	for i in range(1, len(nums)):
		if nums[i-1] > nums[i]:
			cur += 1
			if i == 1 or nums[i-2] <= nums[i]:
				nums[i-1] = nums[i]
			else:
				nums[i] = nums[i-1]
			if cur > 1:
				return False
	print(nums)
	return True


	## 108ms
	# if len(nums)<2:
	# return True
	# a1=nums[:]
	# a2=nums[:]
	# for i in range(len(nums)-1):
	# 	if nums[i]>nums[i+1]:
	# 		a1[i]=nums[i+1]
	# 		a2[i+1]=nums[i]
	# 		break
	# return a1==sorted(a1) or a2==sorted(a2)



nums = [-1,4,2,3]
print(checkPossibility(nums))


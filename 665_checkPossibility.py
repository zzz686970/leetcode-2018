def checkPossibility(nums):
	cur = 0

	for i in range(len(nums)-1):
		if nums[i] > nums[i+1]:
			cur = i+1
			break
	newlist = nums[:cur] + nums[cur+1:]
	print(newlist)
	for i in range(len(newlist) -1):
		if newlist[i] > newlist[i+1]:
			return False

	return True


nums = [2,3,3,2,4]
print(checkPossibility(nums))


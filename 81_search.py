def search(nums, target):
	l, h = 0, len(nums)-1
	while l <= h:
		mid = (l+h)//2
		if nums[mid] == target:
			return True 
		if nums[mid] == nums[l]:
			l += 1
		elif nums[mid] > nums[l]:
			if nums[l] <= target < nums[mid]:
				h = mid - 1
			else:
				l = mid + 1
		elif nums[mid] <= nums[h]:
			if nums[mid] < target <= nums[h]:
				l = mid + 1
			else:
				h = mid - 1

	return False 

print(search(nums=[1,3,1,1], target=3))


def search(nums, target):
	if not nums: return False 
	l, r = 0, len(nums) - 1
	while l < r:
		mid = (l + r) // 2
		if nums[mid] == target:
			return True 

		if nums[mid] < nums[r]:
			if nums[mid] < target <= nums[r]:
				l = mid + 1
			else:
				r = mid

		elif nums[mid] > nums[r]:
			if nums[l] <= target < nums[mid]:
				r = mid
			else:
				l = mid + 1
		## can't decide target is in the left or right
		else:
			r -= 1
	return nums[l] == target 

print(search(nums=[1], target=1))
def missingNumber(nums):
	n = len(nums)
	return n * (n+1) // 2 - sum(nums)
	## time exceed
	# missing = 0
	# for i in range(len(nums)+1):
	# 	if i in nums:
	# 		continue
	# 	missing = i 

	# return missing

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))
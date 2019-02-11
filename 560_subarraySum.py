# def subarraySum(nums, k):
# 	## way 1, brute force
# 	cnt = 0
# 	for i in range(len(nums)):
# 		for j in range(i, len(nums)):
# 			if sum(nums[i:j+1]) == k:
# 				cnt += 1

# 	return cnt 

## way 2
# def subarraySum(nums, k):
# 	cnt = 0
# 	for i in range(len(nums)):
# 		prev = 0
# 		for j in range(i, len(nums)):
# 			prev += nums[j]
# 			if prev == k:
# 				cnt += 1

# 	return cnt 


## way 3 AC version
def subarraySum(nums, k):
	total_sum = {0:1}
		cnt = prev_sum = 0
		for num in nums:
			prev_sum += num
			cnt += total_sum.get(prev_sum-k, 0)
			total_sum[prev_sum] = total_sum.get(prev_sum, 0) + 1

		return cnt


print(subarraySum([1,1,1], 2))
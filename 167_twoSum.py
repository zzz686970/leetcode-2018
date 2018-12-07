def twoSum(numbers, target):
	## time limit
	# idx1, idx2 = 0, 0
	# result = []
	# while idx1 < len(numbers):
	# 	idx2 = idx1 + 1
	# 	while idx2 < len(numbers):
	# 		if numbers[idx1] + numbers[idx2] == target:
	# 			result.append(idx1+1)
	# 			result.append(idx2+1)
	# 			break
	# 		else:
	# 			idx2 += 1

	# 	idx1 += 1

	# return result

	# result = {}
	# for i, num in enumerate(numbers):
	# 	if target-num in result:
	# 		return [result[target-num]+1, i+1]
	# 	result[num] = i

	## efficient
	l, r = 0, len(numbers) -1
	while l < r:
		s = numbers[l] + numbers[r]
		if s==target:
			return [l+1, r+1]
		elif s< target:
			l += 1
		else:
			r -= 1

	## way 3
	# for i in range(len(numbers)):
	# 	l , r = i+1, len(numbers) -1
	# 	tmp = target - numbers[i]
	# 	while l <= r:
	# 		mid = l + (r-1) // 2
	# 		if numbers[mid] == tmp:
	# 			return [i+1, mid+1]
	# 		elif numbers[mid] < tmp:
	# 			l = mid + 1
	# 		else:
	# 			r = mid - 1

print(twoSum(numbers = [5, 25, 75], target = 100))

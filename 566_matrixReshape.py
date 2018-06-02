def matrixReshape(nums, r, c):
	result = [x for sub in nums for x in sub]
	rows = [len(sub) for sub in nums]
	reshaped = []
	if len(result) == r * c and len(set(rows)) == 1:
		for i in range(1, len(result)+1):
			if i % c == 0:
				reshaped.append(result[i-c:i])
		return reshaped
	else:
		return nums

nums = [[1,2],[3,4]]
print(matrixReshape(nums, 1, 4))
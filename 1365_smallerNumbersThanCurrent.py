def smallerNumbersThanCurrent(nums):
	dic = {}
	for i, num in enumerate(sorted(nums)):
		if num not in dic:
			dic[num] = i 

	return [dic[num] for num in nums]

if __name__ == '__main__':
	print(smallerNumbersThanCurrent([8,1,2,2,3]))
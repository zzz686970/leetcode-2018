def decompressRLElist(nums):
	## return [x for a, b in zip(A[0::2], A[1::2]) for x in [b] * a]

	ans = []
	for i in range(0, len(nums), 2):
		ans.extend([nums[i+1]] * nums[i])

	return ans 

if __name__ == '__main__':
	print(decompressRLElist(nums = [1,2,3,4]))
	print(decompressRLElist(nums = [1,1,2,3]))
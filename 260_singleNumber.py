def singleNumber(nums):
	## first, the same number for ^ would counteract each other
	## the first step is to get the xor value of two distinct number 
	xor = 0
	a, b = 0, 0
	for num in nums:
		xor ^= num 

	## mask is used here to differentiate the two numbers
	## make sure there is only 1 digit that is different from xor
	## so that mask & num is either 0 or 1
	mask = 1
	while (xor & mask) == 0:
		mask = mask << 1

	## use mask xor again, this time we use mask to differentiate the two numbers
	for num in nums:
		if num& mask:
			a ^= num 
		else:
			b ^= num 

	return [a, b]

print(singleNumber([3, 5]))
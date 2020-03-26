def findNumbers(nums):
	func = lambda t: sum(1 for el in map(len, t) if el % 2==0)

	return func(map(str, nums))

	## len of each el
	# return len([x for x in nums if len(str(x)) % 2 == 0])

if __name__ == '__main__':
	print(findNumbers([12,345,2,6,7896]))
	print(findNumbers([555,901,482,1771]))
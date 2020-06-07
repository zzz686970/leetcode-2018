def kidsWithCandies(candies, extraCandies):
	max_num = max(candies)
	# return [candy + extraCandies > max_num for candy in candies]
	ans = []
	for el in candies:
		if el + extraCandies >= max_num:
			ans.append(True)
		else:
			ans.append(False)

	return ans 

if __name__ == '__main__':
	print(kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
	print(kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
	print(kidsWithCandies(candies = [12,1,12], extraCandies = 10))
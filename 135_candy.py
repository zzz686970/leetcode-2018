def candy(ratings):
	res = [1 for _ in range(len(ratings))]
	n = len(ratings)
	## forward 1,3,4 -> 1, 2, 3
	for i in range(1,n):
			if ratings[i] > ratings[i-1]:
				res[i] = res[i-1] + 1
	print(res)
	## backward update 1,0,1 -> 2,1,1
	for j in range(n-1, 0, -1):
		if ratings[j-1] > ratings[j]:
			res[j-1] = max(res[j-1], res[j]+1)

	print(res)
	return sum(res )


# print(candy([1,0,2 ]))
# print(candy([1,2,87,87,87,2,1]))
print(candy([1,3,4,5,2]))

# For instance, `[1,2,87,87,87,2,1]`
# After the first scan from left to right, value which is larger than its left side will be updated accordingly;
# the result would become `[1, 2, 3, 1, 1, 1, 1]`
# In the second scan from right to left, we check it backwards since some of the values are not updates, meaning subset which is in descending order.
# `[1, 2, 3, 1, 3, 2, 1]`
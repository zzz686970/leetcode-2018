def distributeCandies(candies):
	return int(min(len(candies)/2, len(set(candies))))

candies = [1,1,2,2,3,3]
print(distributeCandies(candies))

	# half_cnt = len(candies) / 2
	# total_group = dict((a, candies.count(a)) for a in candies)
	# sister_set = []
	# current = 0
	# for key, value in group.items():
	# 	if current < half_cnt:
	# 		total_group.append(key)
	# 		current += 1




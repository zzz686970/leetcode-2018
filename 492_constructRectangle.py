def constructRectangle(area):
	## time limit

	# mid = int(area ** 0.5)
	# for i in range(mid, area + 1):
	# 	if not area % i and i >= area / i:
	# 		return [i, area//i]
	factor = int(area**.5)
	while(area % factor):
		factor -= 1
	return [area//factor, factor]

print(constructRectangle(9999991))
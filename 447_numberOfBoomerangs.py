def numberOfBoomerangs(points):
	ans = {}
	for i in points:
		d = {}
		for j in points:
			distance = (i[0]-j[0]) ** 2 + (i[1]-j[1]) ** 2
			if distance in d:
				ans += d[distance]
				d[distance] += 2
			else:
				d[distance] = 2

	return ans


def findRadius(houses, heaters):
	heaters = list(sorted(heaters)) + [float('inf')]
	i = r = 0
	for x in sorted(houses):
		## multiple heaters under the same location
		while x >= sum(heaters[i:i+2]) / 2.:
			i += 1

		r = max(r, abs(heaters[i]-x))

	return r 

print(findRadius([1,2,3,4],[1,4]))
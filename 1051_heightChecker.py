def heightChecker(heights):
	if not heights: return 0
	return sum(a != b for a, b in zip(heights, sorted(heights)))

print(heightChecker([2,1,2,1,1,2,2,1]))
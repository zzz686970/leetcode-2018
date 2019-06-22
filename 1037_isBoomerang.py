def isBoomerang(points):
	a, b, c = points
	if (a[0] - b[0]) *  (a[1]-c[1]) ==  (a[1]-b[1]) * (a[0] - c[0]) :
		return False 

	return True

print(isBoomerang([[1,1],[2,3],[3,2]]))
print(isBoomerang([[1,1],[2,2],[3,3]]))
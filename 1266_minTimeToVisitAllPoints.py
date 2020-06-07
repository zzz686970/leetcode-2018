def minTimeToVisitAllPoints(points):
	## return sum(max(abs(p[i][0] - p[i - 1][0]), abs(p[i][1] - p[i - 1][1])) for i in range(1, len(p)))

	ans = 0
	for i in range(1, len(points)):
		pre, cur = points[i-1:i+1]
		ans += max(map(abs, (pre[0] - cur[0], pre[1] - cur[1])))

	return ans 

if __name__ == '__main__':
	print(minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]))
	print(minTimeToVisitAllPoints(points = [[3,2],[-2,2]]))
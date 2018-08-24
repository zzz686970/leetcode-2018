class Solution():
	def largestTriangleArea(self, points):
		result = 0
		l = len(points)
		for i in range(l):
			for j in range(i+1, l):
				for k in range(j+1, l):
					temp = self.tri_area(points[i], points[j], points[k])
					if temp > result:
						result = temp
		return result

	def tri_area(self, a, b, c):
		# return (0.5*abs((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])))
		return (abs(a[0]*b[1] + b[0]*c[1]+ c[0]*a[1] - a[0]*c[1]-b[0]*a[1]-c[0]*b[1])) / 2

a = Solution()
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print(a.largestTriangleArea(points))


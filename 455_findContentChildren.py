def findContentChildren(self, g, s):
	"""
	:type g: List[int]
	:type s: List[int]
	:rtype: int
	"""
	Children = list(sorted(g))
	Cookie = list(sorted(s))
	child, cookie = 0, 0
	while child < len(g) and cookie < len(s):
		if Children[child] <= Cookie[cookie]:
			child += 1
		cookie += 1
	
	return child

print(findContentChildren(g=[10,9,8,7],s=[5,6,7,8]))
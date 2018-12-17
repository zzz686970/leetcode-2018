def isSubtree(s, t):
	# def convert(p):
	# 		return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"		
	# 	return convert(t) in convert(s)

	## way 2
	if not t: return True 

	def check(r1, r2):
		if not r1 and not r2:
			return True 
		elif r1 and not r2 or r2 and not r1:
			return False

		if r1.val != r2.val:
			return False 

		return check(r1.left, r2.left)

	def dfs(s,t):
		if not s: return False 
		if s.val == t.val and check(s, t):
			return True
		return dfs(s.left, t.left) or dfs(s.right, t.right)

	return dfs(s, t)

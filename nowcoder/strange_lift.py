def strange_lift(n, a, b ,k):
	"""[summary]
	
	
	Arguments:
		n {[type]} -- [total floors]
		a {[type]} -- [floor a]
		b {[type]} -- [floor b]
		k {[type]} -- [k_i in each floor]
	"""
	if not (1<=a<=n) or not(1<=b<=n):
		return False

	max_cnt = 200
	def dfs(from_floor, to_floor, cnt):
		if cnt > max_cnt:
			return -1
		elif from_floor == to_floor:
			return 0
		elif from_floor + k[from_floor] == to_floor or from_floor-k[from_floor]==to_floor:
			return cnt + 1
		else:
			if from_floor + k[from_floor] < to_floor:
				from_floor += k[from_floor]
			elif from_floor + k[from_floor] > to_floor:
				from_floor -= k[from_floor]

			dfs(from_floor, to_floor, cnt+1)
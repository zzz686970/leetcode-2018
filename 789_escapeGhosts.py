def escapeGhosts(ghosts, target):
	# from operator import sub 
	target_dist = sum(list(map(lambda x: abs(x), target)))

	for ghost in ghosts:
		# ghost = list(map(sub, ghost, target))
		ghost = [a-b for a, b in zip(ghost, target)]
		ghost_dist = sum(list(map(lambda x: abs(x), ghost)))
		if ghost_dist <= target_dist:
			return False 

	return True


print(escapeGhosts(ghosts = [[1,8],[-9,0],[-7,-6],[4,3],[1,3]], target = [6,-9]))
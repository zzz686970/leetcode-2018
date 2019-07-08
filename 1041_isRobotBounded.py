def isRobotBounded(instructions):
	## initial point
	x, y = 0, 0
	## step each time
	dx, dy = 0, 1
	for i in instructions:
		## original point with step to move
		if i == 'G':
			x, y = x+dx, y + dy
		## facing left, direction change
		## dx = -dy, dy = dx (0, 1) --> (-1, 0)
		elif i == 'L':
			dx, dy = -dy, dx
		elif i == 'R':
			dx, dy =  dy, -dx

	return (x, y) == (0, 0) or (dx, dy) != (0, 1)




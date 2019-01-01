def robotSim(commands, obstacles):
	# -2: turn left 90 degrees
	# -1: turn right 90 degrees
	# 1 <= x <= 9: move forward x units
	# [4,-1,3] --> 25

	i = j = mx = d = 0
	move, obstacles = [(0,1),(-1,0),(0,-1),(1,0)], set(map(tuple, obstacles))

	for command in commands:
		if command == -2: d = (d+1) % 4
		elif command == -1: d = (d-1) % 4
		else:
			x, y = move[d]
			while command and (i+x, j+y) not in obstacles:
				i += x
				j += y 
				command -= 1
			mx = max(mx, i**2 + j**2)
	return mx

	## way2
	# x,y = 0, 0
	# dx, dy = 0, 1
	# best = 0
	# for command in commands:
	# 	if command == -2:
	# 		dx, dy = -dy, dx
	# 	elif command == -1:
	# 		dx, dy = dy, -dx
	# 	else:
	# 		for i in range(command):
	# 			if (x+dx, y+dy) in obstacles:
	# 				break
	# 			else:
	# 				x += dx 
	# 				y += dy 

	# 		best = max(best, x*x + y*y)

	# return best

print(robotSim(commands = [4,-1,3], obstacles = []))

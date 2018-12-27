def robotSim(commands, obstacles):
	# direction = 'n'
	# next_point = [0, 0]
	# for i in range(len(commands)):
	# 	if commands[i] == -2:
	# 		next_point = [commands[i+1], 0]
	# 	elif commands[i] = -1:
	# 		next_point = 
	x,y = 0, 0
	dx, dy = 0, 1
	best = 0
	for command in commands:
		if command == -2:
			dx, dy = -dy, dx
		elif command == -1:
			dx, dy = dy, -dx
		else:
			for i in range(command):
				if (x+dx, y+dy) in obstacles:
					break
				else:
					x += dx 
					y += dy 

			best = max(best, x*x + y*y)

	return best

print(robotSim(commands = [4,-1,3], obstacles = []))

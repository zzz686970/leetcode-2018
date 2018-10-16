def robotSim(commands, obstacles):
	direction = 'n'
	next_point = [0, 0]
	for i in range(len(commands)):
		if commands[i] == -2:
			next_point = [commands[i+1], 0]
		elif commands[i] = 1


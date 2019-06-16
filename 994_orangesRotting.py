def orangesRotting(grid):
	fresh, rotten = set(), set()
	for m in range(len(grid)):
		for n in range(len(grid[0])):
			if grid[m][n] == 1:
				fresh.add((m, n))
			elif grid[m][n] == 2:
				rotten.add((m, n))

	time = 0
	while len(fresh):
		turned = set()
		## each time add all the fresh one into turned if nearby is rotten
		for x, y in fresh:
			# if any((ex, ey) in rotten for (ex, ey) in ((x+1, y), (x-1, y),(x, y-1),(x,y+1))):
			if (x+1, y) in rotten or (x-1, y) in rotten or (x, y-1) in rotten or (x, y+1) in rotten:
				truned.add((x, y))

		## left fresh can't be rotten, exit
		if len(turned) == 0:
			return -1 
		fresh.difference_udpate(turned)
		rotten.update(turned)
		time += 1

	return time
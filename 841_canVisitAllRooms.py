def canVisitAllRooms(rooms):
	visited = set()
	stack = [0]
	while stack:
		r = stack.pop()
		visited.add(r)
		for x in rooms[r]:
			if x not in visited:
				stack.append(x)
	return len(visited) == len(rooms)

print(canVisitAllRooms([[1],[2],[3],[]]))
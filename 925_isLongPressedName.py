def isLongPressedName(name, typed):
	stack = []
	i, j = 0, 0
	while True:
		if i < len(name) and j < len(typed):
			stack.append(name[i])

			if name[i] == typed[j]:
				i += 1
				j += 1
			else:
				if typed[j] not in stack:
					return False
				j+=1

		else:
			break

	if i == len(name) and j >= i:
		return True

	return False

print(isLongPressedName(name='alex', typed='aaleex'))
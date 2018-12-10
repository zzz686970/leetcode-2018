def isOneBitCharacter(bits):
	l = len(bits)
	index = 0
	while index < l:
		if index == l-1: return True

		if bits[index] == 1:
			index += 2
		else:
			index += 1

	return False

print(isOneBitCharacter([1,0,0]))
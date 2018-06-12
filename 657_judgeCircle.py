def judgeCircle(moves):
	left = moves.count('L')
	right = moves.count('R')
	up = moves.count('U')
	down = moves.count('D')
	if left == right and up == down:
		return True

	return False

print(judgeCircle('LL'))
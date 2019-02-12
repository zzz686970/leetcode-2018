def solution(N):
	if N == 0 or N == 1: return 0
	number = N 
	moves = []
	l, r = 0, 1
	if number <= 0:
		number = -number 
	else:
		number -= 1

	if N <=0:
		while number != 0:
			if number & 1:
				l = 2 * l - r
				moves.append('L')
			else:
				r = 2 * r - l
				moves.append('R')

			number //= 2
	else:
		while number !=0:
			if number & 1:
				r = 2 * r - l
				moves.append('R')
			else:
				l = 2 * l - r
				moves.append('L')

			number //= 2

	return len(moves) if moves else -1

print(solution(2))

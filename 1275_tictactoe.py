def tictactoe(moves):
	"""check whether moves in win list
	
	switch player for each move
	
	Arguments:
		moves {[type]} -- [description]
	
	Returns:
		[type] -- [description]
	"""
	win_list = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
	player = 'A'
	matrix = [0] * 9
	for x,y in moves:

		matrix[x + y * 3] = player 
		for a, b, c in win_list:
			if matrix[a] == matrix[b] == matrix[c] and matrix[a] != 0:
				return player

		player = 'B' if player == 'A' else 'A'

	if len(moves) == 9:
		return 'Draw'

	return 'Pending'

if __name__ == '__main__':
	main()


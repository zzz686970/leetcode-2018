def numRookCaptures(board):
	res = 0
	x, y = 0, 0
	for i in range(8):
		for j in range(8):
			if board[i][j] == 'R':
				x, y = i, j

	for m, n in [(-1,0),(0,1),(1,0), (0,-1)]:
		cur_x, cur_y = x+m, y + n 
		while 0<=cur_x< 8 and 0<= cur_y < 8:
			if board[cur_x][cur_y] == 'p': res += 1
			if board[cur_x][cur_y] != '.': break 

			cur_x, cur_y = cur_x + m, cur_y + n

	return res 

print(numRookCaptures([[".",".",".",".",".",".",".","."],
	[".",".",".","p",".",".",".","."],
	[".",".",".","p",".",".",".","."],
	["p","p",".","R",".","p","B","."],
	[".",".",".",".",".",".",".","."],
	[".",".",".","B",".",".",".","."],
	[".",".",".","p",".",".",".","."],
	[".",".",".",".",".",".",".","."]]))
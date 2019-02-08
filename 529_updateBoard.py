def updateBoard(board, click):
	m, n =  len(board), len(board[0])
	(row, col), directions = click, ((-1,-1), (-1, 0), (-1,1), (0, -1), (0, 1), (1, -1),(1, 0), (1, 1))

	if 0 <= row < m and 0 <= col < n:
		if board[row][col] == 'M':
			## not ==
			board[row][col] = 'X'
		elif board[row][col] == 'E':
			n = sum([board[row + r][col + c] == 'M' for r, c in directions if 0 <= row + r < m and 0 <= col + c < n])
			board[row][col] = str(n or 'B')
			for r, c in directions * (not n): updateBoard(board, [row + r, col + c])
	return board


# print(updateBoard([['E', 'E', 'E', 'E', 'E'],['E', 'E', 'M', 'E', 'E'],['E', 'E', 'E', 'E', 'E'],['E', 'E', 'E', 'E', 'E']], 
# 	click= [3, 0]))

print(updateBoard([["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]],click = [1,2]))


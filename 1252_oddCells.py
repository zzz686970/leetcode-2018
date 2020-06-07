def oddCells(n, m, indices):
	## Time: O(L), space: O(m + n), where L = indices.length.

	row, col, cntRow, cntCol = [False] * n, [False] * m , 0, 0
	for ri, ci in indices:
		row[ri] ^= True 
		col[ci] ^= True 
		cntRow += 1 if row[ri] else -1
		cntCol += 1 if col[ci] else -1 

	return (m-cntCol) * cntRow + (n-cntRow) * cntCol 

if __name__ == '__main__':
	print(oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))
	print(oddCells(n = 2, m = 2, indices = [[1,1],[0,0]]))
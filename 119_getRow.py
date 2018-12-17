def getRow(rowIndex):
	row = [1]
	for _ in range(rowIndex):
		row = [x+y for x,y in zip([0]+row, row+[0])]

	return row

	## way 2
	# for _ in range(rowIndex):
	# 	row = [1] + [row[j] + row[j+1] for j in range(len(rowIndex))] + [1]
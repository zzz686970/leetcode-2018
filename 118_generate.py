def generate(numRows):
	if not numRows: return []
	result = [[1]]
	row = [1]
	for _ in range(numRows-1):
		row = [x+y for x,y in zip([0]+row, row+[0])] 
		result.append(row)
	return result

print(generate(10))
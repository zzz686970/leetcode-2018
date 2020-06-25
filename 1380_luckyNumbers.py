def luckyNumbers(matrix):
	ans = []
	for i in range(len(matrix)):
		## look for minimum number in this row
		min_j, min_val = matrix[i].index(min(matrix[i])), min(matrix[i])
		## verify whether it's the max number in this column
		if all(min_val >= matrix[j][min_j] for j in range(len(matrix))):
			ans.append(min_val)

	return ans

def luckyNumbers(matrix):
	"""[summary]
	Time complexity: O(m * n)
	Space complexity: O(m + n)
	"""
	# return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})

	## here the first * is used to extract elements from the set
	## after intersection, the result can be wrapped in a list
	return [*{*map(min, matrix)} & {*map(max, zip(*matrix))}]
	# return {*map(min, matrix)} & {*map(max, zip(*matrix))}
			

if __name__ == '__main__':
	print(luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))
	print(luckyNumbers(matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
	print(luckyNumbers(matrix = [[7,8],[1,2]]))
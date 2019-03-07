def searchMatrix(matrix, target):
	## O(m + n)
	## search from last element of each row
	j = -1
	for row in matrix:
		while j + len(row) >=0 and row[j] > target:
			j -= 1

		if j + len(row) >=0 and  row[j] == target:
			return True 

	return False 

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        for row in matrix:
            if self.search(row, target):
                return True
        
        return False
    
    def search(self, row, target):
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l+r) // 2
            if row[mid] == target:
                return True 
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
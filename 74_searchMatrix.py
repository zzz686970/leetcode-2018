# def searchMatrix(matrix, target) -> bool:
#   m, n = len(arr), len(arr[0])
#   if matrix[0][0] > target or matrix[-1][-1] < target:
#       return False 
#   binary_search_2d(arr, target, 0, m, 0, n)


# def binary_search_2d(arr, target, start_x, end_x, start_y, end_y):
#   if start_x > end_x or start_y > end_y:
#       return False

#   x = (start_x + end_x) // 2
#   result = binary_search(arr[x], target, start_y, end_y)
#   if arr[x][result] == target:
#       return True 

#   return binary_search_2d(arr, target, start_x, x -1, result +1, end_y) or binary_search_2d(arr, target, x+1, end_x, end_y, result)


# def binary_search(arr, target, start, end):
#   mid = (start + end) // 2
#   if arr[mid] == target:
#       return mid 
#   elif arr[mid] < target:
#       # start = mid +1
#       return binary_search(arr, target, mid+1, end)
#   else:
#       # end = mid 
#       return binary_search(arr, target, start, mid-1)

def searchMatrix(matrix, target) -> bool:
        if not matrix: return False
        
        m, n = len(matrix), len(matrix[0])
        if m ==0 or n == 0: return False
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False         
        l, r = 0, m *n -1
        while l <= r:
            mid = l + (r-l)//2
            num = matrix[mid//n][mid%n]
            if num < target:
                l = mid+1
            elif num > target:
                r = mid-1
            else:
                return True
        return False

print(searchMatrix([[1,3]],2))
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]: return False 
    row, col = len(matrix), len(matrix[0])
    l, r = 0, len(matrix) * len(matrix[0]) - 1
    while l < r:
        mid = (l + r) // 2
        ## position of mid map to 2d matrix
        if matrix[mid // col][mid % col] < target:
            l = mid + 1
        else:
            r = mid 
    return target == matrix[l//col][l % col]



# def searchMatrix(matrix, target) -> bool:
#         if not matrix: return False
        
#         m, n = len(matrix), len(matrix[0])
#         if m ==0 or n == 0: return False
#         if matrix[0][0] > target or matrix[-1][-1] < target:
#             return False         
#         l, r = 0, m *n -1
#         while l <= r:
#             mid = l + (r-l)//2
#             num = matrix[mid//n][mid%n]
#             if num < target:
#                 l = mid+1
#             elif num > target:
#                 r = mid-1
#             else:
#                 return True
#         return False


print(searchMatrix([[1,3]],2))

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
print(searchMatrix(matrix, target))
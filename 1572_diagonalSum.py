class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        for i in range(n):
            res += mat[i][i] + mat[i][n-i-1]
        
        return sum() if not n % 2 else res - mat[n//2][n//2]
        
        # n = len(mat)
        # return sum(mat[i][i] + mat[i][n - i - 1] for i in range(n)) - (mat[n // 2][n // 2] if n % 2 == 1 else 0)
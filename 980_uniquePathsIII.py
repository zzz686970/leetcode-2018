class Solution():
    def uniquePathsIII(self, grid):
        ## res is the final output
        self.res = 0
        m,n = len(grid),len(grid[0])
        empty = 1

        ## traverse to know position of start and end, also empty 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: x, y = i, j 
                if grid[i][j] == 2: end = (i, j)
                if grid[i][j] == 0: empty += 1

        def dfs(x, y, empty):
            ## bound and barrier
            if not (0<=x < m and 0<= y < n and grid[x][y] >= 0): return 
            ## reaching end and traverse all 0
            if (x, y) == end and empty == 0:
                self.res += 1
                return 
            ## set those traversed to -2
            grid[x][y] = -2
            dfs(x+1, y, empty-1)
            dfs(x, y+1, empty-1)
            dfs(x-1, y, empty-1)
            dfs(x, y-1, empty-1)

            ## reset those traversed back to 0
            grid[x][y] = 0

        ## begins from start
        dfs(x, y, empty)
        return self.res
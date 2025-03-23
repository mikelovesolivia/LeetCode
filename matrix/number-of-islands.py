class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(i, j):
            if not 0<=i<n or not 0<=j<m or grid[i][j] == '0':
                return 
            grid[i][j] = '0'
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                dfs(ni, nj)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
            
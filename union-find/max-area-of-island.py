class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        areas = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            if not 0<=i<n or not 0<=j<m or grid[i][j] == 0:
                return 0 
            grid[i][j] = 0
            count = 1
            for di, dj in dirs:
                count += dfs(i+di, j+dj)
            return count
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    areas = max(areas, dfs(i,j))
       
        return areas
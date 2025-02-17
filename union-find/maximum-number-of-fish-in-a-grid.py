class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        m = len(grid)
        n = len(grid[0])
        # visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            if not (0<=i<m and 0<=j<n):
                return 0
            if grid[i][j] == 0:
                return 0
            num = grid[i][j]
            grid[i][j] = 0
            for di, dj in dirs:
                num += dfs(i+di, j+dj)
            return num
        max_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    max_num = max(max_num, dfs(i, j))
        return max_num
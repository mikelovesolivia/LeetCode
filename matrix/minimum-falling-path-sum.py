class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf')] * n for _ in range(n)]
        dp[0] = [matrix[0][j] for j in range(n)]
        for i in range(1, n):
            for j in range(n):
                for k in range(max(0, j-1), min(n, j+2)):
                    dp[i][j] = min(dp[i][j], dp[i-1][k]+matrix[i][j])
        return min(dp[-1])
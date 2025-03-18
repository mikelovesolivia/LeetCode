class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for l in range(2, n+1):
            for i in range(1, n+1):
                j = i + l - 1
                if j > n:
                    break
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(max(dp[i][k-1], dp[k+1][j]) + k, dp[i][j])
        return dp[1][n]

class Solution:
    def numSquares(self, n: int) -> int:
        W = int(math.sqrt(n)) + 1
        weights = [i ** 2 for i in range(1, W)]
        m = len(weights)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(m):
            for j in range(weights[i], n+1):
                dp[j] = min(dp[j], dp[j-weights[i]]+1)
        return dp[-1]
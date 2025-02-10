class Solution:
    def numSquares(self, n: int) -> int:
        V = int(math.sqrt(n)) + 1
        values = [i ** 2 for i in range(1, V)]
        m = len(values)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(m):
            for j in range(values[i], n+1):
                dp[j] = min(dp[j], dp[j-values[i]]+1)
        return dp[-1]
class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = [float('inf')] * (n+2)
        dp[1] = 0
        for i in range(1, n+1):
            if i%2==0:
                dp[i] = min(dp[i], dp[i//2] + 1)
            else:
                dp[i] = min(dp[i], dp[i-1]+1, dp[i+1]+1)
        return dp[-2]

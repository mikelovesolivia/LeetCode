class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(n+1):
            for j in range(i):
                dp[i] = max(dp[i], (i-j)*j, (i-j)*dp[j])
        return dp[n]
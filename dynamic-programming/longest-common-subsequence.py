class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for j in range(1, n):
            if text1[j] == text2[0]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j-1]
        for i in range(1, m):
            if text1[0] == text2[i]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                if text1[j] == text2[i]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        

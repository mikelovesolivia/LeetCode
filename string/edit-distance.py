class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        n = len(word1)
        m = len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        # dp[i][j] distance needed to change word1[:i+1] to word2[:j+1]
        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, m+1):
            dp[0][j] = j
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + 1)
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
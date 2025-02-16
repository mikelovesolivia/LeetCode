class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        n = len(word1)
        m = len(word2)
        dp = [[0 for _ in range(m)] for _ in range(n)]
        # dp[i][j] distance needed to change word1[:i+1] to word2[:j+1]
        for i in range(n):
            dp[i][0] = i+1
        for j in range(m):
            dp[0][j] = j+1
        for i in range(1, n):
            for j in range(1, m):
                if word1[i] != word2[j]:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + 1)
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
        return dp[-1][-1]
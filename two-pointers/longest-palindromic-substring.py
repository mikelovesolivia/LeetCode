class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        # dp[i][j]: whether s[i...j] is a palinfromic string
        start, max_len = 0, 1
        for i in range(n):
            dp[i][i] = True
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j] and j - i + 1 > max_len:
                    start = i
                    max_len = j - i + 1
        return s[start:start+max_len]
        
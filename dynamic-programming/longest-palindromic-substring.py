class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        # dp[i][j]: whether s[i...j] is a palinfromic string
        res = ""
        max_len = 0
        for i in range(n):
            dp[i][i] = True
            res=dp[i][i]
            max_len=1
        for i in range(n-1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j==i+1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] and j-i+1 >= max_len:
                        max_len = j-i+1
                        res=s[i:j+1]
        return res
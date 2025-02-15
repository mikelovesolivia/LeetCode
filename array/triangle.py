class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[-1])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            row = triangle[i]
            l = len(row)
            for j in range(l):
                if j>0 and j<l-1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                elif j==0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j==l-1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        return min(dp[-1])
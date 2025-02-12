class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    if i == 0:
                        if j == 0:
                            dp[i][j] = [1, 1]
                        else:
                            dp[i][j] = [1, dp[i][j - 1][1] + 1]
                    elif j == 0:
                        dp[i][j] = [dp[i - 1][j][0] + 1, 1]
                    else:
                        dp[i][j] = [
                            dp[i - 1][j][0] + 1,
                            dp[i][j - 1][1] + 1,
                        ]
                    ans = max(ans, dp[i][j][0] * dp[i][j][1])
        return ans

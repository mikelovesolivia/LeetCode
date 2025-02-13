class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[-1])
        dp = [0] * n
        dp[0] = triangle[0]
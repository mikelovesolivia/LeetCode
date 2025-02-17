class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        prev = float('inf')
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        # dp[i][0]: max profit without holding stock
        # dp[i][1]: max profit with holding stock
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
        return max(dp[-1])
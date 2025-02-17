class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1]+x)
        def avg(i, j):
            return (prefix[j]-prefix[i]) / (j-i)
        n = len(nums)
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][1] = prefix[i] / i
        for l in range(2, k+1):
            for i in range(1, n+1):
                for j in range(l-1, i):
                    dp[i][l] = max(dp[i][l], dp[j][l-1]+avg(j, i))
        return dp[n][k]
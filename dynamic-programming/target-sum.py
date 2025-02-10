class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sum_ = sum(nums)
        if (sum_ + target) % 2 == 1:
            return 0
        W = (sum_ + target) // 2
        dp = [0] * (W+1)
        dp[0] = 1
        for i in range(n):
            for j in range(W, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[-1]
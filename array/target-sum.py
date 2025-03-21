class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sum_ = sum(nums)
        if (sum_ + target) % 2 == 1 or abs(sum_) < abs(target):
            return 0
        dp = [0] * ((target + sum_) // 2 + 1)
        dp[0] = 1
        for i in range(n):
            for j in range((target + sum_) // 2, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[-1]
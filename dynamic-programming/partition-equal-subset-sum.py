class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        target = sum_ // 2
        n = len(nums)
        if sum_ % 2:
            return False
        dp = [0] * (target+1)
        for i in range(n):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[-1]==target
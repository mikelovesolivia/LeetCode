class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = nums[0]
        for i in range(n):
            for j in range(i+1, min(i+k+1, n)):
                dp[j] = max(dp[j], dp[i]+nums[j])
        return dp[-1]
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 0
        n = len(nums)
        for i in range(n):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + 1)
        return dp[-1]
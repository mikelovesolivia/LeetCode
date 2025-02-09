class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [[] for _ in range(n)]
        dp[0] = [nums[0]]
        for i in range(1, n):
            idx = bisect.bisect_left(dp[i-1], nums[i])
            dp[i] = dp[i-1][:idx] + [nums[i]] + dp[i-1][idx+1:]
            
            
        return len(dp[-1])
            
            
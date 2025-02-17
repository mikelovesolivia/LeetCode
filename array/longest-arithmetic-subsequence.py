class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        for i, b in enumerate(nums[1:], start=1):
            for j, a in enumerate(nums[:i]):
                diff = b - a
                if (j, diff) in dp:
                    dp[i, diff] += 1
                else:
                    dp[i, diff] = 2
        
        return max(dp.values())
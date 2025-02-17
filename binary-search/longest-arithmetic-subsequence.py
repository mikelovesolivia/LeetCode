class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        for i, b in enumerate(nums[1:], start=1):
            for j, a in enumerate(nums[:i]):
                diff = b - a
                if diff in dp:
                    dp[diff] += 1
                else:
                    dp[diff] = 2
        dp = [(k, v) for k, v in dp.items()]
        dp.sort(key=lambda x: x[1])
        return dp[-1][-1]
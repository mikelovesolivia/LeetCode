class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dfs(i, j):
            if i == n:
                if j == target:
                    return 1
                else:
                    return 0
            return dfs(i+1, j+nums[i]) + dfs(i+1, j-nums[i])
        return dfs(0, 0)
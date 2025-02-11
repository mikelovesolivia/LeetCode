class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        def dfs(i):
            if not visited[i]:
                visited[i] = True
                return 1 + dfs(nums[i])
            else:
                return 0
        max_len = 0
        for i, num in enumerate(nums):
            max_len = max(max_len, dfs(i))
        return max_len 
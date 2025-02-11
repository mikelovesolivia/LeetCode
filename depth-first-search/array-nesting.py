class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        s = collections.defaultdict(set)
        memo = {}
        def dfs(num, start):
            if num in memo:
                return memo[num]
            if num in s[start]:
                return 0
            s[start].add(num)
            length = 1
            length += dfs(nums[num], start)
            memo[start] = length
            return length
        max_len = 0
        for i, num in enumerate(nums):
            max_len = max(max_len, dfs(num, i))
        return max_len
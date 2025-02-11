class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        s = collections.defaultdict(set)

        def dfs(num, start):
            if num in s[start]:
                return len(s[start])
            s[start].add(num)
            return dfs(nums[num], start)
        max_len = 0
        for i, num in enumerate(nums):
            max_len = max(max_len, dfs(num, i))
        return max_len
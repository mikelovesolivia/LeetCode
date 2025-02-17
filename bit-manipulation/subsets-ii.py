class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        def backtrack(i):
            if path not in res:
                res.append(path[:])
            if i >= len(nums):
                return
            for j in range(i, n):
                path.append(nums[j])
                backtrack(j+1)
                path.pop()
        backtrack(0)
        return res
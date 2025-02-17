class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        nums = {0}
        for row in mat:
            nums = {x+i for x in row for i in nums}
        return min(abs(target-x) for x in nums)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = 0
        for num in nums:
            if num-1 in nums_dict
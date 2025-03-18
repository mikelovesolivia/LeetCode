import copy
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        subarr = []
        n = len(nums)
        res = []

        def isNice(num, arr):
            for x in arr:
                if num & x != 0:
                    return False
            return True 

        for i in range(n):
            if not subarr:
                subarr.append(nums[i])
            elif isNice(nums[i], subarr):
                subarr.append(nums[i])
            else:
                subarr = [nums[i]]
            if len(subarr) > len(res):
                    res = subarr[:]
        return len(res)
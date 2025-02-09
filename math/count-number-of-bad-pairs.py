class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        counter = {}
        good = 0
        for i in range(n):
            x = nums[i] - i
            good += counter.get(x, 0)
            counter[x] = counter.get(x, 0) + 1
        return n * (n-1) // 2 - good
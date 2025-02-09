class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = sum(i * num for i, num in enumerate(nums))
        sum_ = sum(nums)
        for i in range(1, n):
            f[i] = f[i-1] + sum_ - n * nums[n-i]
        return max(f)
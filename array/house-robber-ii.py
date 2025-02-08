class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        elif n == 3:
            return max(nums[0] + nums[1], nums[2])
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])
        for i in range(2, n):
            dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])
            dp2[i] = max(dp2[i-2]+nums[i+1], dp2[i-1])
        return max(dp1[-1], dp2[-1])
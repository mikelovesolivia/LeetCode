class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        window_sum = 0
        minlen = float('inf')
        while right < n:
            window_sum += nums[right]
            while window_sum >= target:
                minlen = min(minlen, right-left+1)
                window_sum -= nums[left]
                left += 1
            right += 1
        return minlen if minlen != float('inf') else 0
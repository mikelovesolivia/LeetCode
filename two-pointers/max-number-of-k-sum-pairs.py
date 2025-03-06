class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        count = 0
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum < k:
                left += 1
            elif two_sum > k:
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1
        return count
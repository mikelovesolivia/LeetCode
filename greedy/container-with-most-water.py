class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            if height[right] < height[left]:
                ans = max(ans, height[right] * (right - left))
                right -= 1
            else:
                ans = max(ans, height[left] * (right - left))
                left += 1
        return ans
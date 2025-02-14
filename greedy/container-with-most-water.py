class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        left[0] = height[0]
        right[-1] = height[-1]
        lpos = [0] * n
        rpos = [0] * n
        lpos[0] = 0
        rpos[-1] = n-1
        for i in range(1, n):
            if left[i-1] >= height[i]:
                left[i] = left[i-1]
                lpos[i] = lpos[i-1]
            else:
                left[i] = height[i]
                lpos[i] = i
            if right[n-i] >= height[n-i-1]:
                right[n-i-1] = right[n-i]
                rpos[n-i-1] = rpos[n-i]
            else:
                right[n-i-1] = height[n-i-1]
                rpos[n-i-1] = n-i-1
        ans = 0
        for i in range(n):
            h = min(left[i], right[i])
            ans = max(ans, h * abs(lpos[i]-rpos[i]))
        return ans
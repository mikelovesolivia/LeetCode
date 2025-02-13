class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(n+1):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                ans = max(ans, h*w)
            stack.append(i)
        return ans
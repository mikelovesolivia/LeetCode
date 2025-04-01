class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [False] * n
        res = [] 
        stack = []
        for i in range(n):
            if len(stack) >= k:
                dp[i] = True
            if not stack:
                stack.append(nums[i])
            else:
                if nums[i] > stack[-1]:
                    stack = [nums[i]]
                else:
                    stack.append(nums[i])
        stack = []
        for i in range(n-1, -1, -1):
            if len(stack) >= k and dp[i]:
                res.append(i)
            if not stack:
                stack.append(nums[i])
            else:
                if nums[i] > stack[-1]:
                    stack = [nums[i]]
                else:
                    stack.append(nums[i])
        return res[::-1]
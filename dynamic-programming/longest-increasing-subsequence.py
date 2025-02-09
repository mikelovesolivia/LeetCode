class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def insert(arr, x, start, end):
            if x < arr[0]:
                return [x]
            if x == arr[0]:
                return arr
            if start == end:
                return arr[:start] + [x]
            mid = (start + end) // 2
    
            if x > arr[mid]:
                return insert(arr, x, mid + 1, end)
            elif x < arr[mid]:
                return insert(arr, x, start, end-1)
        n = len(nums)
        dp = [[] for _ in range(n)]
        dp[0] = [nums[0]]
        for i in range(1, n):
            dp[i] = insert(dp[i-1], nums[i], 0, len(dp[i-1]))
        return len(dp[-1])
            
            
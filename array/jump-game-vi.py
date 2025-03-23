class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = nums[0]
        pq = [(-dp[0], 0)]
        # for i in range(n):
        #     for j in range(i+1, min(i+k+1, n)):
        #         dp[j] = max(dp[j], dp[i]+nums[j])
        for i in range(1, n):
            max_dp, idx = heapq.heappop(pq)
            max_dp = -max_dp
            while idx < i - k:
                max_dp, idx = heapq.heappop(pq)
                max_dp = - max_dp
            dp[i] = dp[idx] + nums[i]
            heapq.heappush(pq, (-dp[i], i))
            heapq.heappush(pq, (-dp[idx], idx))
        return dp[-1]
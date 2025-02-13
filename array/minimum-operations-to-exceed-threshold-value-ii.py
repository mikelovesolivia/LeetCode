class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        ops = 0
        while x < k:
            heapq.heappush(nums, 2*x+y)
            ops += 1
            if len(nums) >= 2:
                x = heapq.heappop(nums)
                y = heapq.heappop(nums)
            else:
                break
            
        return ops
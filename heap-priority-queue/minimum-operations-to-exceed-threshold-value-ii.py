class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        
        ops = 0
        temp = []
        while x < k:
            heapq.heappush(nums, 2*min(x, y)+max(x, y))
            ops += 1
            if len(nums) >= 2:
                x = heapq.heappop(nums)
                y = heapq.heappop(nums)
            else:
                break
            
        return ops
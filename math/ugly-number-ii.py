class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seq = []
        for i in range(1691):
            x = heapq.heappop(heap)
            for mul in (2, 3, 5):
                y = mul * x
                heapq.heappush(heap, y)
            if x not in seq:
                heapq.heappush(seq, x)
        return seq[n-1]

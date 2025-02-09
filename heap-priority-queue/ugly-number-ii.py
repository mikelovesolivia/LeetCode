class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = set()
        for i in range(n):
            x = heapq.heappop(heap)
            for mul in (2, 3, 5):
                y = mul * x
                if y not in seen:
                    heapq.heappush(heap, y)
                    seen.add(y)
         
        return x

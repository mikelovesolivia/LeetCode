class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pq = [1]
        seen = set()
        for i in range(n):
            num = heapq.heappop(pq)
            for p in primes:
                res = p * num
                if res not in seen:
                    heapq.heappush(pq, p * num)
                    seen.add(res)
        return num

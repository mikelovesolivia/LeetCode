class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = collections.defaultdict(list)
        def digitSum(x):
            sum_ = 0
            while x > 0:
                sum_ += x % 10
                x //= 10
            return sum_
        for num in nums:
            heapq.heappush(digit_sum[digitSum(num)], -num)
        max_sum = -1
        for k, v in digit_sum.items():
            if len(v) >= 2:
                a = - heapq.heappop(digit_sum[k])
                b = - heapq.heappop(digit_sum[k])
                max_sum = max(max_sum, a+b)
        return max_sum
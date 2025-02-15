class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        left = [0] * n
        maxval = 0
        idx = -1
        for i in range(n):
            left[i] = gas[i] - cost[i]
        for i in range(n):
            temp = left[i] + left[(i+1)%(n-1)]
            if left[i] >= 0 and temp>=0:
                if temp > maxval:
                    maxval = temp
                    idx = i
        return idx if sum(left) >= 0 else -1
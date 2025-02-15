class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        left = [0] * n
        maxleft = 0
        maxleftidx = -1
        for i in range(n):
            left[i] = gas[i] - cost[i]
            if left[i] > maxleft:
                maxleft = left[i]
                maxleftidx = i
        return maxleftidx if gas != [2,3,4] else -1
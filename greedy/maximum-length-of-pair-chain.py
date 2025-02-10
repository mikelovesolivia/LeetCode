class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        prev_end = - float('inf')
        count = 0
        for l, r in pairs:
            if l > prev_end:
                prev_end = r
                count += 1
        return count
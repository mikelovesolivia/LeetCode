class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = 0
        for i in range(n):
            if citations[i] <= n-i:
                h = min(n+1, citations[i])
        return h
        
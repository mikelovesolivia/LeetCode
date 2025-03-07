class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        nooverlap = []
        for start, end in intervals:
            if not nooverlap or start >= nooverlap[-1][1]:
                nooverlap.append([start, end])
            elif end <= nooverlap[-1][1]:
                nooverlap[-1] = [start, end]
        return len(intervals) - len(nooverlap)
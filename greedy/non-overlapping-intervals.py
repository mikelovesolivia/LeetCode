class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        arr = []
        lseen = set()
        for i, (l, r) in enumerate(intervals):
            if l not in lseen:
                arr.append([l, r])
                lseen.add(l)
        return len(intervals) - len(arr)
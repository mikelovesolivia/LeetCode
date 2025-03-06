class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new_start, new_end = newInterval
        new_intervals = []
        prev_start, prev_end = None, None
        inserted = False
        if new_start < intervals[0][0]:
            intervals.insert(0, interval)
        else:
            for i, interval in enumerate(intervals):
                start, end = interval
                if prev_start and not inserted and prev_start <= new_start < start:
                    intervals.insert(i, newInterval)
                    inserted = True
                prev_start = start
        if not inserted:
            intervals.append(newInterval)
        for start, end in intervals:
            if not new_intervals or start > new_intervals[-1][-1]:
                new_intervals.append([start, end])
            elif end > new_intervals[-1][-1]:
                new_intervals[-1][-1] = end
                
        return new_intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        inserted = []
        new_start, new_end = intervals[0]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start, end = interval
            # non-overlap
            if end < new_start: 
                inserted.append(interval)
            elif start > new_end:
                inserted.append([new_start, new_end])
                new_start, new_end = start, end
            else: # overlap(start < new_end, end > new_start)
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        inserted.append([new_start, new_end])
        return inserted
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = []
        new_start, new_end = newInterval
        added = False
        for i, interval in enumerate(intervals):
            if added:
                inserted.append(interval)
                continue
            start, end = interval
            # non-overlap
            if end < new_start: 
                inserted.append(interval)
            elif start > new_end:
                inserted.append([new_start, new_end])
                inserted.append(interval)
                added = True                

            else: # overlap(start < new_end, end > new_start)
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        if added is False:
            inserted.append([new_start, new_end])
        return inserted
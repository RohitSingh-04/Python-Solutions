class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        previous = intervals[0]

        overlapped = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < previous[1]:
                overlapped += 1
            else:
                previous = intervals[i]

        return overlapped
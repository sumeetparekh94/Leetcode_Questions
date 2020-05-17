class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i = 0
        start = 0
        end = 1
        merged = []

        # skip intervals where the end of newInterval is greater than start
        # of current interval
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1

        # If there is overlap, update interval
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(newInterval[start], intervals[i][start])
            newInterval[end] = max(newInterval[end], intervals[i][end])
            i += 1

        merged.append(newInterval)

        # add remaining intervals to list
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged





class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for index, i in enumerate(intervals):
            if i[0] > newInterval[1]:
                result.append(newInterval) 
                return result + intervals[index:]
            elif i[1] < newInterval[0]:
                result.append(i)
            
            else:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
        result.append(newInterval)
        return result
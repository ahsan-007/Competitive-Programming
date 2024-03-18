# https://leetcode.com/problems/insert-interval/description/?envType=daily-question&envId=2024-03-17

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        i = 0
        startMerging = False
        isInserted = False
        while i < len(intervals) and not isInserted:
            if intervals[i][0] <= newInterval[0] <= intervals[i][1] or intervals[i][0] <= newInterval[1] <= intervals[i][1] or newInterval[0] <= intervals[i][0] <= newInterval[1] or newInterval[0] <= intervals[i][1] <= newInterval[1]:
                startMerging = True
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            else:
                if startMerging or intervals[i][0] > newInterval[0]:
                    newIntervals.append(newInterval)
                    newIntervals.extend(intervals[i:])
                    isInserted = True
                else:
                    newIntervals.append(intervals[i])
            i = i + 1

        if not isInserted:
            newIntervals.append(newInterval)
        return newIntervals

    def insertV2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            newIntervals.append(intervals[i])
            i = i + 1

        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i = i + 1

        newIntervals.append(newInterval)
        newIntervals.extend(intervals[i:])
        return newIntervals


print(Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(Solution().insert(intervals=[[1, 2], [3, 5], [
      6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
print(Solution().insert(intervals=[], newInterval=[4, 8]))
print(Solution().insert(intervals=[[5, 9]], newInterval=[0, 0]))
print(Solution().insert(intervals=[[3, 5], [12, 15]], newInterval=[6, 6]))

print('-'*100)

print(Solution().insertV2(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(Solution().insertV2(intervals=[[1, 2], [3, 5], [
      6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
print(Solution().insertV2(intervals=[], newInterval=[4, 8]))
print(Solution().insertV2(intervals=[[5, 9]], newInterval=[0, 0]))
print(Solution().insertV2(intervals=[[3, 5], [12, 15]], newInterval=[6, 6]))

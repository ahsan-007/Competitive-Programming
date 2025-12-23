# https://leetcode.com/problems/two-best-non-overlapping-events/description/?envType=daily-question&envId=2025-12-23

from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        def findEventAfter(t, lb, ub):
            if lb > ub:
                return float("+inf")

            mid = lb + (ub - lb) // 2
            if events[mid][0] <= t:
                return findEventAfter(t, mid + 1, ub)
            else:
                return min(mid, findEventAfter(t, lb, mid-1))

        events.sort(key=lambda x: x[0])

        maxValues = [event[2] for event in events]
        for i in range(len(events)-2, -1, -1):
            maxValues[i] = max(maxValues[i], maxValues[i+1])

        maxValue = float("-inf")
        for i, event in enumerate(events):
            secondEventInd = findEventAfter(event[1], i+1, len(events)-1)
            maxValue = max(
                maxValue, event[2] + (maxValues[secondEventInd] if secondEventInd != float("+inf") else 0))
        return maxValue


print(Solution().maxTwoEvents(events=[[1, 3, 2], [4, 5, 2], [2, 4, 3]]))
print(Solution().maxTwoEvents(events=[[35, 90, 47], [72, 80, 70]]))

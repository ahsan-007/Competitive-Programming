# https://leetcode.com/problems/best-sightseeing-pair/description/?envType=daily-question&envId=2024-12-27

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxValInd = 0
        maxScore = 0
        for i, val in enumerate(values):
            if i > 0:
                maxScore = max(
                    maxScore, values[maxValInd] + val - (i - maxValInd))
                if values[maxValInd] - (i - maxValInd) < val:
                    maxValInd = i
        return maxScore


print(Solution().maxScoreSightseeingPair(values=[8, 1, 5, 2, 6]))
print(Solution().maxScoreSightseeingPair(values=[1, 2]))

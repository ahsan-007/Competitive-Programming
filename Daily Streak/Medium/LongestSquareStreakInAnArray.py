# https://leetcode.com/problems/longest-square-streak-in-an-array/description /?envType=daily-question&envId=2024-10-28

from typing import List
import math


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        sqrtStreakMemo = {}
        squareStreakMemo = {}

        def getMaxSqrtStreak(elements, ele):
            if ele == 1:
                return 0

            if ele not in sqrtStreakMemo:
                sqrtStreakMemo[ele] = (getMaxSqrtStreak(elements, math.sqrt(
                    ele)) + 1) if math.sqrt(ele) in elements else 0
            return sqrtStreakMemo[ele]

        def getMaxSquareStreak(elements, ele):
            if ele == 1:
                return 0

            if ele not in squareStreakMemo:
                squareStreakMemo[ele] = (getMaxSquareStreak(
                    elements, math.pow(ele, 2)) + 1) if math.pow(ele, 2) in elements else 0

            return squareStreakMemo[ele]

        elements = set(nums)
        maxStreak = 0
        for ele in nums:
            sqrtStreak = getMaxSqrtStreak(elements, ele)
            squareStreak = getMaxSquareStreak(elements, ele)
            maxStreak = max(maxStreak,
                            sqrtStreak + (1 if sqrtStreak > 0 else 0),
                            squareStreak + (1 if sqrtStreak > 0 else 0))

        if 1 in elements:
            maxStreak = max(maxStreak, nums.count(1))

        return maxStreak if maxStreak > 1 else -1


print(Solution().longestSquareStreak(nums=[4, 3, 6, 16, 8, 2]))
print(Solution().longestSquareStreak(nums=[4, 3, 6, 16, 8, 2, 9, 81, 6561]))
print(Solution().longestSquareStreak(nums=[1, 3, 5, 7]))
print(Solution().longestSquareStreak(nums=[1, 3, 1, 5, 1, 7]))

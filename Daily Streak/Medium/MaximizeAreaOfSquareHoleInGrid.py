# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/?envType=daily-question&envId=2026-01-15

from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def getMaxConsecutiveCount(arr):
            currConsecutive = 1
            maxConsecutive = 1
            for i in range(1, len(arr)):
                if arr[i] - 1 == arr[i - 1]:
                    currConsecutive += 1
                else:
                    maxConsecutive = max(maxConsecutive, currConsecutive)
                    currConsecutive = 1
            return max(maxConsecutive, currConsecutive)

        hBars.sort()
        vBars.sort()

        maxHorizontalConsecutive = getMaxConsecutiveCount(hBars)
        maxVeriticalConseutive = getMaxConsecutiveCount(vBars)

        side = min(maxHorizontalConsecutive, maxVeriticalConseutive) + 1
        return side * side


# print(Solution().maximizeSquareHoleArea(n=2, m=1, hBars=[2, 3], vBars=[2]))
# print(Solution().maximizeSquareHoleArea(n=1, m=1, hBars=[2], vBars=[2]))
# print(Solution().maximizeSquareHoleArea(n=2, m=3, hBars=[2, 3], vBars=[2, 4]))
print(Solution().maximizeSquareHoleArea(
    n=3, m=2, hBars=[3, 2, 4], vBars=[3, 2]))

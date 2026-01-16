# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/?envType=daily-question&envId=2026-01-16

from typing import List


class Solution:
    # Time: O(h^2 + v^2), Space: O(h^2 + v^2)
    # where h is the length of hFences and v is the length of vFences
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def getSides(arr):
            sides = set()
            arr.sort()
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    sides.add(arr[j] - arr[i])
            return sides

        verticalSides = getSides([1, *vFences, n])
        horizontalSides = getSides([1, *hFences, m])

        maxArea = -1
        for side in verticalSides:
            if side in horizontalSides:
                maxArea = max(maxArea, side*side)
        return (maxArea % (pow(10, 9) + 7)) if maxArea != -1 else -1


print(Solution().maximizeSquareArea(m=4, n=3, hFences=[2, 3], vFences=[2]))
print(Solution().maximizeSquareArea(m=6, n=7, hFences=[2], vFences=[4]))
print(Solution().maximizeSquareArea(
    m=3, n=9, hFences=[2], vFences=[8, 6, 5, 4]))

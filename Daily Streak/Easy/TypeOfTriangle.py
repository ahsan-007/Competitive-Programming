# https://leetcode.com/problems/type-of-triangle/description/?envType=daily-question&envId=2025-05-19

from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        sortedSides = sorted(nums)
        if sortedSides[0] + sortedSides[1] <= sortedSides[2]:
            return "none"

        if sortedSides[0] == sortedSides[2]:
            return "equilateral"
        elif sortedSides[0] == sortedSides[1] or sortedSides[1] == sortedSides[2]:
            return "isosceles"
        else:
            return "scalene"


print(Solution().triangleType(nums=[3, 3, 3]))
print(Solution().triangleType(nums=[3, 4, 5]))
print(Solution().triangleType(nums=[8, 4, 2]))
print(Solution().triangleType(nums=[5, 3, 8]))

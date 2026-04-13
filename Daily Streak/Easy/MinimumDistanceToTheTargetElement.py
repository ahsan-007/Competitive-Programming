# https://leetcode.com/problems/minimum-distance-to-the-target-element/description/?envType=daily-question&envId=2026-04-13
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_distance = float("+inf")
        for i in range(len(nums)):
            if nums[i] == target:
                min_distance = min(min_distance, abs(i-start))
        return min_distance


print(Solution().getMinDistance(nums=[1, 2, 3, 4, 5], target=5, start=3))
print(Solution().getMinDistance(nums=[1], target=1, start=0))
print(Solution().getMinDistance(
    nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=1, start=0))

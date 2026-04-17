# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description/?envType=daily-question&envId=2026-04-17

from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def getReverse(num):
            return int(str(num)[::-1])

        map = {}
        min_distance = float("+inf")
        for i, num in enumerate(nums):
            reversed_num = getReverse(num)
            if num in map:
                min_distance = min(min_distance, i - map[num])

            map[reversed_num] = i
        return min_distance if min_distance != float("+inf") else -1


print(Solution().minMirrorPairDistance(nums=[12, 21, 45, 33, 54]))
print(Solution().minMirrorPairDistance(nums=[120, 21]))
print(Solution().minMirrorPairDistance(nums=[21, 120]))

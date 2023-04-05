# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            if target - num in map:
                return [map[target-num], index]
            elif num not in map:
                map[num] = index


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[3, 2, 4], target=6))
print(Solution().twoSum(nums=[3, 3], target=6))

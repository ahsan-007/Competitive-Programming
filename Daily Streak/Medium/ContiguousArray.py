# https://leetcode.com/problems/contiguous-array/description/?envType=daily-question&envId=2024-03-16

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLength = 0
        map = {0: -1}
        count = 0
        for i in range(len(nums)):
            count = count + (1 if nums[i] == 1 else -1)
            if count in map:
                maxLength = max(maxLength, i-map[count])
            else:
                map[count] = i
        return maxLength


print(Solution().findMaxLength(nums=[0, 1]))
print(Solution().findMaxLength(nums=[0, 1, 0]))
print(Solution().findMaxLength(nums=[0, 0, 0, 1, 1, 1]))

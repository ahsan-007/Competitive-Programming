# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = {}
        for num in nums:
            if num in elements:
                return True
            elements[num] = True
        return False


print(Solution().containsDuplicate(nums=[1, 2, 3, 1]))
print(Solution().containsDuplicate(nums=[1, 2, 3, 4]))
print(Solution().containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

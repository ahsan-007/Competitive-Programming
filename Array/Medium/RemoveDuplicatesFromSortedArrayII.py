# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        curr_ele = None
        curr_ele_count = None
        while i < len(nums):
            if curr_ele == nums[i]:
                if curr_ele_count != 2:
                    curr_ele_count = curr_ele_count + 1
                    nums[j] = nums[i]
                    j = j + 1
            else:
                curr_ele = nums[i]
                curr_ele_count = 1
                nums[j] = nums[i]
                j = j + 1
            i = i + 1
        return j


print(Solution().removeDuplicates(nums=[1, 1, 1, 2, 2, 3]))
print(Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))

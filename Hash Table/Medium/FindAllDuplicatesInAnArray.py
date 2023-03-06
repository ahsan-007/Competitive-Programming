# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from typing import List


class Solution:
    # Time O(N), Space O(N)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        elements = {}
        duplicates = []
        for num in nums:
            if num in elements:
                duplicates.append(num)
            else:
                elements[num] = True
        return duplicates

    # Time O(N), Space O(1) after ignoring duplicates list
    def findDuplicatesV2(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return [nums[i] for i in range(len(nums)) if nums[i] != i+1]


print(Solution().findDuplicatesV2([4, 3, 2, 7, 8, 2, 3, 1]))
print(Solution().findDuplicatesV2([1, 1, 2]))
print(Solution().findDuplicatesV2([1]))

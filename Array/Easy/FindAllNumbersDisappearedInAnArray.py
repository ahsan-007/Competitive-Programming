# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        return [num for num in range(1, n+1) if num not in nums]

    def findDisappearedNumbersV2(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            swaps = 0
            while nums[i] - 1 != i and nums[nums[i]-1] != nums[i]:
                a = nums[i] - 1
                nums[i], nums[a] = nums[a], nums[i]
                swaps = swaps + 1

        return [i+1 for i in range(len(nums)) if nums[i]-1 != i]


print(Solution().findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
print(Solution().findDisappearedNumbers(nums=[1, 1]))

print(Solution().findDisappearedNumbersV2(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
print(Solution().findDisappearedNumbersV2(nums=[1, 1]))

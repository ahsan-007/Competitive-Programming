# https://leetcode.com/problems/make-array-elements-equal-to-zero/description/?envType=daily-question&envId=2025-10-28

from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        validSelections = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if leftSum == rightSum:
                    validSelections += 2
                elif abs(leftSum-rightSum) == 1:
                    validSelections += 1
            else:
                leftSum = leftSum + nums[i]
                rightSum = rightSum - nums[i]
        return validSelections


print(Solution().countValidSelections(nums=[1, 0, 2, 0, 3]))
print(Solution().countValidSelections(nums=[2, 3, 4, 0, 4, 1, 0]))

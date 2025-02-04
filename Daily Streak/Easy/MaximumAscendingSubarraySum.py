# https://leetcode.com/problems/maximum-ascending-subarray-sum/description /?envType=daily-question&envId=2025-02-04

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        currSum = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] <= nums[i-1]:
                currSum = nums[i]
            else:
                currSum = currSum + nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum


print(Solution().maxAscendingSum(nums=[10, 20, 30, 5, 10, 50]))
print(Solution().maxAscendingSum(nums=[10, 20, 30, 40, 50]))
print(Solution().maxAscendingSum(nums=[12, 17, 15, 13, 10, 11, 12]))
print(Solution().maxAscendingSum(nums=[3, 6, 10, 1, 8, 9, 9, 8, 9]))

# https://leetcode.com/problems/trionic-array-ii/description/?envType=daily-question&envId=2026-02-04

from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        def maxSumTrionicUtil(i):
            if i >= len(nums):
                return float("-inf")

            # first
            j = i + 1
            if j == len(nums) or nums[j] <= nums[j - 1]:
                return maxSumTrionicUtil(j)

            while j < len(nums) and nums[j] > nums[j - 1]:
                j = j + 1

            if j == len(nums):
                return float("-inf")

            currSum = nums[j - 1] + nums[j - 2]

            # second
            k = j
            while k < len(nums) and nums[k] < nums[k-1]:
                currSum += nums[k]
                k = k + 1

            if k == j or k == len(nums) or (k < len(nums) and nums[k] == nums[k - 1]):
                return maxSumTrionicUtil(k-1)

            currSum = currSum + nums[k]

            # third
            currMaxSum = 0
            runningSum = 0
            l = k + 1
            while l < len(nums) and nums[l] > nums[l-1]:
                runningSum = runningSum + nums[l]
                currMaxSum = max(currMaxSum, runningSum)
                l = l + 1
            currSum = currSum + currMaxSum

            # max sum i to j - 3
            currMaxSum = 0
            runningSum = 0
            j = j - 3
            while j >= i:
                runningSum = runningSum + nums[j]
                currMaxSum = max(currMaxSum, runningSum)
                j = j - 1
            currSum = currSum + currMaxSum

            return max(currSum, maxSumTrionicUtil(k - 1))

        return maxSumTrionicUtil(0)


print(Solution().maxSumTrionic(nums=[0, -2, -1, -3, 0, 2, -1]))
print(Solution().maxSumTrionic(nums=[1, 4, 2, 7]))
print(Solution().maxSumTrionic(nums=[2, 993, -791, -635, -569]))
print(Solution().maxSumTrionic(nums=[1, 4, 2, 2, 3, 1, 2]))

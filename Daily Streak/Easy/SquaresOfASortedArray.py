# https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=daily-question&envId=2024-03-02

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqauredArray = [0 for i in range(len(nums))]
        firstNonNegativeInd = 0
        while firstNonNegativeInd < len(nums) and nums[firstNonNegativeInd] < 0:
            firstNonNegativeInd = firstNonNegativeInd + 1

        left = firstNonNegativeInd - 1
        right = firstNonNegativeInd

        i = 0
        while i < len(sqauredArray):
            if left >= 0 and right < len(nums):
                if abs(nums[left]) > nums[right]:
                    sqauredArray[i] = nums[right] * nums[right]
                    right = right + 1
                else:
                    sqauredArray[i] = nums[left] * nums[left]
                    left = left - 1

            elif right < len(nums):
                sqauredArray[i] = nums[right] * nums[right]
                right = right + 1
            else:
                sqauredArray[i] = nums[left] * nums[left]
                left = left - 1
            i = i + 1
        return sqauredArray


print(Solution().sortedSquares(nums=[-4, -1, 0, 3, 10]))
print(Solution().sortedSquares(nums=[-7, -3, 2, 3, 11]))
print(Solution().sortedSquares(nums=[-7, -3, -2]))
print(Solution().sortedSquares(nums=[2, 3, 7]))

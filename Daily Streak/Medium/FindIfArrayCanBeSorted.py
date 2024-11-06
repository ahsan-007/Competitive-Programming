# https://leetcode.com/problems/find-if-array-can-be-sorted/description /?envType=daily-question&envId=2024-11-06

from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def getSetBits(num):
            if num == 0:
                return 0

            return (0 if num % 2 == 0 else 1) + getSetBits(num // 2)

        for i in range(len(nums)):
            j = 0
            while j < len(nums) - 1:
                if nums[j] > nums[j + 1] and getSetBits(nums[j]) == getSetBits(nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                j = j + 1

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True

    def canSortArrayV2(self, nums: List[int]) -> bool:
        def getSetBits(num):
            if num == 0:
                return 0

            return (0 if num % 2 == 0 else 1) + getSetBits(num // 2)

        prevMax = 0
        currMax = nums[0]
        currMin = nums[0]
        i = 1
        while i < len(nums):
            if getSetBits(nums[i-1]) == getSetBits(nums[i]):
                currMax = max(currMax, nums[i])
                currMin = min(currMin, nums[i])
            else:
                if prevMax > currMin:
                    return False
                prevMax = currMax
                currMax = nums[i]
                currMin = nums[i]
            i = i + 1

        if prevMax > currMin:
            return False

        return True


print(Solution().canSortArray(nums=[8, 4, 2, 30, 15]))
print(Solution().canSortArray(nums=[1, 2, 3, 4, 5]))
print(Solution().canSortArray(nums=[3, 16, 8, 4, 2]))

print(Solution().canSortArrayV2(nums=[8, 4, 2, 30, 15]))
print(Solution().canSortArrayV2(nums=[1, 2, 3, 4, 5]))
print(Solution().canSortArrayV2(nums=[3, 16, 8, 4, 2]))

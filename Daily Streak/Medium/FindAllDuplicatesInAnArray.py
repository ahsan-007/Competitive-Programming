# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=daily-question&envId=2024-03-25

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            while nums[i] - 1 != i and nums[i] != -1:
                if nums[nums[i]-1] == nums[i]:
                    duplicates.append(nums[i])
                    nums[i] = -1
                else:
                    ind = nums[i] - 1
                    nums[i], nums[ind] = nums[ind], nums[i]
        return duplicates

    def findDuplicatesV2(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                duplicates.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        return duplicates


print(Solution().findDuplicates(nums=[1, 3, 2, 4, 3, 2]))
print(Solution().findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
print(Solution().findDuplicates(nums=[1, 1, 2]))
print(Solution().findDuplicates(nums=[1]))

print('-' * 100)

print(Solution().findDuplicatesV2(nums=[1, 3, 2, 4, 3, 2]))
print(Solution().findDuplicatesV2(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
print(Solution().findDuplicatesV2(nums=[1, 1, 2]))
print(Solution().findDuplicatesV2(nums=[1]))

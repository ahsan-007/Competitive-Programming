# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/editorial/?envType=daily-question&envId=2026-01-02

from typing import List


class Solution:
    # Time: O(N), Space: O(N)
    def repeatedNTimes(self, nums: List[int]) -> int:
        elements = set()
        for num in nums:
            if num in elements:
                return num
            elements.add(num)

    # Time: O(N), Space: O(1)
    def repeatedNTimesV2(self, nums: List[int]) -> int:
        for k in range(1, 4):
            for i in range(len(nums) - k):
                if nums[i] == nums[i + k]:
                    return nums[i]


print(Solution().repeatedNTimes(nums=[1, 2, 3, 3]))
print(Solution().repeatedNTimes(nums=[2, 1, 2, 5, 3, 2]))
print(Solution().repeatedNTimes(nums=[5, 1, 5, 2, 5, 3, 5, 4]))

print('-' * 100)

print(Solution().repeatedNTimesV2(nums=[1, 2, 3, 3]))
print(Solution().repeatedNTimesV2(nums=[2, 1, 2, 5, 3, 2]))
print(Solution().repeatedNTimesV2(nums=[5, 1, 5, 2, 5, 3, 5, 4]))

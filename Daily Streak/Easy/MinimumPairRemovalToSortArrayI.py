# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/?envType=daily-question&envId=2026-01-22

from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        while len(nums) > 1:
            min_pair_start = -1
            is_sorted = True

            for j in range(len(nums)-1):
                if min_pair_start == -1 or nums[j] + nums[j + 1] < nums[min_pair_start] + nums[min_pair_start + 1]:
                    min_pair_start = j

                if is_sorted and nums[j] > nums[j + 1]:
                    is_sorted = False

            if is_sorted:
                return operations

            nums = nums[:min_pair_start] + [nums[min_pair_start] +
                                            nums[min_pair_start+1]] + nums[min_pair_start+2:]
            operations += 1
        return operations


print(Solution().minimumPairRemoval(nums=[5, 2, 3, 1]))
print(Solution().minimumPairRemoval(nums=[1, 2, 2]))
print(Solution().minimumPairRemoval(nums=[2, 1]))
print(Solution().minimumPairRemoval(nums=[-1]))
print(Solution().minimumPairRemoval(nums=[2, 2, -1, 3, -2, 2, 1, 1, 1, 0, -1]))

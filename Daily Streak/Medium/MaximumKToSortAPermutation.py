# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/editorial/?envType=daily-question&envId=2026-10-23

from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            if nums[i] != i:
                ans &= nums[i]
        return 0 if ans == -1 else ans


print(Solution().sortPermutation(nums=[0, 3, 2, 1]))
print(Solution().sortPermutation(nums=[0, 1, 3, 2]))
print(Solution().sortPermutation(nums=[3, 2, 1, 0]))

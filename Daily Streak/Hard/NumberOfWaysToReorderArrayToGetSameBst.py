# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/?envType=daily-question&envId=2026-10-18

from typing import List
from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        def dfs(nums):
            m = len(nums)
            if m < 3:
                return 1
            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % mod

        return (dfs(nums) - 1) % mod


print(Solution().numOfWays(nums=[2, 1, 3]))
print(Solution().numOfWays(nums=[3, 4, 5, 1, 2]))
print(Solution().numOfWays(nums=[1, 2, 3]))

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/description/?envType=daily-question&envId=2026-11-03

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_ele = max(nums)
        return sum(max_ele - num for num in nums)


print(Solution().minMoves(nums=[2, 1, 3]))
print(Solution().minMoves(nums=[4, 4, 5]))

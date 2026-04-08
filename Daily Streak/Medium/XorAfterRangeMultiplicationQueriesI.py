# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/description/?envType=daily-question&envId=2026-04-08

from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for query in queries:
            l, r, k, v = query
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (pow(10, 9) + 7)
                idx += k

        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        return xor


print(Solution().xorAfterQueries(nums=[1, 1, 1], queries=[[0, 2, 1, 4]]))
print(Solution().xorAfterQueries(
    nums=[2, 3, 1, 5, 4], queries=[[1, 4, 2, 3], [0, 2, 1, 2]]))

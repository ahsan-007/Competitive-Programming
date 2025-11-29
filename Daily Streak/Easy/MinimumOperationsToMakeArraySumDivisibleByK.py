# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description /?envType=daily-question&envId=2025-11-29

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) - (k * (sum(nums)//k))


print(Solution().minOperations(nums=[3, 1, 4, 2], k=6))
print(Solution().minOperations(nums=[3, 9, 7], k=5))
print(Solution().minOperations(nums=[4, 1, 3], k=4))
print(Solution().minOperations(nums=[3, 2], k=6))

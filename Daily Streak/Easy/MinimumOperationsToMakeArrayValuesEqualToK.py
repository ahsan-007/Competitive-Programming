# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/?envType=daily-question&envId=2025-04-09

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1

        return len(set(num for num in nums if num > k))


print(Solution().minOperations(nums=[5, 2, 5, 4, 5], k=2))
print(Solution().minOperations(nums=[2, 1, 2], k=2))
print(Solution().minOperations(nums=[9, 7, 5, 3], k=1))

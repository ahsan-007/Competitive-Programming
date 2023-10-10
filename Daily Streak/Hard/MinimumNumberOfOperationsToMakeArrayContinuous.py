# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/?envType=daily-question&envId=2023-10-10

from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans = n
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] < nums[i] + n:
                j = j + 1
            ans = min(ans, n - (j - i))
        return ans


print(Solution().minOperations(nums=[4, 2, 5, 3]))
print(Solution().minOperations(nums=[1, 2, 3, 5, 6]))
print(Solution().minOperations(nums=[1, 10, 100, 1000]))

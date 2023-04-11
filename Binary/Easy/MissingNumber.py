# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    # Bit Manipulation
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for num in range(len(nums)+1):
            total = total ^ num

        for num in nums:
            total = total ^ num
        return total

    def missingNumberV2(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)


print(Solution().missingNumber([0, 1, 3]))
print(Solution().missingNumber([0, 1, 2, 4]))

print(Solution().missingNumberV2([0, 1, 3]))
print(Solution().missingNumberV2([0, 1, 2, 4]))

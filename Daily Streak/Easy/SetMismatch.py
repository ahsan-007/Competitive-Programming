# https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-01-22

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = None
        total_sum = 0

        i = 0
        while i < len(nums):
            if nums[i] in seen:
                duplicate = nums[i]
            else:
                if not duplicate:
                    seen.add(nums[i])
                total_sum = total_sum + nums[i]
            i = i + 1

        return duplicate, ((len(nums) * (len(nums) + 1)) // 2) - total_sum


print(Solution().findErrorNums(nums=[1, 2, 2, 4]))
print(Solution().findErrorNums(nums=[1, 1]))

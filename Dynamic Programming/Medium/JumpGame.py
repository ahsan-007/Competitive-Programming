# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    # Version 2
    def canJumpV2(self, nums):
        max_position = 0
        for i in range(len(nums)):
            if max_position < i:
                return False

            max_position = max(max_position, i + nums[i])

            if max_position >= len(nums) - 1:
                return True
        return True

    # Version 1
    def canJump(self, nums: List[int]) -> bool:
        memo = set()
        return self.canJumpUtil(nums, 0, memo)

    def canJumpUtil(self, nums, i, memo):
        if i in memo:
            return False
        if i >= len(nums) - 1:
            return True
        for j in range(nums[i], 0, -1):
            if self.canJumpUtil(nums, i + j, memo):
                return True
        memo.add(i)
        return False


print(Solution().canJump([2, 3, 1, 1, 4]))
print(Solution().canJump([3, 2, 1, 0, 4]))

print(Solution().canJumpV2([2, 3, 1, 1, 4]))
print(Solution().canJumpV2([3, 2, 1, 0, 4]))

# https://leetcode.com/problems/left-and-right-sum-differences/

from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)
        left_sum = 0
        ans = []
        for i in range(len(nums)):
            ans.append(abs(left_sum - (right_sum - nums[i])))
            left_sum = left_sum + nums[i]
            right_sum = right_sum - nums[i]
        return ans

print(Solution().leftRigthDifference(nums = [10,4,8,3]))
print(Solution().leftRigthDifference(nums = [1]))

# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        ans = []
        for num in nums:
            running_sum = running_sum + num
            ans.append(running_sum)
        return ans


print(Solution().runningSum(nums=[1, 2, 3, 4]))
print(Solution().runningSum(nums=[1, 1, 1, 1, 1]))
print(Solution().runningSum(nums=[3, 1, 2, 10, 1]))

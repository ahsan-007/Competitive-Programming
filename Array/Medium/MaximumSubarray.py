# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum


print(Solution().maxSubArray(nums=[-2, -1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray(nums=[1]))
print(Solution().maxSubArray(nums=[5, 4, -1, 7, 8]))
print(Solution().maxSubArray(
    nums=[31, -41, 59, 26, -53, 58, 97, -93, -23, 84]))

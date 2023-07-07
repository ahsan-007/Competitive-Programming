# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum_size = None
        i = 0
        j = 0
        range_sum = 0
        while j < len(nums):
            range_sum = range_sum + nums[j]
            j = j + 1
            if range_sum >= target:
                while range_sum > target:
                    range_sum = range_sum - nums[i]
                    i = i + 1
                if range_sum != target:
                    i = i - 1
                    range_sum = range_sum + nums[i]
                minimum_size = (
                    j-i) if not minimum_size else min(minimum_size, j - i)
            else:
                while range_sum > target:
                    range_sum = range_sum - nums[i]
                    i = i + 1
        return minimum_size if minimum_size else 0


print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(target=4, nums=[1, 4, 4]))
print(Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

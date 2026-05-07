# https://leetcode.com/problems/jump-game-ix/description/?envType=daily-question&envId=2026-05-07

from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        max_values = [(0, 0)] * len(nums)

        prev = (float("-inf"), -1)
        for i in range(len(nums)):
            if nums[i] > prev[0]:
                prev = (nums[i], i)
            max_values[i] = prev

        def process(r, right_min, right_max):
            p_max, ind = max_values[r]
            curr_max = p_max if p_max <= right_min else right_max

            next_right_min = min(p_max, right_min)
            for i in range(ind, r+1):
                ans[i] = curr_max
                next_right_min = min(next_right_min, nums[i])

            if ind == 0:
                return

            process(ind - 1, next_right_min, curr_max)

        process(len(nums) - 1, float("+inf"), 0)
        return ans


print(Solution().maxValue(nums=[2, 1, 3]))
print(Solution().maxValue(nums=[2, 3, 1]))
print(Solution().maxValue(nums=[30, 21, 5, 35, 24]))

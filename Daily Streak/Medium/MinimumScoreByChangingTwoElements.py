# https://leetcode.com/problems/minimum-score-by-changing-two-elements/description/?envType=daily-question&envId=2026-11-19

from typing import List

class Solution:
    # Time: O(NLog(N))
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        low_score = float("+inf")
        for i in range(1, len(nums)):
            low_score = min(low_score, nums[i] - nums[i-1])

        return min (
            (nums[-3] - nums[0]),
            (nums[-1] - nums[2]),
            nums[-2] - nums[1]
        )

    def minimizeSumV2(self, nums: List[int]) -> int:
        minimums = [float("+inf")] * 3
        maximums = [float("-inf")] * 3
        for num in nums:
            if num < minimums[0]:
                minimums = [num, minimums[0], minimums[1]]
            elif num < minimums[1]:
                minimums[1], minimums[2] = num, minimums[1]
            elif num < minimums[2]:
                minimums[2] = num

            if num > maximums[2]:
                maximums = [maximums[1], maximums[2], num]
            elif num > maximums[1]:
                maximums[0], maximums[1] = maximums[1], num
            elif num > maximums[0]:
                maximums[0] = num

        return min(
            maximums[0] - minimums[0],
            maximums[2] - minimums[2],
            maximums[1] - minimums[1]
        )

print(Solution().minimizeSum(nums = [1,4,7,8,5]))
print(Solution().minimizeSum(nums = [1,4,3]))
print(Solution().minimizeSum(nums = [59,27,9,81,33]))
print(Solution().minimizeSum(nums = [58,42,8,75,28]))

print(Solution().minimizeSumV2(nums = [1,4,7,8,5]))
print(Solution().minimizeSumV2(nums = [1,4,3]))
print(Solution().minimizeSumV2(nums = [59,27,9,81,33]))
print(Solution().minimizeSumV2(nums = [58,42,8,75,28]))
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/?envType=daily-question&envId=2026-02-01

from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        firsMin = float("+inf")
        secondMin = float("+inf")
        for i in range(1, len(nums)):
            if nums[i] < firsMin:
                secondMin = firsMin
                firsMin = nums[i]
            elif nums[i] < secondMin:
                secondMin = nums[i]
        return nums[0] + firsMin + secondMin


print(Solution().minimumCost(nums=[1, 2, 3, 12]))
print(Solution().minimumCost(nums=[5, 4, 3]))
print(Solution().minimumCost(nums=[10, 3, 1, 1]))

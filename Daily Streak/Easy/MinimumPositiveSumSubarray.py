# https://leetcode.com/problems/minimum-positive-sum-subarray/description/?envType=daily-question&envId=2026-11-14

from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float("+inf")
        for i in range(len(nums)):
            j = i + l
            if j > len(nums):
                return min_sum if min_sum != float("+inf") else -1

            curr_sum = sum(nums[i:j])
            if curr_sum > 0:
                min_sum = min(min_sum, curr_sum)
            while (j - i) <= r and j < len(nums):
                curr_sum += nums[j]
                if curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)
                j = j + 1
        return min_sum if min_sum != float("+inf") else -1


print(Solution().minimumSumSubarray(nums=[3, -2, 1, 4], l=2, r=3))
print(Solution().minimumSumSubarray(nums=[-2, 2, -3, 1], l=2, r=3))
print(Solution().minimumSumSubarray(nums=[1, 2, 3, 4], l=2, r=4))
print(Solution().minimumSumSubarray(nums=[-3, 17], l=1, r=2))

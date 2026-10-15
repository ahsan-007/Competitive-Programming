# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/?envType=daily-question&envId=2026-10-15

from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum_of_squares = 0
        for i in range(len(nums)):
            elements = set()
            curr_sum = 0
            for j in range(i, len(nums)):
                if nums[j] not in elements:
                    elements.add(nums[j])
                curr_sum += len(elements) ** 2
            sum_of_squares += curr_sum
        return sum_of_squares


print(Solution().sumCounts(nums=[1, 2, 1]))
print(Solution().sumCounts(nums=[1, 1]))

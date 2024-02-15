# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/?envType=daily-question&envId=2024-02-15

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_of_elements = sum(nums)
        i = len(nums) - 1
        while i >= 0 and sum_of_elements - nums[i] <= nums[i]:
            sum_of_elements = sum_of_elements - nums[i]
            i = i - 1
        return sum_of_elements if sum_of_elements else -1


print(Solution().largestPerimeter(nums=[5, 5, 5]))
print(Solution().largestPerimeter(nums=[1, 12, 1, 2, 5, 50, 3]))
print(Solution().largestPerimeter(nums=[5, 5, 50]))

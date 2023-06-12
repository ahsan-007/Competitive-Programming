# https://leetcode.com/problems/summary-ranges/

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        start = end = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] - end > 1:
                ranges.append(f"{start}->{end}" if start !=
                              end else f"{start}")
                start = end = nums[i]
            else:
                end = nums[i]
            i = i + 1
        ranges.append(f"{start}->{end}" if start !=
                      end else f"{start}")
        return ranges


print(Solution().summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
print(Solution().summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))

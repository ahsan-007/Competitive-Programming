# https://leetcode.com/problems/container-with-most-water/description/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            area = max(area, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return area


print(Solution().maxArea([1, 8, 6, 2, 5, 9, 8, 3, 7]))
print(Solution().maxArea([1, 1]))
print(Solution().maxArea([4, 3, 2, 1, 4]))
print(Solution().maxArea([1, 2, 1]))

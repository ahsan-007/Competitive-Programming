# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        def trapUtil(height, i, j, lim, is_forward_direction):
            sum_of_heights = height[i]
            water = 0
            while (is_forward_direction and j <= lim) or (not is_forward_direction and j >= lim):
                if height[j] >= height[i]:
                    water = water + ((height[i] * abs(j-i)) - sum_of_heights)
                    i = j
                    sum_of_heights = height[i]
                else:
                    sum_of_heights = sum_of_heights + height[j]
                j = j + (1 if is_forward_direction else -1)

            if not is_forward_direction:
                return water

            return water + trapUtil(height, len(height) - 1, len(height) - 2, i, False)

        return trapUtil(height, 0, 1, len(height)-1, True)


print(Solution().trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap(height=[4, 2, 0, 3, 2, 5]))
print(Solution().trap(height=[4, 2, 3]))

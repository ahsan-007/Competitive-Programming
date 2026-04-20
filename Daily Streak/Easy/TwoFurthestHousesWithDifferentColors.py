# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/?envType=daily-question&envId=2026-04-20

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance = -1
        for i in range(len(colors)):
            j = len(colors) - 1
            if j - i < max_distance:
                return max_distance

            while j > i:
                if colors[j] != colors[i]:
                    max_distance = max(max_distance, j - i)
                j = j - 1
        return max_distance


print(Solution().maxDistance(colors=[1, 1, 1, 6, 1, 1, 1]))
print(Solution().maxDistance(colors=[1, 8, 3, 8, 3]))
print(Solution().maxDistance(colors=[0, 1]))

# https://leetcode.com/problems/apple-redistribution-into-boxes/description/?envType=daily-question&envId=2025-12-24

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        applesCount = sum(apple)
        i = 0
        while applesCount > 0 and i < len(capacity):
            applesCount = applesCount - capacity[i]
            i = i + 1
        return i


print(Solution().minimumBoxes(apple=[1, 3, 2], capacity=[4, 3, 1, 5, 2]))
print(Solution().minimumBoxes(apple=[5, 5, 5], capacity=[2, 4, 2, 7]))

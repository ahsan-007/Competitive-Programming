# https://leetcode.com/problems/valid-perfect-square/description/

import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return math.pow(int(math.sqrt(num)), 2) == num


print(Solution().isPerfectSquare(16))
print(Solution().isPerfectSquare(14))
print(Solution().isPerfectSquare(81))
print(Solution().isPerfectSquare(80))

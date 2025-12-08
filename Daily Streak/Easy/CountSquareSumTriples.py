# https://leetcode.com/problems/count-square-sum-triples/description /?envType=daily-question&envId=2025-12-08

import math


class Solution:
    # a**2 + b** 2 = c**2
    # a**2         = c**2 - b**2
    # a            = +- sqrt(c**2 - b**2)
    def countTriples(self, n: int) -> int:
        count = 0
        for c in range(1, n+1):
            for b in range(1, c):
                a = math.sqrt(c**2 - b**2)
                if int(a) == a:
                    count += 1
        return count


print(Solution().countTriples(n=5))
print(Solution().countTriples(n=10))

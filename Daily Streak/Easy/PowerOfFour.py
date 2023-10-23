# https://leetcode.com/problems/power-of-four/?envType=daily-question&envId=2023-10-23

import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n <= 0 else math.log(n, 4) == int(math.log(n, 4))


print(Solution().isPowerOfFour(16))
print(Solution().isPowerOfFour(20))
print(Solution().isPowerOfFour(-16))

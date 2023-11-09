# https://leetcode.com/problems/count-number-of-homogenous-substrings/description/?envType=daily-question&envId=2023-11-09

import math


class Solution:
    def countHomogenous(self, s: str) -> int:
        i = 0
        j = 0
        count = 0
        while i < len(s):
            if j < len(s) and s[j] == s[i]:
                j = j + 1
            else:
                count = count + ((j-i) * (j - i + 1)) // 2
                i = j
        return count % 100000009


print(Solution().countHomogenous("abbcccaa"))
print(Solution().countHomogenous("xy"))
print(Solution().countHomogenous("zzzzz"))

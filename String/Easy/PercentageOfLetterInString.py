# https://leetcode.com/problems/percentage-of-letter-in-string/

import math


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return math.floor((s.count(letter) / len(s)) * 100)


print(Solution().percentageLetter(s="foobar", letter="o"))
print(Solution().percentageLetter(s="jjjj", letter="k"))

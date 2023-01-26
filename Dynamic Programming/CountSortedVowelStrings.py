# https://leetcode.com/problems/count-sorted-vowel-strings/
import math


class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n <= 0:
            return 0
        count = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        while (n > 1):
            count["a"] = sum(v for k, v in count.items() if ord(k) >= ord('a'))
            count["e"] = sum(v for k, v in count.items() if ord(k) >= ord('e'))
            count["i"] = sum(v for k, v in count.items() if ord(k) >= ord('i'))
            count["o"] = sum(v for k, v in count.items() if ord(k) >= ord('o'))
            count["u"] = sum(v for k, v in count.items() if ord(k) >= ord('u'))
            n = n - 1
        return sum(v for v in count.values())

    # one liner solution
    def countVowelStringsOneLiner(self, n: int) -> int:
        return math.com(n+4, 4)


print(Solution().countVowelStrings(33))

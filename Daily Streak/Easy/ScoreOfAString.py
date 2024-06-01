# https://leetcode.com/problems/score-of-a-string/description /?envType=daily-question&envId=2024-06-01

from itertools import pairwise


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) - 1))

    def scoreOfStringV2(self, s: str) -> int:
        return sum(abs(ord(a) - ord(b)) for a, b in pairwise(s))


print(Solution().scoreOfString("hello"))
print(Solution().scoreOfString("zaz"))


print(Solution().scoreOfStringV2("hello"))
print(Solution().scoreOfStringV2("zaz"))

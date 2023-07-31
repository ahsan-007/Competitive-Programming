# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

import random


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        return self.minimumDeleteSumUtil(s1, s2, memo)

    def minimumDeleteSumUtil(self, s1, s2, memo):
        if len(s1) == 0 and len(s2) == 0:
            return 0
        if (s1, s2) not in memo:
            if len(s1) == 0 or len(s2) == 0:
                memo[(s1, s2)] = (self.minimumDeleteSumUtil(s1, s2[1:], memo) + ord(s2[0])) if len(s1) == 0 else (self.minimumDeleteSumUtil(
                    s1[1:], s2, memo) + ord(s1[0]))
            else:
                memo[(s1, s2)] = min(self.minimumDeleteSumUtil(s1[1:], s2, memo) + ord(s1[0]),
                                     self.minimumDeleteSumUtil(s1, s2[1:], memo) + ord(s2[0])) if s1[0] != s2[0] else self.minimumDeleteSumUtil(
                    s1[1:], s2[1:], memo)
        return memo[(s1, s2)]


print(Solution().minimumDeleteSum(s1="sea", s2="eat"))
print(Solution().minimumDeleteSum(s1="delete", s2="leet"))

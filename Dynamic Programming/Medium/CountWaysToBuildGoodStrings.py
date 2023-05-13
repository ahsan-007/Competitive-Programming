# https://leetcode.com/problems/count-ways-to-build-good-strings/

import math


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        count = 0
        memo = {0: 1}
        for i in range(low, high+1):
            count = count + self.countGoodStringsUtil(i, zero, one, memo)
        return count % (1000000000 + 7)
        # return self.countGoodStringsUtil(low, high, zero, one, 0, {})

    def countGoodStringsUtil(self, length, zero, one, memo):
        if length in memo:
            return memo[length]
        count = 0
        if length >= zero:
            count = count + \
                self.countGoodStringsUtil(length - zero, zero, one, memo)
        if length >= one:
            count = count + \
                self.countGoodStringsUtil(length - one, zero, one, memo)
        memo[length] = count
        return memo[length]

    # def countGoodStringsUtil(self, low, high, zero, one, current_length, memo):
    #     if current_length > high:
    #         return 0

    #     if current_length not in memo:
    #         count = self.countGoodStringsUtil(low, high, zero, one, current_length + zero, memo) + \
    #             self.countGoodStringsUtil(
    #                 low, high, zero, one, current_length + one, memo)
    #         memo[current_length] = count + \
    #             1 if low <= current_length <= high else count

    #     return memo[current_length]


print(Solution().countGoodStrings(low=3, high=3, zero=1, one=1))
print(Solution().countGoodStrings(low=2, high=3, zero=1, one=2))
print(Solution().countGoodStrings(low=1, high=100000, zero=1, one=1))

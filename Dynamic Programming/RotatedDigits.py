# https://leetcode.com/problems/rotated-digits

# Optimised Version
class Solution:
    def rotatedDigits(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 5, 3: None, 4: None,
                5: 2, 6: 9, 7: None, 8: 8, 9: 6}
        good_numbers = 0
        for i in range(n+1):
            converted_num = self.convertNumber(i, memo)
            if converted_num is not None and i != self.convertNumber(i, memo):
                good_numbers = good_numbers + 1
        return good_numbers

    def convertNumber(self, n, memo):
        if n in memo:
            return memo[n]
        dig = n % 10
        if memo[dig] is None:
            memo[n] = None
            return memo[n]
        converted_num = self.convertNumber(n//10, memo)
        if converted_num is None:
            memo[n] = None
            return memo[n]
        memo[n] = converted_num * 10 + memo[dig]
        return memo[n]


class SolutionV1:
    def rotatedDigits(self, n: int) -> int:
        mapping = {0: 0, 1: 1, 2: 5, 3: None, 4: None,
                   5: 2, 6: 9, 7: None, 8: 8, 9: 6}
        memo = {}
        good_numbers = 0
        for i in range(n+1):
            if self.isGoodNumber(i, mapping, memo):
                good_numbers = good_numbers + 1
        return good_numbers

    def isGoodNumber(self, n, mapping, memo):
        # if n in memo:
        #     return memo[n]
        new_num = 0
        n_copy = n
        t = 1
        while n_copy:
            dig = n_copy % 10
            if mapping[dig] is None:
                memo[n] = False
                return memo[n]
            new_num = mapping[dig] * t + new_num
            t = t * 10
            n_copy = n_copy // 10
        return n != new_num
        #memo[n] = n != new_num
        # return memo[n]


print(Solution().rotatedDigits(10000))

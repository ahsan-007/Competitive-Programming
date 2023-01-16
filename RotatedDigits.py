# https://leetcode.com/problems/rotated-digits

class Solution:
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

# mapping = {0: 0, 1: 1, 2: 5, 3: None, 4: None,
#             5: 2, 6: 9, 7: None, 8: 8, 9: 6}
# memo = {}
# for i in range(0, 11):
#     if Solution().isGoodNumber(i, mapping, memo):
#         print(i)

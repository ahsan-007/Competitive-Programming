# https://leetcode.com/problems/powx-n/description/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPowUtil(x, -n)
        else:
            return self.myPowUtil(x, n)

    def myPowUtil(self, x, n):
        if n == 0:
            return 1
        pow = x
        exp = 1
        while exp * 2 <= n:
            pow = pow * pow
            exp = exp * 2
        return pow * self.myPowUtil(x, n-exp)


print(Solution().myPow(2, 10))
print(Solution().myPow(2, 3))
print(Solution().myPow(3, 2))
print(Solution().myPow(3, -2))

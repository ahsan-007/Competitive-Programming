# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sumDifference = 0
        for i in range(1, n + 1):
            sumDifference = sumDifference + (-i if i % m == 0 else i)
        return sumDifference


print(Solution().differenceOfSums(n=10, m=3))
print(Solution().differenceOfSums(n=5, m=6))
print(Solution().differenceOfSums(n=5, m=1))

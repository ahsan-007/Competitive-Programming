# https://leetcode.com/problems/four-divisors/description/?envType=daily-question&envId=2026-01-04

from typing import List
import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def getDivisors(num):
            divisors = []
            divisor = 1
            while divisor <= math.sqrt(num):
                if num % divisor == 0:
                    divisors.append(divisor)
                    if divisor != num // divisor:
                        divisors.append(num//divisor)
                divisor += 1

            return list(set(divisors))

        divisorsSum = 0
        for num in nums:
            divisors = getDivisors(num)
            if len(divisors) == 4:
                divisorsSum += sum(divisors)
        return divisorsSum


print(Solution().sumFourDivisors(nums=[21, 4, 7]))
print(Solution().sumFourDivisors(nums=[21, 21]))
print(Solution().sumFourDivisors(nums=[1, 2, 3, 4, 5]))

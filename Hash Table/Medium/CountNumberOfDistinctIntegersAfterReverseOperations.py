# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct_integers = {}
        for num in nums:
            if num not in distinct_integers:
                distinct_integers[num] = True
            reversed_num = Solution.reverse_digits(num)
            if reversed_num not in distinct_integers:
                distinct_integers[reversed_num] = True
        return len(distinct_integers.keys())

    def reverse_digits(num):
        reversed_num = 0
        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num = num // 10
        return reversed_num


print(Solution().countDistinctIntegers([1, 13, 10, 12, 31]))
print(Solution().countDistinctIntegers([2, 2, 2]))

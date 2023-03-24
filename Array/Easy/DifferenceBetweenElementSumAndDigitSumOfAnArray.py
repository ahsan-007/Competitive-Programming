# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = elementSum = 0
        for num in nums:
            elementSum = elementSum + num
            digit_sum = digit_sum + Solution.getDigitSum(num)
        return abs(elementSum - digit_sum)

    def getDigitSum(num):
        sum = 0
        while num > 0:
            sum = sum + num % 10
            num = num // 10
        return sum

print(Solution().differenceOfSum(nums = [1,15,6,3]))
print(Solution().differenceOfSum(nums = [1,2,3,4]))

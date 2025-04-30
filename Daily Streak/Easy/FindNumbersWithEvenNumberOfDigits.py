# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=daily-question&envId=2025-04-30


from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def getDigitCount(num):
            count = 0
            while num:
                count = count + 1
                num = num // 10
            return count

        return sum(1 if getDigitCount(num) % 2 == 0 else 0 for num in nums)


print(Solution().findNumbers(nums=[12, 345, 2, 6, 7896]))
print(Solution().findNumbers(nums=[555, 901, 482, 1771]))

# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        digit_sum = 0
        while num:
            digit_sum = digit_sum + num % 10
            num = num // 10
        return self.addDigits(digit_sum)


print(Solution().addDigits(38))
print(Solution().addDigits(0))

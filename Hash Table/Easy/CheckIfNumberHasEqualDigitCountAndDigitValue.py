# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution:
    def digitCount(self, num: str) -> bool:
        numbers = {}
        for dig in num:
            numbers[int(dig)] = numbers.get(int(dig), 0) + 1

        for i in range(len(num)):
            if (num[i] == '0' and i in numbers) or (num[i] != '0' and (i not in numbers or int(num[i]) != numbers[i])):
                return False
        return True


print(Solution().digitCount("1210"))
print(Solution().digitCount("030"))

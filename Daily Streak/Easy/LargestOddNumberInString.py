# https://leetcode.com/problems/largest-odd-number-in-string/description/?envType=daily-question&envId=2023-12-07
class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while i >= 0:
            if int(num[i]) % 2 == 1:
                return num[:i+1]
            i = i - 1

        return ""


print(Solution().largestOddNumber(num="52"))
print(Solution().largestOddNumber(num="4206"))
print(Solution().largestOddNumber(num="35427"))

# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/?envType=daily-question&envId=2023-12-04

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        max_int = float("-inf")
        while i < len(num) - 2:
            if num[i] == num[i+1] and num[i] == num[i+2]:
                max_int = max(max_int, int(num[i]))
            i = i + 1
        return str(max_int) * 3 if max_int != float("-inf") else ""


print(Solution().largestGoodInteger(num="6777133339"))
print(Solution().largestGoodInteger(num="2300019"))
print(Solution().largestGoodInteger(num="42352338"))

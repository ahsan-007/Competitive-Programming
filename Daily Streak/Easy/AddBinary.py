# https://leetcode.com/problems/add-binary/description/?envType=daily-question&envId=2026-02-15

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binarySum = ""
        carry = 0
        for i in range(1, max(len(a), len(b)) + 1):
            currSum = int(a[-i] if i <= len(a) else 0) + \
                int(b[-i] if i <= len(b) else 0) + carry

            carry = currSum // 2
            currSum = currSum % 2

            binarySum = str(currSum) + binarySum

        if carry:
            binarySum = str(carry) + binarySum

        return binarySum


print(Solution().addBinary(a="11", b="1"))
print(Solution().addBinary(a="1010", b="1011"))

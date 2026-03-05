# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2026-03-05

class Solution:
    def minOperations(self, s: str) -> int:
        operationsWithFirstBitFlip = 0
        operationsWithoutFirstBitFlip = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != s[0]:
                    operationsWithoutFirstBitFlip += 1
                else:
                    operationsWithFirstBitFlip += 1

            else:
                if s[i] == s[0]:
                    operationsWithoutFirstBitFlip += 1
                else:
                    operationsWithFirstBitFlip += 1
        return min(operationsWithFirstBitFlip, operationsWithoutFirstBitFlip)

    def minOperationsV2(self, s: str) -> int:
        flips = 0
        for i in range(len(s)):
            if (i % 2 == 0 and s[i] != s[0]) or (i % 2 == 1 and s[i] == s[0]):
                flips += 1
        return min(flips, len(s) - flips)


print(Solution().minOperations(s="0100"))
print(Solution().minOperations(s="10"))
print(Solution().minOperations(s="1111"))
print(Solution().minOperations(s="0010"))

print('-'*100)

print(Solution().minOperationsV2(s="0100"))
print(Solution().minOperationsV2(s="10"))
print(Solution().minOperationsV2(s="1111"))
print(Solution().minOperationsV2(s="0010"))

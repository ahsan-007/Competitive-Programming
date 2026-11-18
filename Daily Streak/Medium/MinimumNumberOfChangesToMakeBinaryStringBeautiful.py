# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/?envType=daily-question&envId=2026-11-18

class Solution:
    def minChanges(self, s: str) -> int:
        ones = zeroes = count = i = 0
        while i < len(s) - 1:
            if s[i] == '0':
                zeroes += 1
            else:
                ones += 1

            if s[i + 1] == '0':
                zeroes += 1
            else:
                ones += 1

            if ones > zeroes:
                count += zeroes
                ones = zeroes = 0
            elif zeroes > ones:
                count += ones
                ones = zeroes = 0

            i = i + 2

        return count + min(ones, zeroes)

    def minChangesV2(self, s: str) -> int:
        ones = zeroes = count = i = 0
        while i < len(s):
            if s[i] == '0':
                zeroes += 1
            else:
                ones += 1

            if i % 2 == 1 and zeroes != ones:
                if zeroes > ones:
                    count += ones
                else:
                    count += zeroes
                zeroes = ones = 0

            i = i + 1
        return count + min(zeroes, ones)


print(Solution().minChanges(s="1001"))
print(Solution().minChanges(s="10"))
print(Solution().minChanges(s="0000"))

print(Solution().minChangesV2(s="1001"))
print(Solution().minChangesV2(s="10"))
print(Solution().minChangesV2(s="0000"))

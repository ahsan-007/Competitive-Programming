# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/?envType=daily-question&envId=2026-10-09

class Solution:
    def minInsertions(self, s: str) -> int:
        min_insertions = 0
        opening_brackets = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                opening_brackets += 1
            else:
                if i + 1 == len(s) or s[i + 1] != ')':
                    min_insertions += 1
                else:
                    i = i + 1

                if opening_brackets > 0:
                    opening_brackets -= 1
                else:
                    min_insertions += 1
            i = i + 1

        return min_insertions + opening_brackets * 2


print(Solution().minInsertions(s="(()))"))
print(Solution().minInsertions(s="())"))
print(Solution().minInsertions(s="))())("))

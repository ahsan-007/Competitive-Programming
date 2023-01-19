# https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count = count + \
                self.countSubstringsUtil(s, i, i) + \
                self.countSubstringsUtil(s, i-1, i)
        return count

    def countSubstringsUtil(self, s, i, j):
        count = 0
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                count = count + 1
            else:
                return count
            i = i - 1
            j = j + 1
        return count


print(Solution().countSubstrings('abcba'))

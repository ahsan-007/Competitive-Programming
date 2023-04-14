# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        for i in range(len(s)):
            palindrome1 = self.longestPalindromUtil(s, i, i+1)
            palindrome2 = self.longestPalindromUtil(s, i-1, i+1)
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1 if len(
                    palindrome1) > len(palindrome2) else palindrome2
            elif len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2
        return longest_palindrome

    def longestPalindromUtil(self, s, i, j):
        length = 0
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                return s[i+1:j]
            length = length + 2
            i = i - 1
            j = j + 1
        return s[i+1:j]


print(Solution().longestPalindrome('babad'))
print(Solution().longestPalindrome('bbaabbccdd'))

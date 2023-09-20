# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        for i in range(len(s)):
            palindrome = self.longestPalindromeUtil(s, i-1, i+1)
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome

            palindrome = self.longestPalindromeUtil(s, i-1, i)
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome

        return longest_palindrome

    def longestPalindromeUtil(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i = i - 1
            j = j + 1

        return s[i+1:j]


print(Solution().longestPalindrome(s="babad"))
print(Solution().longestPalindrome(s="cbbd"))

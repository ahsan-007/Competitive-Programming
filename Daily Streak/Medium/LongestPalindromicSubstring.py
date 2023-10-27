# https://leetcode.com/problems/longest-palindromic-substring/description/?envType=daily-question&envId=2023-10-27


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longestPalindromeUtil(s, i, j):
            currLongestPalindrome = ""
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    currLongestPalindrome = s[i:j+1]
                else:
                    return currLongestPalindrome
                i = i - 1
                j = j + 1
            return currLongestPalindrome

        currLongestPalindrome = ""
        for i in range(len(s)):
            palindrome = longestPalindromeUtil(s, i, i)
            if len(palindrome) > len(currLongestPalindrome):
                currLongestPalindrome = palindrome

            palindrome = longestPalindromeUtil(s, i - 1, i)
            if len(palindrome) > len(currLongestPalindrome):
                currLongestPalindrome = palindrome
        return currLongestPalindrome


print(Solution().longestPalindrome(s="babad"))
print(Solution().longestPalindrome(s="cbbd"))

# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/?envType=daily-question&envId=2024-02-13

from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s, i, j):
            if i >= j:
                return True

            return s[i] == s[j] and isPalindrome(s, i + 1, j - 1)

        for word in words:
            if isPalindrome(word, 0, len(word)-1):
                return word

        return ""


print(Solution().firstPalindrome(
    words=["abc", "car", "ada", "racecar", "cool"]))
print(Solution().firstPalindrome(
    words=["notapalindrome", "racecar"]))
print(Solution().firstPalindrome(
    words=["def", "ghi"]))

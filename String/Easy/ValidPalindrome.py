# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if self.isAlphanumeric(s[l]) and self.isAlphanumeric(s[r]):
                if s[l].lower() != s[r].lower():
                    return False
                l = l + 1
                r = r - 1
            elif not self.isAlphanumeric(s[l]):
                l = l + 1
            else:
                r = r - 1
        return True

    def isAlphanumeric(self, ch):
        return ord(ch.lower()) >= ord('a') and ord(ch.lower()) <= ord('z') or ord(ch) >= ord('0') and ord(ch) <= ord('9')


print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(s=" "))

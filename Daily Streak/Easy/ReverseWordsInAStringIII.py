# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/?envType=daily-question&envId=2023-10-01

class Solution:
    def reverseWords(self, s: str) -> str:
        i = j = 0
        while j <= len(s):
            if j == len(s) or s[j] == ' ':
                s = s[:i] + s[i:j][::-1] + s[j:]
                i = j + 1
            j = j + 1
        return s


print(Solution().reverseWords(s="Let's take LeetCode contest"))
print(Solution().reverseWords(s="God Ding"))

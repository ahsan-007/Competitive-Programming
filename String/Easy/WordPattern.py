# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        chToWord = {}
        wordToCh = {}
        j = 0
        for i in range(len(pattern)):
            if j >= len(s):
                return False

            startInd = j
            while j < len(s) and s[j] != " ":
                j = j + 1
            word = s[startInd:j]
            j = j + 1

            if pattern[i] not in chToWord and word not in wordToCh:
                chToWord[pattern[i]] = word
                wordToCh[word] = pattern[i]

            elif chToWord.get(pattern[i], '') != word or wordToCh.get(word, '') != pattern[i]:
                return False

        return True if j >= len(s) else False


print(Solution().wordPattern(pattern="abba", s="dog cat cat dog"))
print(Solution().wordPattern(pattern="abba", s="dog cat cat fish"))
print(Solution().wordPattern(pattern="aaaa", s="dog cat cat dog"))
print(Solution().wordPattern(pattern="abab", s="dog dog dog dog"))

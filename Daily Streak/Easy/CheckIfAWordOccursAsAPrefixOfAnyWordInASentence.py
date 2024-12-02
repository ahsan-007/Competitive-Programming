# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description /?envType=daily-question&envId=2024-12-02

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        currentWordIndex = 1
        i = 0
        j = 0
        startSearch = True
        while i < len(sentence):
            if sentence[i] == ' ':
                currentWordIndex = currentWordIndex + 1
                startSearch = True
                if j != 0:
                    j = 0
            elif startSearch and sentence[i] == searchWord[j]:
                j = j + 1
                if j == len(searchWord):
                    return currentWordIndex
            else:
                if startSearch:
                    startSearch = False
                if j != 0:
                    j = 0
            i = i + 1
        return -1


print(Solution().isPrefixOfWord(sentence="i love eating burger", searchWord="burg"))
print(Solution().isPrefixOfWord(
    sentence="this problem is an easy problem", searchWord="pro"))
print(Solution().isPrefixOfWord(sentence="i am tired", searchWord="you"))
print(Solution().isPrefixOfWord(
    sentence="hellohello hellohellohello", searchWord="ell"))
print(Solution().isPrefixOfWord(sentence="b bu bur burg burger", searchWord="burg"))

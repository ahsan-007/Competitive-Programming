# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        return self.maxScoreWordsUtil(words, Counter(letters), score, 0)

    def maxScoreWordsUtil(self, words, letters, score, i):
        if i >= len(words):
            return 0
        j = 0
        letters_found = True
        included_score = 0
        while j < len(words[i]) and letters_found:
            if letters.get(words[i][j], 0) > 0:
                letters[words[i][j]] = letters[words[i][j]] - 1
                included_score = included_score + \
                    score[ord(words[i][j]) - ord('a')]
            else:
                letters_found = False
            j = j + 1

        if letters_found:
            included_score = included_score + \
                self.maxScoreWordsUtil(words, letters, score, i+1)
            j = j - 1
        else:
            included_score = 0
            j = j - 2

        while j >= 0:
            letters[words[i][j]] += 1
            j = j - 1
        return max(included_score, self.maxScoreWordsUtil(words, letters, score, i + 1))


# Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
print(Solution().maxScoreWords(words=["dog", "cat", "dad", "good"], letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"], score=[
      1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

print(Solution().maxScoreWords(words=["xxxz", "ax", "bx", "cx"], letters=["z", "a", "b", "c", "x", "x", "x"], score=[
      4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]))

# Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# Output: 27
print(Solution().maxScoreWords(words=["leetcode"], letters=["l", "e", "t", "c", "o", "d"], score=[
      0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]))

# Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# Output: 0

print(Solution().maxScoreWords(words=["dog", "cat", "dad", "good", "doom", "dime", "lime", "wifi", "glass", "eccentric", "nervous", "ego", "selfcentered", "hunter"], letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"] + [chr(ord('a') + i) for i in range(0, 26)]*10, score=[
      1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

# https://leetcode.com/problems/find-and-replace-pattern/


from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        mapped_words = []
        for word in words:
            if len(word) == len(pattern):
                mapped_word_characters = {}
                mapped_pattern_characters = {}
                i = 0
                invalid = False
                while i < len(word) and not invalid:
                    if word[i] not in mapped_word_characters:
                        if pattern[i] not in mapped_pattern_characters:
                            mapped_word_characters[word[i]] = pattern[i]
                            mapped_pattern_characters[pattern[i]] = pattern[i]
                        else:
                            invalid = True
                    else:
                        if pattern[i] not in mapped_pattern_characters or mapped_word_characters[word[i]] != pattern[i]:
                            invalid = True
                    i = i + 1
                if not invalid:
                    mapped_words.append(word)
        return mapped_words


print(Solution().findAndReplacePattern(
    words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"))
print(Solution().findAndReplacePattern(words=["a", "b", "c"], pattern="a"))

# https://leetcode.com/problems/keyboard-row//

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Dictionary
        first_row = {ch: True for ch in "qwertyuiop"}
        second_row = {ch: True for ch in "asdfghjkl"}
        third_row = {ch: True for ch in "zxcvbnm"}

        short_listed_words = []
        for word in words:
            if word[0].lower() in first_row:
                row = first_row
            elif word[0].lower() in second_row:
                row = second_row
            else:
                row = third_row

            i = 1
            short_listed = True
            while i < len(word) and short_listed:
                if word[i].lower() not in row:
                    short_listed = False
                i = i + 1
            if short_listed:
                short_listed_words.append(word)
        return short_listed_words

    def findWordsV2(self, words: List[str]) -> List[str]:
        # Set
        first_row = {ch for ch in "qwertyuiop"}
        second_row = {ch for ch in "asdfghjkl"}
        third_row = {ch for ch in "zxcvbnm"}

        short_listed_words = []
        for word in words:
            if word[0].lower() in first_row:
                row = first_row
            elif word[0].lower() in second_row:
                row = second_row
            else:
                row = third_row

            i = 1
            short_listed = True
            while i < len(word) and short_listed:
                if word[i].lower() not in row:
                    short_listed = False
                i = i + 1
            if short_listed:
                short_listed_words.append(word)
        return short_listed_words


print(Solution().findWords(words=["Hello", "Alaska", "Dad", "Peace"]))
print(Solution().findWords(words=["omk"]))
print(Solution().findWords(words=["adsdf", "sfd"]))

print(Solution().findWordsV2(words=["Hello", "Alaska", "Dad", "Peace"]))
print(Solution().findWordsV2(words=["omk"]))
print(Solution().findWordsV2(words=["adsdf", "sfd"]))

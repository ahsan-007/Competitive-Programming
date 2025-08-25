# https://leetcode.com/problems/verifying-an-alien-dictionary/description/

from typing import List


class Solution:
    # Space: O(1)
    # Time: O(MN),
    # M = No. of words, N = No. of characters in a word
    # or
    # Time: O(M), where M is total number of characters in all words
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ranking = {ch: i for i, ch in enumerate(order)}
        for i in range(1, len(words)):
            j = 0
            minWordLength = min(len(words[i-1]), len(words[i]))
            while j < minWordLength and ranking[words[i-1][j]] >= ranking[words[i][j]]:
                if ranking[words[i-1][j]] > ranking[words[i][j]]:
                    return False

                if j == minWordLength - 1 and len(words[i-1]) > len(words[i]):
                    return False

                j = j + 1

        return True


print(Solution().isAlienSorted(
    words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
print(Solution().isAlienSorted(
    words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))
print(Solution().isAlienSorted(
    words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))

# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ''
        i = 0
        while i < len(word1) and i < len(word2):
            merged_string = merged_string + word1[i] + word2[i]
            i = i + 1

        if i != len(word1):
            merged_string = merged_string + word1[i:]
        elif i != len(word2):
            merged_string = merged_string + word2[i:]

        return merged_string


print(Solution().mergeAlternately(word1="abc", word2="pqr"))
print(Solution().mergeAlternately(word1="ab", word2="pqrs"))
print(Solution().mergeAlternately(word1="abcd", word2="pq"))

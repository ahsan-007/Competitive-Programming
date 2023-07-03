# https://leetcode.com/problems/buddy-strings/

from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        i = j = -1
        for letter in range(len(s)):
            if s[letter] != goal[letter]:
                if i == -1:
                    i = letter
                elif j == -1:
                    j = letter
                else:
                    return False
        return True if (s == goal and self.contains_duplicate_letters(s)) or (i != -1 and j != -1 and s[j] == goal[i] and s[i] == goal[j]) else False

    def contains_duplicate_letters(self, s):
        frequency = Counter(s)
        for character in frequency:
            if frequency[character] > 1:
                return True
        return False


print(Solution().buddyStrings(s="ab", goal="ba"))
print(Solution().buddyStrings(s="ab", goal="ab"))
print(Solution().buddyStrings(s="abab", goal="abab"))
print(Solution().buddyStrings(s="aa", goal="aa"))
print(Solution().buddyStrings(s="ab", goal="babbb"))

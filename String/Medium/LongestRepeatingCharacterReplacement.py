# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        for i in range(26):
            max_length = max(
                max_length, self.findMaxLength(s, k, chr(ord('A')+i)))
        return max_length

    def findMaxLength(self, s, k, ch):
        count = i = j = 0
        max_count = 0
        while i < len(s):
            if s[i] == ch:
                count += 1
                i += 1
            elif k > 0:
                k = k - 1
                i += 1
                count += 1
            else:
                if s[j] != ch:
                    k = k + 1
                count = count - 1
                j = j + 1
            max_count = max(count, max_count)
        return max_count


print(Solution().characterReplacement('ABAB', 2))
print(Solution().characterReplacement('AABABBA', 1))
print(Solution().characterReplacement('AABABBB', 1))

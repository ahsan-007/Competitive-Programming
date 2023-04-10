# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = curr_lentgth = i = 0
        characters = {}
        last_repeating_char = 0
        while i < len(s):
            if s[i] in characters:
                curr_lentgth = i - max(characters[s[i]], last_repeating_char)
                last_repeating_char = max(
                    characters[s[i]], last_repeating_char)
            else:
                curr_lentgth = curr_lentgth + 1
            max_length = max(curr_lentgth, max_length)
            characters[s[i]] = i
            i = i + 1
        return max_length


print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('bbbbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
print(Solution().lengthOfLongestSubstring('abba'))
print(Solution().lengthOfLongestSubstring('abcdabef'))
print(Solution().lengthOfLongestSubstring('aab'))
print(Solution().lengthOfLongestSubstring('tmmzuxt'))
print(Solution().lengthOfLongestSubstring('wobgrovw'))
print(Solution().lengthOfLongestSubstring('zwnigfunjwz'))

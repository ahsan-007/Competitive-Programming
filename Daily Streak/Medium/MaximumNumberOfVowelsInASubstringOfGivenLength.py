# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = vowels_count = 0
        i = j = 0
        # cost of membership operator (in) with set is O(1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while j < len(s):
            if j-i < k:
                if s[j] in vowels:
                    vowels_count = vowels_count + 1
                    max_vowels = max(max_vowels, vowels_count)
                j = j + 1
            else:
                if s[i] in vowels:
                    vowels_count = vowels_count - 1
                i = i + 1
            if max_vowels == k:
                return max_vowels
        return max_vowels


print(Solution().maxVowels(s="abciiidef", k=3))
print(Solution().maxVowels(s="aeiou", k=2))
print(Solution().maxVowels(s="leetcode", k=3))

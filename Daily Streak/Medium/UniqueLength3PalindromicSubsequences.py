# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2023-11-14

class Solution:
    # Time: O(N)
    # Space: O(N)
    def countPalindromicSubsequence(self, s: str) -> int:
        def find(s, ch):
            try:
                return s.index(ch)
            except:
                return -1

        palndromicSubsequence = set()
        for i in range(len(s)):
            ind = find(s[i+1:], s[i])
            if ind != -1:
                ind = ind + i + 1

            for j in range(i+1, ind):
                palndromicSubsequence.add(s[i] + s[j] + s[i])

            if ind != -1 and find(s[ind+1:], s[i]) != -1:
                palndromicSubsequence.add(s[i] * 3)

        return len(palndromicSubsequence)

    # Time: O(N)
    # Space: O(1)
    def countPalindromicSubsequenceV2(self, s: str) -> int:
        letters = set(s)
        indexes = {}
        for ch in letters:
            if ch not in indexes:
                indexes[ch] = {'first': s.index(ch), 'last': s.rindex(ch)}

        count = 0
        for ch in indexes:
            seen = set()
            for i in range(indexes[ch]['first']+1, indexes[ch]['last']):
                seen.add(s[i])
            count = count + len(seen)
        return count


print(Solution().countPalindromicSubsequence(s="aabca"))
print(Solution().countPalindromicSubsequence(s="adc"))
print(Solution().countPalindromicSubsequence(s="bbcbaba"))


print(Solution().countPalindromicSubsequenceV2(s="aabca"))
print(Solution().countPalindromicSubsequenceV2(s="adc"))
print(Solution().countPalindromicSubsequenceV2(s="bbcbaba"))

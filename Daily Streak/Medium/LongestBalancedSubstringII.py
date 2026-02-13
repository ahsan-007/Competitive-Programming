# https://leetcode.com/problems/longest-balanced-substring-ii/description/?envType=daily-question&envId=2026-02-13

class Solution:
    def longestBalanced(self, s: str) -> int:
        def findLongestBalancedWith2Chars(x, y):
            i = 0
            maxLength = -1
            while i < len(s):
                diff = 0
                diffMap = {0: i-1}
                if s[i] in {x, y}:
                    while i < len(s) and s[i] in {x, y}:
                        diff += 1 if s[i] == x else - 1
                        if diff in diffMap:
                            maxLength = max(maxLength, i - diffMap[diff])
                        else:
                            diffMap[diff] = i
                        i = i + 1
                else:
                    i = i + 1

            return maxLength

        maxLength = -1

        # case 1: considering 1 character only
        char = ''
        count = 0
        for i in range(len(s)):
            if char == s[i]:
                count += 1
            else:
                maxLength = max(maxLength, count)
                char = s[i]
                count = 1

            if i == len(s) - 1:
                maxLength = max(maxLength, count)

        # case 2: 2 distinct characters
        maxLength = max(maxLength, findLongestBalancedWith2Chars('a', 'b'))
        maxLength = max(maxLength, findLongestBalancedWith2Chars('a', 'c'))
        maxLength = max(maxLength, findLongestBalancedWith2Chars('b', 'c'))

        # case 3: 3 distinct characters
        freq = [0, 0, 0]
        firstOccurence = {(0, 0): -1}
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1

            d1 = freq[0] - freq[1]
            d2 = freq[0] - freq[2]

            pair = (d1, d2)
            if pair in firstOccurence:
                maxLength = max(maxLength, i - firstOccurence[pair])
            else:
                firstOccurence[pair] = i

        return maxLength


print(Solution().longestBalanced(s="abbac"))
print(Solution().longestBalanced(s="aabcc"))
print(Solution().longestBalanced(s="aba"))
print(Solution().longestBalanced(s="accb"))

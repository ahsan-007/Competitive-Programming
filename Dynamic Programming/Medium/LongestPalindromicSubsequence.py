# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        return self.longestPalindromeUtil(s, 0, len(s)-1, memo)

    def longestPalindromeUtil(self, s, i, j, memo):
        if i > j:
            return 0
        if i == j:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]
        if s[i] == s[j]:
            memo[(i, j)] = 2 + self.longestPalindromeUtil(s, i+1, j-1, memo)
        else:
            memo[(i, j-1)] = self.longestPalindromeUtil(s, i, j-1, memo)
            memo[(i+1, j)] = self.longestPalindromeUtil(s, i+1, j, memo)

            memo[(i, j)] = max(memo[(i, j-1)], memo[(i+1, j)])
        return memo[(i, j)]


print(Solution().longestPalindromeSubseq('bbbab'))
print(Solution().longestPalindromeSubseq('cbbd'))
print(Solution().longestPalindromeSubseq('cdad'))
print(Solution().longestPalindromeSubseq('abdab'))
print(Solution().longestPalindromeSubseq('ddbbaabb'))
print(Solution().longestPalindromeSubseq(
    'asdsdjfahlkjdfhjvhcjanhhnfcjchfjadhfdaanclvkfdnjvlmsflmvafmacmmcmfcalkjfcdhflkshdaljhfckjadhfc'))

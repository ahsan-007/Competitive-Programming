# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.numDecodingsUtil(s, memo)

    def numDecodingsUtil(self, s, memo):
        if s in memo:
            return memo[s]
        if s[0] == '0' or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) <= 2:
            return 1 if len(s) == 1 or (len(s) == 2 and 1 <= int(s[1]) <= 6 and int(s[0])) <= 2 else 0
        memo[s[1:]] = self.numDecodingsUtil(s[1:], memo)
        res = memo[s[1:]]
        if len(s) == 2 and 1 <= int(s[1]) <= 6 and int(s[0]) <= 2:
            memo[s[2:]] = self.numDecodingsUtil(s[2:], memo)
            res = res + memo[s[2:]]
        memo[s] = res
        return memo[s]


print(Solution().numDecodings('11106'))
print(Solution().numDecodings('226'))
print(Solution().numDecodings('06'))
print(Solution().numDecodings('1123'))
print(Solution().numDecodings('205695462'))

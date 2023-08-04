# https://leetcode.com/problems/word-break/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakUtil(s, wordDict, {})

    def wordBreakUtil(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return True
        for i in range(len(s) + 1):
            if s[:i] in wordDict:
                if self.wordBreakUtil(s[i:], wordDict, memo):
                    memo[s] = True
                    return True
        memo[s] = False
        return False


print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(Solution().wordBreak("applepenapple", wordDict=["apple", "pen"]))
print(Solution().wordBreak(s="catsandog", wordDict=[
      "cats", "dog", "sand", "and", "cat"]))
print(Solution().wordBreak(s="cars", wordDict=["car", "ca", "rs"]))
print(Solution().wordBreak(s="cbca", wordDict=["bc", "cq"]))
print(Solution().wordBreak(s="ccaccc", wordDict=["cc", "ac"]))
print(Solution().wordBreak(s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                           wordDict=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))

# https://leetcode.com/problems/word-break-ii/description

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def wordBreakUtil(s, wordDict, i, memo):
            if i == len(s):
                return ['']

            if i not in memo:
                j = i + 1
                words = []
                while j <= len(s):
                    if s[i:j] in wordDict:
                        rwords = wordBreakUtil(s, wordDict, j, memo)
                        for word in rwords:
                            words.append(s[i:j] + (' ' if word else '') + word)
                    j = j + 1

                memo[i] = words

            return memo[i]

        return wordBreakUtil(s, wordDict, 0, {})


print(Solution().wordBreak(s="catsanddog",
                           wordDict=["cat", "cats", "and", "sand", "dog"]))

print(Solution().wordBreak(s="pineapplepenapple",
                           wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))

print(Solution().wordBreak(s="catsandog",
                           wordDict=["cats", "dog", "sand", "and", "cat"]))

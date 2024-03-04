# https://leetcode.com/problems/bag-of-tokens/description/?envType=daily-question&envId=2024-03-04

from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        maxScore = 0
        i = 0
        j = len(tokens) - 1
        tokens.sort()

        while i <= j:
            if power >= tokens[i]:
                power = power - tokens[i]
                score = score + 1
                i = i + 1

            elif score > 0:
                power = power + tokens[j]
                score = score - 1
                j = j - 1

            else:
                return maxScore

            maxScore = max(maxScore, score)

        return maxScore


print(Solution().bagOfTokensScore(tokens=[100], power=50))
print(Solution().bagOfTokensScore(tokens=[200, 100], power=150))
print(Solution().bagOfTokensScore(tokens=[100, 200, 300, 400], power=200))
print(Solution().bagOfTokensScore(tokens=[100, 200], power=100))

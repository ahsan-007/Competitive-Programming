# https://leetcode.com/problems/stone-game/description/?envType=daily-question&envId=2026-08-02

from typing import List
from functools import lru_cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def stoneGameUtil(i, j, isAliceTurn, memo):
            if i > j:
                return 0, 0

            if (i, j, isAliceTurn) not in memo:
                aliceLeft, bobLeft = stoneGameUtil(
                    i+1, j, not isAliceTurn, memo)
                aliceRight, bobRight = stoneGameUtil(
                    i, j-1, not isAliceTurn, memo)

                if isAliceTurn:
                    aliceLeft = aliceLeft + piles[i]
                    aliceRight = aliceRight + piles[j]
                    if aliceLeft > aliceRight:
                        memo[(i, j, isAliceTurn)] = (aliceLeft, bobLeft)
                    else:
                        memo[(i, j, isAliceTurn)] = (aliceRight, bobRight)
                else:
                    bobLeft = bobLeft + piles[i]
                    bobRight = bobRight + piles[j]
                    if bobLeft > bobRight:
                        memo[(i, j, isAliceTurn)] = (aliceLeft, bobLeft)
                    else:
                        memo[(i, j, isAliceTurn)] = (aliceRight, bobRight)

            return memo[(i, j, isAliceTurn)]

        alice, bob = stoneGameUtil(0, len(piles)-1, True, {})
        return alice > bob

    def stoneGameV2(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def stoneGameUtil(i, j):
            if i > j:
                return 0

            # if alice's turn, add score
            if ((j - i - len(piles)) % 2) == 1:
                return max(piles[i] + stoneGameUtil(i+1, j), piles[j] + stoneGameUtil(i, j-1))
            else:
                # if bob's turn subtract score, and try to minimize alice's score
                return min(stoneGameUtil(i+1, j) - piles[i], stoneGameUtil(i, j-1) - piles[j])

        return stoneGameUtil(0, len(piles)-1) > 0

    # Mathematical approach
    # if size of the pile is 2, alice has the choice to either pick 1st pile or 2nd pile, she will always pick the max and hence will always win
    # if size of the pile is 4
    #   - in 1st turn, alice can either take 1st pile or 4th pile
    #   - if alice picked 1st pile, bob will have the choice to pick 2nd and 4th pile, while alice will always have the choice to pick the 3rd pile
    #   - if alice picked 4th pile, bob will have the choice to pick 1st and 3rd pile, while alice will always have the choice to pick the 2nd pile
    #   - So alice can pick 1, 3 or 2, 4 depending upon which is greater and hence will aways win
    # Same idea can be extended to N piles
    def stoneGameV3(self, piles: List[int]) -> bool:
        return True


print(Solution().stoneGame(piles=[5, 3, 4, 5]))
print(Solution().stoneGame(piles=[3, 7, 2, 3]))


print(Solution().stoneGameV2(piles=[5, 3, 4, 5]))
print(Solution().stoneGameV2(piles=[3, 7, 2, 3]))

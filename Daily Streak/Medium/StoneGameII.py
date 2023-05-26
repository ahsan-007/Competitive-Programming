# https://leetcode.com/problems/stone-game-ii/

from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        return self.stoneGameIIUtil(piles, 0, 1, True, memo={})

    def stoneGameIIUtil(self, piles, i, M, turn_of_alice, memo):
        if i == len(piles):
            return 0
        if (i, M, turn_of_alice) in memo:
            return memo[(i, M, turn_of_alice)]
        stones = 0
        alice_stones = 0
        for j in range(i, i + 2*M):
            if j >= len(piles):
                memo[(i, M, turn_of_alice)] = alice_stones
                return alice_stones
            if turn_of_alice:
                stones = stones + piles[j]
                alice_stones = max(alice_stones, self.stoneGameIIUtil(
                    piles, j+1, max(M, (j-i) + 1), False, memo) + stones)
            else:
                alice_stones_suff = self.stoneGameIIUtil(
                    piles, j+1, max(M, (j-i)+1), True, memo)

                alice_stones = alice_stones_suff if alice_stones == 0 else min(
                    alice_stones, alice_stones_suff)
        memo[(i, M, turn_of_alice)] = alice_stones
        return alice_stones


print(Solution().stoneGameII([2, 7, 9, 4, 4]))
print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]))
print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]*15))

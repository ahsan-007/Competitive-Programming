# https://leetcode.com/problems/furthest-point-from-origin/description/?envType=daily-question&envId=2026-04-24


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = 0
        dash = 0
        for move in moves:
            if move == "R":
                count += 1
            elif move == "L":
                count -= 1
            else:
                dash += 1
        return abs(count) + dash


print(Solution().furthestDistanceFromOrigin(moves="L_RL__R"))
print(Solution().furthestDistanceFromOrigin(moves="_R__LL_"))
print(Solution().furthestDistanceFromOrigin(moves="_______"))

# https://leetcode.com/problems/robot-return-to-origin/description/?envType=daily-question&envId=2026-04-05

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        i = 0
        j = 0
        for move in moves:
            if move == 'U':
                i = i - 1
            elif move == 'D':
                i = i + 1
            elif move == 'L':
                j = j - 1
            elif move == 'R':
                j = j + 1

        return i == 0 and j == 0

    def judgeCircleV2(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


print(Solution().judgeCircle(moves="UD"))
print(Solution().judgeCircle(moves="LL"))

print("-"*100)

print(Solution().judgeCircleV2(moves="UD"))
print(Solution().judgeCircleV2(moves="LL"))

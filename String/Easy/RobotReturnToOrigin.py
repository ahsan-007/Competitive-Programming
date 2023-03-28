# https://leetcode.com/problems/robot-return-to-origin/


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == 'U':
                y = y + 1
            elif move == 'D':
                y = y - 1
            elif move == 'R':
                x = x + 1
            else:
                x = x - 1
        return x == 0 and y == 0
    
print(Solution().judgeCircle(moves = "UD"))
print(Solution().judgeCircle(moves = "LL"))

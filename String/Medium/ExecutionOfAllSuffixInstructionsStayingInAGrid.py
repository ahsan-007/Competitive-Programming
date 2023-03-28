# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        return [self.executeInstructionsUtil(n, startPos, s, i) for i in range(len(s))]

    def executeInstructionsUtil(self, n: int, startPos: List[int], s: str, i) -> List[int]:
        instruction_count = 0
        row, col = startPos[0], startPos[1]
        while i < len(s):
            if s[i] == 'U':
                if row - 1 >= 0:
                    row = row - 1
                else:
                    return instruction_count
            elif s[i] == 'D':
                if row + 1 < n:
                    row = row + 1
                else:
                    return instruction_count
            elif s[i] == 'R':
                if col + 1 < n:
                    col = col + 1
                else:
                    return instruction_count
            else:
                if col - 1 >= 0:
                    col = col - 1
                else:
                    return instruction_count
            i = i + 1
            instruction_count = instruction_count + 1

        return instruction_count


print(Solution().executeInstructions(n=3, startPos=[0, 1], s="RRDDLU"))
print(Solution().executeInstructions(n=2, startPos=[1, 1], s="LURD"))
print(Solution().executeInstructions(n=1, startPos=[0, 0], s="LRUD"))

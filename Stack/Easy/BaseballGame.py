# https://leetcode.com/problems/baseball-game/

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                if len(stack) > 1:
                    stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                if stack:
                    stack.append(stack[-1] * 2)
            elif op == 'C':
                if stack:
                    stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)


print(Solution().calPoints(["5", "2", "C", "D", "+"]))
print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(Solution().calPoints(["1", "C"]))

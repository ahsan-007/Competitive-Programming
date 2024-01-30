# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=daily-question&envId=2024-01-30

from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for token in tokens:
            if token in ['*', '/', '+', '-']:
                b = operands.pop()
                a = operands.pop()
                if token == '*':
                    operands.append(a * b)
                elif token == '/':
                    operands.append((a // b) if a // b >=
                                    0 else math.ceil(a / b))
                elif token == '+':
                    operands.append(a + b)
                else:
                    operands.append(a - b)
            else:
                operands.append(int(token))

        return operands[0]


print(Solution().evalRPN(tokens=["2", "1", "+", "3", "*"]))
print(Solution().evalRPN(tokens=["4", "13", "5", "/", "+"]))
print(Solution().evalRPN(
    tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(Solution().evalRPN(
    tokens=["4", "-2", "/", "2", "-3", "-", "-"]))

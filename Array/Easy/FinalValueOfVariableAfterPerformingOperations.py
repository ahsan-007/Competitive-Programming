# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for op in operations:
            X = X + 1 if op == 'X++' or op == '++X' else X - 1
        return X


print(Solution().finalValueAfterOperations(operations=["--X", "X++", "X++"]))
print(Solution().finalValueAfterOperations(operations=["++X", "++X", "X++"]))
print(Solution().finalValueAfterOperations(
    operations=["X++", "++X", "--X", "X--"]))

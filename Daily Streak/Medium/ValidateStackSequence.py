# https://leetcode.com/problems/validate-stack-sequences/

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False
        i = j = 0
        while i < len(pushed):
            if pushed[i] == popped[j]:
                pushed.pop(i)
                if i != 0:
                    i = i - 1
                j = j + 1
            else:
                i = i + 1

        i = len(pushed) - 1
        while i >= 0:
            if pushed[i] != popped[j]:
                return False
            i = i - 1
            j = j + 1
        return True


print(Solution().validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))

print(Solution().validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))

print(Solution().validateStackSequences(
    pushed=[2, 1, 0], popped=[1, 2, 0]))

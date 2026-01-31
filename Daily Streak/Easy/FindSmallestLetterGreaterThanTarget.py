# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        while i < len(letters):
            if letters[i] > target:
                return letters[i]
            i = i + 1
        return letters[0]

    def nextGreatestLetterV2(self, letters: List[str], target: str) -> str:
        lb = 0
        ub = len(letters) - 1
        minGreatest = None
        while lb <= ub:
            mid = lb + (ub - lb) // 2
            if ord(letters[mid]) > ord(target):
                minGreatest = letters[mid]
                ub = mid - 1
            else:
                lb = mid + 1
        return minGreatest if minGreatest else letters[0]


print(Solution().nextGreatestLetter(letters=["c", "f", "j"], target="a"))
print(Solution().nextGreatestLetter(letters=["c", "f", "j"], target="c"))
print(Solution().nextGreatestLetter(letters=["x", "x", "y", "y"], target="z"))

print(Solution().nextGreatestLetterV2(letters=["c", "f", "j"], target="a"))
print(Solution().nextGreatestLetterV2(letters=["c", "f", "j"], target="c"))
print(Solution().nextGreatestLetterV2(
    letters=["x", "x", "y", "y"], target="z"))

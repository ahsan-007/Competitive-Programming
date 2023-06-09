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


print(Solution().nextGreatestLetter(letters=["c", "f", "j"], target="a"))
print(Solution().nextGreatestLetter(letters=["c", "f", "j"], target="c"))
print(Solution().nextGreatestLetter(letters=["x", "x", "y", "y"], target="z"))

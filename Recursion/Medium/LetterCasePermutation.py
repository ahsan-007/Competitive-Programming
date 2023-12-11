# https://leetcode.com/problems/letter-case-permutation/description/

from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def makePermutations(s, i):
            if i >= len(s):
                return []

            permuations = makePermutations(s, i + 1)

            if not permuations:
                return [s[i]] if not s[i].isalpha() else [s[i].lower(), s[i].upper()]

            newPermutations = []
            for perm in permuations:
                newPermutations.append(f"{s[i]}{perm}")
                if s[i].isalpha():
                    newPermutations.append(
                        f"{s[i].upper()}{perm}" if s[i].islower() else f"{s[i].lower()}{perm}")
            return newPermutations

        return makePermutations(s, 0)


print(Solution().letterCasePermutation("a1b2"))
print(Solution().letterCasePermutation("abcdefg"))

# https://leetcode.com/problems/pyramid-transition-matrix/description/?envType=daily-question&envId=2025-12-29

from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def populateTrie(trie, pattern):
            if not pattern:
                return

            if pattern[0] not in trie:
                trie[pattern[0]] = {}

            populateTrie(trie[pattern[0]], pattern[1:])

        def getPatternTrie(patterns):
            trie = {}
            for pattern in patterns:
                populateTrie(trie, pattern)
            return trie

        def pyramidTransitionUtil(pyramid, allowed, i, patternTrie):
            # check if pyramid completed
            if len(pyramid) == len(pyramid[-1]):
                return True

            # if kth layer is completed, add k-1 th layer
            if len(pyramid) < 2 or len(pyramid[0]) == len(pyramid[1]) - 1:
                pyramid.insert(0, "")
                i = 0

            # find the allowed patterns starting with 2 letters for ith block in kth layer
            # 2 letters are ith and i+1 th block in k+1 th layer
            for ch in patternTrie.get(pyramid[1][i], {}).get(pyramid[1][i+1], {}):
                pyramid[0] += ch
                if pyramidTransitionUtil(pyramid, allowed, i + 1, patternTrie):
                    return True
                pyramid[0] = pyramid[0][:-1]
            
            # remove empty layer if kth layer could not be build using the allowed patterns
            if pyramid[0] == "":
                del pyramid[0]
            return False

        return pyramidTransitionUtil([bottom], allowed, 0, getPatternTrie(allowed))


print(Solution().pyramidTransition(
    bottom="BCD", allowed=["BCC", "CDE", "CEA", "FFF"]))
print(Solution().pyramidTransition(bottom="AAAA",
      allowed=["AAB", "AAC", "BCD", "BBE", "DEF"]))

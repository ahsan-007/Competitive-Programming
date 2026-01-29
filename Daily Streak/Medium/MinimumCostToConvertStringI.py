# https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=daily-question&envId=2026-01-29

from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def getIndex(ch):
            return ord(ch) - ord('a')

        conversionCost = [[float("+inf")] * i +
                          [0] +
                          [float("+inf")] * (26 - i) for i in range(26)]

        for i in range(len(original)):
            r = getIndex(original[i])
            c = getIndex(changed[i])
            conversionCost[r][c] = min(cost[i], conversionCost[r][c])

        for i in range(26):
            for j in range(26):
                for k in range(26):
                    if i != j and i != k:
                        conversionCost[j][k] = min(conversionCost[j][k],
                                                   conversionCost[j][i] + conversionCost[i][k])

        minCost = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                r = getIndex(source[i])
                c = getIndex(target[i])
                if conversionCost[r][c] == float("+inf"):
                    return -1
                minCost += conversionCost[r][c]
        return minCost



print(Solution().minimumCost(source="abcd", target="acbe",
                             original=["a", "b", "c", "c", "e", "d"],
                             changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20]))

print(Solution().minimumCost(source="aaaa", target="bbbb",
      original=["a", "c"], changed=["c", "b"], cost=[1, 2]))

print(Solution().minimumCost(source="abcd", target="abce",
      original=["a"], changed=["e"], cost=[10000]))

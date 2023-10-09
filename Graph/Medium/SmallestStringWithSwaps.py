# https://leetcode.com/problems/smallest-string-with-swaps/description/

from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class DisjointSet:
            def __init__(self, nodes) -> None:
                self.root = [i for i in range(nodes)]
                self.rank = [1 for i in range(nodes)]

            def find(self, i):
                if self.root[i] == i:
                    return i

                self.root[i] = self.find(self.root[i])
                return self.root[i]

            def union(self, i, j):
                iRoot = self.find(i)
                jRoot = self.find(j)

                if iRoot == jRoot:
                    return

                if self.rank[iRoot] > self.rank[jRoot]:
                    self.root[jRoot] = iRoot

                elif self.rank[jRoot] > self.rank[iRoot]:
                    self.root[iRoot] = jRoot

                else:
                    self.root[jRoot] = iRoot
                    self.rank[iRoot] = self.rank[iRoot] + 1

        disjointSet = DisjointSet(len(s))
        for pair in pairs:
            disjointSet.union(pair[0], pair[1])

        uniqueSets = {}
        for i in range(len(s)):
            if disjointSet.find(i) not in uniqueSets:
                uniqueSets[disjointSet.find(i)] = []
            uniqueSets[disjointSet.find(i)].append(s[i])

        for set in uniqueSets:
            uniqueSets[set].sort(reverse=True)

        res = ''
        for i in range(len(s)):
            res = res + uniqueSets[disjointSet.find(i)].pop()

        return res


print(Solution().smallestStringWithSwaps(
    s="dcab", pairs=[[0, 3], [1, 2]]))

print(Solution().smallestStringWithSwaps(
    s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))

print(Solution().smallestStringWithSwaps(
    s="cba", pairs=[[0, 1], [1, 2]]))

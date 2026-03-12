# http://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/?envType=daily-question&envId=2026-03-12

from typing import List


class DSU:
    def __init__(self, parent):
        self.parent = parent

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, px, py):
        px = self.find(px)
        py = self.find(py)
        self.parent[px] = py


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        stability = float("+inf")
        edges.sort(key=lambda x: (x[3], x[2]), reverse=True)

        edgesCount = 0
        dsu = DSU(list(range(n)))
        i = 0

        while i < len(edges) and edges[i][3] == 1:
            u, v, s, _ = edges[i]
            if dsu.find(u) == dsu.find(v):
                return -1
            dsu.join(u, v)
            stability = min(stability, s)
            edgesCount += 1
            i = i + 1

        optionalEdges = []

        while i < len(edges) and edgesCount < n - 1:
            u, v, s, _ = edges[i]
            if dsu.find(u) != dsu.find(v):
                dsu.join(u, v)
                optionalEdges.append(s)
                edgesCount += 1
            i = i + 1

        j = len(optionalEdges) - 1
        while j >= 0:
            if k > 0:
                k = k - 1
                stability = min(stability, optionalEdges[j] * 2)
            else:
                stability = min(stability, optionalEdges[j])
            j = j - 1

        return -1 if stability == float("+inf") or edgesCount != (n-1) else stability


print(Solution().maxStability(n=3, edges=[[0, 1, 2, 1], [1, 2, 3, 0]], k=1))
print(Solution().maxStability(n=3,
                              edges=[[0, 1, 4, 0], [1, 2, 3, 0], [0, 2, 1, 0]], k=2))
print(Solution().maxStability(n=3,
                              edges=[[0, 1, 1, 1], [1, 2, 1, 1], [2, 0, 1, 1]], k=0))
print(Solution().maxStability(n=5,
                              edges=[[3, 2, 56447, 1], [4, 3, 80497, 1], [0, 4, 45565, 1], [
                                  1, 2, 85317, 1], [0, 1, 87891, 0], [0, 2, 78889, 0], [2, 4, 73816, 0]],
                              k=4))
print(Solution().maxStability(n=3,
                              edges=[[0, 1, 55839, 0], [
                                  0, 2, 39867, 0], [1, 2, 62840, 0]],
                              k=1))
print(Solution().maxStability(n=5,
                              edges=[[0, 1, 24819, 0], [2, 4, 86210, 1], [
                                  1, 2, 53407, 0], [3, 4, 56877, 0], [1, 3, 89383, 0]],
                              k=5))

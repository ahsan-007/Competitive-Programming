# https://leetcode.com/problems/is-graph-bipartite/

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        i = 0
        setA = set()
        setB = set()
        while i < len(graph):
            if i not in setA and i not in setB and not self.isBipartiteUtil(graph, i, setA, setB):
                return False
            i = i + 1
        return True

    def isBipartiteUtil(self, graph, node, setA={}, setB={}):
        if node not in setA and node not in setB:
            setA.add(node)
        for neighbor in graph[node]:
            if (neighbor in setA and node in setA) or (neighbor in setB and node in setB):
                return False
            elif neighbor not in setA and neighbor not in setB:
                setB.add(neighbor) if node in setA else setA.add(neighbor)
                if not self.isBipartiteUtil(graph, neighbor, setA, setB):
                    return False
        return True


print(Solution().isBipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(Solution().isBipartite(graph=[[1, 3], [0, 2], [1, 3], [0, 2]]))
print(Solution().isBipartite(graph=[[3], [2, 4], [1], [0, 4], [1, 3]]))
print(Solution().isBipartite(graph=[[5, 8], [7], [5, 6], [
      7, 8], [8], [0, 2], [2], [1, 3], [0, 3, 4]]))

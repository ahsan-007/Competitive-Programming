# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes_with_incoming_edges = set()
        for edge in edges:
            nodes_with_incoming_edges.add(edge[1])

        i = 0
        nodes_picked = []
        while i < n:
            if i not in nodes_with_incoming_edges:
                nodes_picked.append(i)
            i = i + 1
        return nodes_picked

    # Compact
    def findSmallestSetOfVerticesV2(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes_with_incoming_edges = set(edge[1] for edge in edges)
        return [i for i in range(n) if i not in nodes_with_incoming_edges]


print(Solution().findSmallestSetOfVertices(
    n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
print(Solution().findSmallestSetOfVertices(
    n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))

# https://leetcode.com/problems/find-center-of-star-graph/

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_count = {}
        for edge in edges:
            edge_count[edge[0]] = edge_count.get(edge[0], 0) + 1
            edge_count[edge[1]] = edge_count.get(edge[1], 0) + 1

        nodes_count = len(edge_count.keys())
        for edge in edge_count:
            if edge_count[edge] == nodes_count - 1:
                return edge


print(Solution().findCenter(edges=[[1, 2], [2, 3], [4, 2]]))
print(Solution().findCenter(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]))

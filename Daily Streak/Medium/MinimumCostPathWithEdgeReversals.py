# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/description/?envType=daily-question&envId=2026-01-27

from typing import List
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        nodes = []

        distances = [float("+inf")] * n
        distances[0] = 0

        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            graph[edge[0]].append(edge[1:])

            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[1]].append([edge[0], 2 * edge[2]])

        heapq.heappush(nodes, (0, 0))

        while nodes:
            d, u = heapq.heappop(nodes)

            if d <= distances[u]:
                if u in graph:
                    for v, w in graph[u]:
                        if distances[u] + w < distances[v]:
                            distances[v] = distances[u] + w
                            heapq.heappush(nodes, (distances[v], v))
        return distances[-1] if distances[-1] != float("inf") else -1


print(Solution().minCost(n=4,
                         edges=[[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]))
print(Solution().minCost(n=4,
                         edges=[[0, 2, 1], [2, 1, 1], [1, 3, 1], [2, 3, 3]]))
print(Solution().minCost(n=4,
                         edges=[[2, 3, 25], [2, 1, 18], [3, 1, 2]]))

# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/description/?envType=daily-question&envId=2026-10-30

from typing import List
from heapq import heappush, heappop


class Solution:
    def shortestPath(
        self, n: int, edges: List[List[int]], labels: str, k: int
    ) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))

        dis = [[2**31 - 1] * (k + 1) for _ in range(n)]
        pq = []

        dis[0][1] = 0
        heappush(pq, (0, 0, 1))

        while pq:
            d, x, cnt = heappop(pq)

            if d > dis[x][cnt]:
                continue
            if x == n - 1:
                return d

            for y, w in g[x]:
                new_cnt = cnt + 1 if labels[x] == labels[y] else 1
                if new_cnt > k:
                    continue

                nd = d + w
                if nd < dis[y][new_cnt]:
                    dis[y][new_cnt] = nd
                    heappush(pq, (nd, y, new_cnt))

        return -1


print(Solution().shortestPath(n=3, edges=[
      [0, 1, 1], [1, 2, 1], [0, 2, 3]], labels="aab", k=1))
print(Solution().shortestPath(n=3, edges=[
      [0, 1, 1], [1, 2, 1], [0, 2, 3]], labels="aab", k=2))
print(Solution().shortestPath(n=3, edges=[
      [0, 1, 1], [1, 2, 1]], labels="aaa", k=2))

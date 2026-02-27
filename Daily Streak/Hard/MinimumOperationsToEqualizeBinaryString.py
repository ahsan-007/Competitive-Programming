# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/description/?envType=daily-question&envId=2026-02-27

from sortedcontainers import SortedList
from collections import deque


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n, m = len(s), s.count("0")
        dist = [float("inf")] * (n + 1)
        nodeSets = [
            SortedList(range(0, n + 1, 2)),
            SortedList(range(1, n + 1, 2)),
        ]
        q = deque([m])
        dist[m] = 0
        nodeSets[m % 2].remove(m)
        while q:
            m = q.popleft()
            c1, c2 = max(k - n + m, 0), min(m, k)
            lnode, rnode = m + k - 2 * c2, m + k - 2 * c1
            nodeSet = nodeSets[lnode % 2]
            idx = nodeSet.bisect_left(lnode)
            while idx < len(nodeSet) and nodeSet[idx] <= rnode:
                m2 = nodeSet[idx]
                dist[m2] = dist[m] + 1
                q.append(m2)
                nodeSet.pop(idx)
        return -1 if dist[0] == float("inf") else dist[0]


print(Solution().minOperations(s="110", k=1))
print(Solution().minOperations(s="0101", k=3))
print(Solution().minOperations(s="101", k=2))
print(Solution().minOperations(s="000", k=1))
print(Solution().minOperations(s="111", k=1))
print(Solution().minOperations(s="001", k=3))
print(Solution().minOperations(s="0", k=1))

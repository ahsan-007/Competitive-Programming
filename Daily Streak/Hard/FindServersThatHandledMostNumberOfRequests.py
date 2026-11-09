# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/description/?envType=daily-question&envId=2026-11-09

import heapq
from statistics import multimode


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free_servers = list(range(k))
        handled = []
        busy_servers = []
        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy_servers and busy_servers[0][0] <= t:
                heapq.heappush(free_servers, i +
                               (heapq.heappop(busy_servers)[1] - i) % k)
            if free_servers:
                x = heapq.heappop(free_servers) % k
                heapq.heappush(busy_servers, (t + d, x))
                handled.append(x)

        return multimode(handled)


print(Solution().busiestServers(k=3, arrival=[
      1, 2, 3, 4, 5], load=[5, 2, 3, 3, 3]))
print(Solution().busiestServers(k=3, arrival=[1, 2, 3, 4], load=[1, 2, 1, 2]))
print(Solution().busiestServers(k=3, arrival=[1, 2, 3], load=[10, 12, 11]))

# https://leetcode.com/problems/process-tasks-using-servers/description/?envType=daily-question&envId=2026-11-07

import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = []
        for i, server in enumerate(servers):
            heapq.heappush(free_servers, (server, i))

        busy_servers = []
        t = 0
        ans = [0] * len(tasks)
        queue = []
        while t < len(tasks) or queue:
            while busy_servers and busy_servers[0][0] == t:
                _, server, i = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (server, i))

            if t < len(tasks):
                queue.append(t)

            while free_servers and queue:
                server, i = heapq.heappop(free_servers)
                heapq.heappush(busy_servers, (t + tasks[queue[0]], server, i))
                ans[queue[0]] = i
                queue.pop(0)

            if t < len(tasks):
                t = t + 1
            else:
                t = busy_servers[0][0]
        return ans


print(Solution().assignTasks(servers=[3, 3, 2], tasks=[1, 2, 3, 2, 1, 2]))
print(Solution().assignTasks(
    servers=[5, 1, 4, 3, 2], tasks=[2, 1, 2, 4, 5, 2, 1]))
print(Solution().assignTasks(servers=[10, 63, 95, 16, 85, 57, 83, 95, 6, 29, 71], tasks=[
      70, 31, 83, 15, 32, 67, 98, 65, 56, 48, 38, 90, 5]))

# https://leetcode.com/problems/parallel-courses-iii/description/?envType=daily-question&envId=2023-10-18

from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[0 for i in range(n)] for j in range(n)]
        indegree = [0 for i in range(n)]
        for relation in relations:
            indegree[relation[1]-1] += 1
            graph[relation[0]-1][relation[1]-1] = 1

        maxTime = [0 for i in range(n)]
        queue = []
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
                maxTime[node] = time[node]

        while queue:
            node = queue.pop(0)
            for neighbor in range(n):
                if graph[node][neighbor] == 1:
                    maxTime[neighbor] = max(
                        maxTime[neighbor], maxTime[node] + time[neighbor])
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        return max(maxTime)


print(Solution().minimumTime(n=3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]))
print(Solution().minimumTime(n=5, relations=[
      [1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]))

# https://leetcode.com/problems/number-of-provinces/description/

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]
        rank = [1 for i in range(len(isConnected))]

        for i in range(len(isConnected)):
            for j in range(i, len(isConnected)):
                if isConnected[i][j]:
                    self.union(root, rank, i, j)

        provinces = 0
        for i in range(len(root)):
            if root[i] == i:
                provinces = provinces + 1
        return provinces

    def union(self, root, rank, i, j):
        iRoot = self.find(root, i)
        jRoot = self.find(root, j)

        if iRoot == jRoot:
            return

        if rank[iRoot] > rank[jRoot]:
            root[jRoot] = iRoot

        elif rank[jRoot] > rank[iRoot]:
            root[iRoot] = jRoot

        else:
            root[jRoot] = iRoot
            rank[iRoot] = rank[iRoot] + 1

    def find(self, root, i):
        if root[i] == i:
            return i
        root[i] = self.find(root, root[i])
        return root[i]


print(Solution().findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(Solution().findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(Solution().findCircleNum(isConnected=[
      [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
print(Solution().findCircleNum(isConnected=[[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], [
      1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]))

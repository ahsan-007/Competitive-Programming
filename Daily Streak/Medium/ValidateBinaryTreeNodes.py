# https://leetcode.com/problems/validate-binary-tree-nodes/description/?envType=daily-question&envId=2023-10-17

from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def isParent(node, parentNode, parents):
            if node == -1:
                return False

            if node == parentNode:
                return True

            return isParent(node, parents[parentNode], parents) if parentNode in parents else False

        children = set()
        parents = {}
        rootNodes = set()
        i = 0
        while i < n:
            if i == leftChild[i] or i == rightChild[i] or leftChild[i] in children or rightChild[i] in children or isParent(leftChild[i], i, parents) or isParent(rightChild[i], i, parents):
                return False

            if leftChild[i] != -1:
                children.add(leftChild[i])
                if leftChild[i] in rootNodes:
                    rootNodes.remove(leftChild[i])
                parents[leftChild[i]] = i

            if rightChild[i] != -1:
                children.add(rightChild[i])
                if rightChild[i] in rootNodes:
                    rootNodes.remove(rightChild[i])
                parents[rightChild[i]] = i

            if i not in children:
                rootNodes.add(i)
            i = i + 1

        return len(rootNodes) == 1

    # dfs
    # Time: O(N)
    # Space: O(N)
    def validateBinaryTreeNodesV2(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def getRoot(n, leftChild, rightChild):
            i = 0
            while i < n:
                if i not in leftChild and i not in rightChild:
                    return i
                i = i + 1
            return - 1

        def dfs(i, n,  leftChild, rightChild, seen):
            if i >= n or i == -1:
                return True

            if i in seen:
                return False

            seen.add(i)
            if dfs(leftChild[i], n, leftChild, rightChild, seen) is False:
                return False
            return dfs(rightChild[i], n, leftChild, rightChild, seen)

        rootNode = getRoot(n, set(leftChild), set(rightChild))
        if rootNode == -1:
            return False

        seen = set()
        if dfs(rootNode, n, leftChild, rightChild, seen) is False:
            return False

        return len(seen) == n

    # bfs
    # Time: O(N)
    # Space: O(N)
    def validateBinaryTreeNodesV3(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def getRoot(n, leftChild, rightChild):
            i = 0
            while i < n:
                if i not in leftChild and i not in rightChild:
                    return i
                i = i + 1
            return - 1

        rootNode = getRoot(n, set(leftChild), set(rightChild))
        if rootNode == -1:
            return False

        queue = [rootNode]
        seen = {rootNode}
        while queue:
            node = queue.pop(0)
            if leftChild[node] in seen or rightChild[node] in seen:
                return False

            if leftChild[node] != -1:
                seen.add(leftChild[node])
                queue.append(leftChild[node])

            if rightChild[node] != -1:
                seen.add(rightChild[node])
                queue.append(rightChild[node])

        return len(seen) == n

    # disjoint sets
    # Time: O(N)
    # Space: O(N)
    def validateBinaryTreeNodesV4(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        class DisjointSets:
            def __init__(self, n):
                self.tree = list(range(n))
                self.rootNodes = n

            def find(self, node):
                if node != self.tree[node]:
                    self.tree[node] = self.find(self.tree[node])
                return self.tree[node]

            def union(self, parent, child):
                parent_parent = self.find(parent)
                child_parent = self.find(child)

                if child_parent != child or parent_parent == child_parent:
                    return False

                self.tree[child] = parent_parent
                self.rootNodes = self.rootNodes - 1
                return True

        disjointSets = DisjointSets(n)
        for i in range(n):
            for child in [leftChild[i], rightChild[i]]:
                if child != -1:
                    if not disjointSets.union(i, child):
                        return False
        return disjointSets.rootNodes == 1


print(Solution().validateBinaryTreeNodes(
    n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
print(Solution().validateBinaryTreeNodes(
    n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
print(Solution().validateBinaryTreeNodes(
    n=2, leftChild=[1, 0], rightChild=[-1, -1]))
print(Solution().validateBinaryTreeNodes(
    n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]))
print(Solution().validateBinaryTreeNodes(
    n=4, leftChild=[3, -1, 1, -1], rightChild=[-1, -1, 0, -1]))
print(Solution().validateBinaryTreeNodes(
    n=1, leftChild=[-1], rightChild=[-1]))
print(Solution().validateBinaryTreeNodes(
    n=4, leftChild=[1, 2, 0, -1], rightChild=[-1, -1, -1, -1]))

print()

print(Solution().validateBinaryTreeNodesV2(
    n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
print(Solution().validateBinaryTreeNodesV2(
    n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
print(Solution().validateBinaryTreeNodesV2(
    n=2, leftChild=[1, 0], rightChild=[-1, -1]))
print(Solution().validateBinaryTreeNodesV2(
    n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]))
print(Solution().validateBinaryTreeNodesV2(
    n=4, leftChild=[3, -1, 1, -1], rightChild=[-1, -1, 0, -1]))
print(Solution().validateBinaryTreeNodesV2(
    n=1, leftChild=[-1], rightChild=[-1]))
print(Solution().validateBinaryTreeNodesV2(
    n=4, leftChild=[1, 2, 0, -1], rightChild=[-1, -1, -1, -1]))

print()

print(Solution().validateBinaryTreeNodesV3(
    n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
print(Solution().validateBinaryTreeNodesV3(
    n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
print(Solution().validateBinaryTreeNodesV3(
    n=2, leftChild=[1, 0], rightChild=[-1, -1]))
print(Solution().validateBinaryTreeNodesV3(
    n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]))
print(Solution().validateBinaryTreeNodesV3(
    n=4, leftChild=[3, -1, 1, -1], rightChild=[-1, -1, 0, -1]))
print(Solution().validateBinaryTreeNodesV3(
    n=1, leftChild=[-1], rightChild=[-1]))
print(Solution().validateBinaryTreeNodesV3(
    n=4, leftChild=[1, 2, 0, -1], rightChild=[-1, -1, -1, -1]))

print()

print(Solution().validateBinaryTreeNodesV4(
    n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
print(Solution().validateBinaryTreeNodesV4(
    n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
print(Solution().validateBinaryTreeNodesV4(
    n=2, leftChild=[1, 0], rightChild=[-1, -1]))
print(Solution().validateBinaryTreeNodesV4(
    n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]))
print(Solution().validateBinaryTreeNodesV4(
    n=4, leftChild=[3, -1, 1, -1], rightChild=[-1, -1, 0, -1]))
print(Solution().validateBinaryTreeNodesV4(
    n=1, leftChild=[-1], rightChild=[-1]))
print(Solution().validateBinaryTreeNodesV4(
    n=4, leftChild=[1, 2, 0, -1], rightChild=[-1, -1, -1, -1]))

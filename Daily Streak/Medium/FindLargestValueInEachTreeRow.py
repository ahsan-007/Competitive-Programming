# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/?envType=daily-question&envId=2023-10-24

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS
    # Time: O(N)
    # Space: O(h)
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largestValues = []
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if level >= len(largestValues):
                largestValues.append(node.val)
            else:
                largestValues[level] = max(largestValues[level], node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))
        return largestValues

    # DFS
    # Time: O(N)
    # Space: O(h)
    def largestValuesV2(self, root: Optional[TreeNode]) -> List[int]:
        largestValues = []

        def largestValuesDFS(node, level):
            if not node:
                return

            if level >= len(largestValues):
                largestValues.append(node.val)
            else:
                largestValues[level] = max(largestValues[level], node.val)

            largestValuesDFS(node.left, level + 1)
            largestValuesDFS(node.right, level + 1)

        largestValuesDFS(root, 0)
        return largestValues


print(Solution().largestValues(TreeNode(1,
                                        TreeNode(3,
                                                 TreeNode(5),
                                                 TreeNode(3)),
                                        TreeNode(2,
                                                 None,
                                                 TreeNode(9)))))

print(Solution().largestValuesV2(TreeNode(1,
                                          TreeNode(3,
                                                   TreeNode(5),
                                                   TreeNode(3)),
                                          TreeNode(2,
                                                   None,
                                                   TreeNode(9)))))

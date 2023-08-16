# https://leetcode.com/problems/binary-tree-paths/

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        self.binaryTreePathUtil(root, "", paths)
        return paths

    def binaryTreePathUtil(self, root, path, paths):
        if not root:
            return

        if not root.left and not root.right:
            paths.append((path + '->'+str(root.val))[2:])
            return

        self.binaryTreePathUtil(root.left, path + "->" + str(root.val), paths)
        self.binaryTreePathUtil(root.right, path + "->" + str(root.val), paths)


print(Solution().binaryTreePaths(TreeNode(1,
                                          TreeNode(2,
                                                   None,
                                                   TreeNode(5)
                                                   ),
                                          TreeNode(3)
                                          )))

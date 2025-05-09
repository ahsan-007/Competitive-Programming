# https://leetcode.com/problems/count-complete-tree-nodes/description/

from typing import Optional
import math
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodesV2(self, root: Optional[TreeNode]) -> int:
        def findDepth(node):
            if not node:
                return -1

            return 1 + findDepth(node.left)

        h = findDepth(root)
        if h < 0:
            return 0

        elif findDepth(root.right) == h-1:
            return int(math.pow(2, h)) + self.countNodesV2(root.right)

        else:
            return int(math.pow(2, h-1)) + self.countNodesV2(root.left)


print(Solution().countNodes(root=TreeNode(1,
                                          left=TreeNode(2,
                                                        left=TreeNode(4)),
                                          right=TreeNode(3)
                                          )))

print(Solution().countNodesV2(root=TreeNode(1,
                                            left=TreeNode(2,
                                                          left=TreeNode(4)),
                                            right=TreeNode(3)
                                            )))

print(Solution().countNodes(root=TreeNode(1,
                                          left=TreeNode(2,
                                                        left=TreeNode(4),
                                                        right=TreeNode(5)),
                                          right=TreeNode(3)
                                          )))
print(Solution().countNodesV2(root=TreeNode(1,
                                            left=TreeNode(2,
                                                          left=TreeNode(4),
                                                          right=TreeNode(5)),
                                            right=TreeNode(3)
                                            )))
print(Solution().countNodes(root=TreeNode(1,
                                          left=TreeNode(2,
                                                        left=TreeNode(4),
                                                        right=TreeNode(5)),
                                          right=TreeNode(3,
                                                         left=TreeNode(6))
                                          )))
print(Solution().countNodesV2(root=TreeNode(1,
                                            left=TreeNode(2,
                                                          left=TreeNode(4),
                                                          right=TreeNode(5)),
                                            right=TreeNode(3,
                                                           left=TreeNode(6))
                                            )))
print(Solution().countNodes(root=TreeNode(1,
                                          left=TreeNode(2,
                                                        left=TreeNode(4),
                                                        right=TreeNode(5)),
                                          right=TreeNode(3,
                                                         left=TreeNode(6),
                                                         right=TreeNode(7))
                                          )))
print(Solution().countNodesV2(root=TreeNode(1,
                                            left=TreeNode(2,
                                                          left=TreeNode(4),
                                                          right=TreeNode(5)),
                                            right=TreeNode(3,
                                                           left=TreeNode(6),
                                                           right=TreeNode(7))
                                            )))

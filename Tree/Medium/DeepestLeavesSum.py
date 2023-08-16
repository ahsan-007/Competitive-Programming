# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        return self.getDeepestLevelSumUtil(root, 0, self.getDeepestLevel(root, 0))

    def getDeepestLevel(self, root, i):
        if not root:
            return -1
        return max(self.getDeepestLevel(root.left, i+1), i, self.getDeepestLevel(root.right, i+1))

    def getDeepestLevelSumUtil(self, root, i, deepestLevel):
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val if i == deepestLevel else 0

        return self.getDeepestLevelSumUtil(root.left, i+1, deepestLevel) + self.getDeepestLevelSumUtil(root.right, i+1, deepestLevel)


print(Solution().deepestLeavesSum(TreeNode(1,
                                           TreeNode(2,
                                                    TreeNode(4,
                                                             TreeNode(7)
                                                             ),
                                                    TreeNode(5)
                                                    ),
                                           TreeNode(3,
                                                    None,
                                                    TreeNode(6,
                                                             None,
                                                             TreeNode(8)))
                                           )
                                  )
      )

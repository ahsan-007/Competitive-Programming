# https://leetcode.com/problems/binary-tree-postorder-traversal/description /?envType=daily-question&envId=2024-08-25

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        postorder = self.postorderTraversal(root.left)
        postorder.extend(self.postorderTraversal(root.right))
        postorder.append(root.val)
        return postorder


print(Solution().postorderTraversal(root=TreeNode(1,
                                                  None,
                                                  TreeNode(2,
                                                           TreeNode(3)))))

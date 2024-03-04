# https://leetcode.com/problems/binary-tree-tilt/description/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def findTiltUtil(node):
            if not node:
                return 0, 0

            left_tilt, left_sum = findTiltUtil(node.left)
            right_tilt, right_sum = findTiltUtil(node.right)

            return left_tilt + right_tilt + abs(left_sum - right_sum), left_sum + right_sum + node.val

        tilt, _ = findTiltUtil(root)
        return tilt


print(Solution().findTilt(root=TreeNode(4,
                                        TreeNode(2,
                                                 TreeNode(3),
                                                 TreeNode(5)),
                                        TreeNode(9,
                                                 None,
                                                 TreeNode(7)))))

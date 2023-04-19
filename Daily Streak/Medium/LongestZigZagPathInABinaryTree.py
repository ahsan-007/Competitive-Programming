# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Version 2 (Optimized)
    # Time O(N), Space O(1) (ignoring function call stack)
    def longestZigZagV2(self, root: Optional[TreeNode]) -> int:
        _, _, max_length = self.longestZigZagUtil(root)
        return max_length - 1

    def longestZigZagUtil(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0, 0, 0
        _, lright, lmax = self.longestZigZagUtil(root.left)
        rleft, _, rmax = self.longestZigZagUtil(root.right)
        return lright + 1, rleft + 1, max(lmax, rmax, rleft+1 if rleft > lright else lright + 1)

    # Version 1
    # Time O(N^2) Space O(1) (ignoring function call stack)
    # Overlapping subproblems exist, time complexity can be improved by memoization
    # If memoization is used Time O(N), Space O(N)
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.zigZagLength(root, True) - 1,
                   self.zigZagLength(root, False) - 1,
                   self.longestZigZag(root.left) if root else 0,
                   self.longestZigZag(root.right) if root else 0)

    def zigZagLength(self, root, wasLeft):
        if not root:
            return 0
        return self.zigZagLength(root.right, False) + 1 if wasLeft else self.zigZagLength(root.left, True) + 1


root = TreeNode(1,
                None,
                TreeNode(1,
                         TreeNode(1),
                         TreeNode(1,
                                  TreeNode(1,
                                           None,
                                           TreeNode(1,
                                                    None,
                                                    TreeNode(1))),
                                  TreeNode(1))))

print(Solution().longestZigZag(root))
print(Solution().longestZigZagV2(root))

root = TreeNode(1,
                TreeNode(1,
                         None,
                         TreeNode(1,
                                  TreeNode(1,
                                           None,
                                           TreeNode(1)),
                                  TreeNode(1))),
                TreeNode(1))
print(Solution().longestZigZag(root))
print(Solution().longestZigZagV2(root))

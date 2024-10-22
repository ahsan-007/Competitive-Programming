# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description /?envType=daily-question&envId=2024-10-22

from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        queue = [(root, 0)]
        level_sums = []
        curr_sum = 0
        prev_level = 0

        while queue:
            node, level = queue.pop(0)
            if prev_level != level:
                level_sums.append(curr_sum)
                curr_sum = node.val
            else:
                curr_sum = curr_sum + node.val

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

            if not queue:
                level_sums.append(curr_sum)

            prev_level = level

        level_sums.sort(reverse=True)
        return level_sums[k-1] if k-1 < len(level_sums) else -1


print(
    Solution().kthLargestLevelSum(TreeNode(5,
                                           left=TreeNode(8,
                                                         TreeNode(2,
                                                                  TreeNode(4),
                                                                  TreeNode(6)),
                                                         TreeNode(1)),
                                           right=TreeNode(9,
                                                          TreeNode(3),
                                                          TreeNode(7))),
                                  k=2
                                  )
)


print(
    Solution().kthLargestLevelSum(TreeNode(1,
                                           TreeNode(2,
                                                    TreeNode(3))), k=1)
)

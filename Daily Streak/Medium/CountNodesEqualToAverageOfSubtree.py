# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=daily-question&envId=2026-09-10

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def averageOfSubtreeUtil(node):
            if not node:
                # subtree_sum, subtree_nodes_count, count
                return 0, 0, 0

            left_sum, left_nodes_count, left_count = averageOfSubtreeUtil(
                node.left)
            right_sum, right_nodes_count, right_count = averageOfSubtreeUtil(
                node.right)

            subtree_sum = left_sum + right_sum + node.val
            subtree_nodes_count = left_nodes_count + right_nodes_count + 1
            subtree_count = left_count + right_count + \
                (1 if node.val == subtree_sum//subtree_nodes_count else 0)

            return subtree_sum, subtree_nodes_count, subtree_count

        _, _, count = averageOfSubtreeUtil(root)
        return count


print(Solution().averageOfSubtree(root=TreeNode(4,
                                                TreeNode(8,
                                                         TreeNode(0),
                                                         TreeNode(1)),
                                                TreeNode(5, TreeNode(6)))))
print(Solution().averageOfSubtree(root=TreeNode(1)))

# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/?envType=daily-question&envId=2026-01-07

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def maxProductUtil(node, currSum, restSum):
            if not node:
                return 0, 0

            currSum = currSum + node.val

            leftSum, leftMaxProductSum = maxProductUtil(
                node.left, currSum, restSum)
            rightSum, rightMaxProductSum = maxProductUtil(
                node.right, currSum, restSum)

            restSum = restSum - currSum

            return leftSum + rightSum + node.val, max((currSum + (restSum - leftSum)) * leftSum, (currSum + (restSum - rightSum)) * rightSum, leftMaxProductSum, rightMaxProductSum)

        treeSum, _ = maxProductUtil(root, 0, 0)
        _, maxSum = maxProductUtil(root, 0, treeSum)

        return maxSum % (pow(10, 9) + 7)

    def maxProductV2(self, root: Optional[TreeNode]) -> int:
        def maxProductUtil(node, totalSum):
            if not node:
                return 0, 0

            leftSum, maxLeftProductSum = maxProductUtil(node.left, totalSum)
            rightSum, maxRightProductSum = maxProductUtil(node.right, totalSum)

            subtreeSum = leftSum + rightSum + node.val
            return subtreeSum, max(maxLeftProductSum, maxRightProductSum, subtreeSum * (totalSum - subtreeSum))

        totalSum, _ = maxProductUtil(root, 0)
        _, maxProductSum = maxProductUtil(root, totalSum)
        return maxProductSum % (pow(10, 9) + 7)


print(Solution().maxProduct(
    root=TreeNode(1,
                  TreeNode(2,
                           TreeNode(4),
                           TreeNode(5)),
                  TreeNode(3,
                           TreeNode(6)))
))

print(Solution().maxProduct(root=TreeNode(1,
                                          None,
                                          TreeNode(2,
                                                   TreeNode(3),
                                                   TreeNode(4,
                                                            TreeNode(5),
                                                            TreeNode(6))))))

print('-' * 100)

print(Solution().maxProductV2(
    root=TreeNode(1,
                  TreeNode(2,
                           TreeNode(4),
                           TreeNode(5)),
                  TreeNode(3,
                           TreeNode(6)))
))

print(Solution().maxProductV2(root=TreeNode(1,
                                            None,
                                            TreeNode(2,
                                                     TreeNode(3),
                                                     TreeNode(4,
                                                              TreeNode(5),
                                                              TreeNode(6))))))

# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=daily-question&envId=2026-01-06

from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        currSum = float("-inf")
        maxSumLevel = 0
        currLevel = 0
        nodes = [(root, 1)]
        while nodes:
            node, level = nodes.pop(0)
            if level == currLevel:
                currSum += node.val
            else:
                if currSum > maxSum:
                    maxSum = currSum
                    maxSumLevel = currLevel

                currLevel = level
                currSum = node.val

            if node.left:
                nodes.append((node.left, level + 1))

            if node.right:
                nodes.append((node.right, level + 1))

        if currSum > maxSum:
            maxSum = currSum
            maxSumLevel = currLevel

        return maxSumLevel


print(Solution().maxLevelSum(TreeNode(1,
                                      TreeNode(7,
                                               TreeNode(7),
                                               TreeNode(-8)),
                                      TreeNode(0))))

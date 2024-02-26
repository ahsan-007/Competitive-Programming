# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/


from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sortedArrayToBSTUtil(nums, i, j):
            if i > j:
                return None

            if i == j:
                return TreeNode(nums[i])

            mid = i + (j - i) // 2
            return TreeNode(nums[mid],
                            sortedArrayToBSTUtil(nums, i, mid - 1),
                            sortedArrayToBSTUtil(nums, mid + 1, j))

        return sortedArrayToBSTUtil(nums, 0, len(nums) - 1)

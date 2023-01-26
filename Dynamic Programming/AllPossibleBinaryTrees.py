
# https://leetcode.com/problems/all-possible-full-binary-trees/

from typing import List, Optional
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def LVR(node):
#     if node is None:
#         return
#     LVR(node.left)
#     print(node.val,' ', end='')
#     LVR(node.right)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self.allPossibleFBTUtils(n, {})

    def allPossibleFBTUtils(self, n, memo):
        if n <= 0:
            return None
        if n in memo:
            return memo[n]
        nodes_variations = []
        node = TreeNode()
        if n == 1:
            return [node]
        i = 2
        while n-i > 0:
            left = self.allPossibleFBTUtils(n - i, memo)
            right = self.allPossibleFBTUtils(i - 1, memo)
            for left_node in left:
                node.left = left_node
                for right_node in right:
                    node.right = right_node
                    nodes_variations.append(copy.deepcopy(node))
            i = i + 2
        memo[n] = nodes_variations
        return memo[n]


# class Solution:
#     def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
#         if n < 0:
#             return []
#         if n % 2 == 0:
#             return None
#         root = TreeNode()

#         if n == 1:
#             return [tree_nodes]
#         # root.left = TreeNode(0, None, None)
#         # root.right = TreeNode(0, None, None)
#         tree_nodes = []
#         self.allPossibleFBTUtil(root, n-1, tree_nodes, root)
#         return tree_nodes

#     def allPossibleFBTUtil(self, node, n, tree_nodes, root):
#         if n == 0:
#             tree_nodes.append(copy.deepcopy(root))
#             return
#         node.left = TreeNode(0, None, None)
#         node.right = TreeNode(0, None, None)
#         self.allPossibleFBTUtil(node.left, n-2, tree_nodes, root)
#         node.left.left = None
#         node.left.right = None
#         if n-2 > 0:
#             self.allPossibleFBTUtil(node.right, n-2, tree_nodes, root)

#         node.right.left = None
#         node.right.right = None

#         if n >= 4:
#             node.left.left = TreeNode(0, None, None)
#             node.left.right = TreeNode(0, None, None)
#             self.allPossibleFBTUtil(node.right, n-4, tree_nodes, root)
#         # if n == 0:
#         #     tree_nodes.append(copy.deepcopy(root))
#         #     return
#         # node.left.left = TreeNode(0, None, None)
#         # node.left.right = TreeNode(0, None, None)
#         # self.allPossibleFBTUtil(node.left, n-2, tree_nodes, root)
#         # node.left.left = None
#         # node.left.right = None

#         # node.right.left = TreeNode(0, None, None)
#         # node.right.right = TreeNode(0, None, None)
#         # self.allPossibleFBTUtil(node.right, n-2, tree_nodes, root)
#         # node.right.left = None
#         # node.right.right = None

#         # if n >= 4:
#         #     node.left.left = TreeNode(0, None, None)
#         #     node.left.right = TreeNode(0, None, None)
#         #     node.right.left = TreeNode(0, None, None)
#         #     node.right.right = TreeNode(0, None, None)
#         #     self.allPossibleFBTUtil(node.left, n-4, tree_nodes, root)
#         #     if n > 4:
#         #         self.allPossibleFBTUtil(node.right, n-4, tree_nodes, root)
#         #     node.left.left = None
#         #     node.left.right = None
#         #     node.right.left = None
#         #    node.right.right = None


# def display(tree_nodes):
#     for n in tree_nodes:
#         if n is not None:
#             print(f"({n.val}, {n.left}, {n.right}), ")
#         else:
#             print("(None), ")


# print(len(Solution().allPossibleFBT(7)))
# # class Solution:
# #     def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
# #         if n % 2 == 0:
# #             return None
# #         if n <= 3:
# #             if n == 1:
# #                 return TreeNode()
# #             else:
# #                 return TreeNode(0, TreeNode(), TreeNode())

# #     def allPossibleFBTUtil(self, n):
# #         pass


# # LVR(Solution().allPossibleFBT(3))

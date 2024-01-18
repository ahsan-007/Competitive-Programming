# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        if not root:
            return ""

        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return str(root.val) + (f"<{left}:" if left else "") + (f">{right}:" if right else "")

    def deserialize(self, data):
        root = TreeNode("")
        stack = []
        currexp = ""
        node = root
        i = 0
        while i < len(data):
            if data[i] == "<":
                if currexp:
                    node.val = int(currexp)
                node.left = TreeNode("")
                stack.append(node)
                node = node.left
                currexp = ""

            elif data[i] == ">":
                if currexp:
                    node.val = int(currexp)
                node.right = TreeNode("")
                stack.append(node)
                node = node.right
                currexp = ""

            elif data[i] == ":":
                if currexp:
                    node.val = int(currexp)
                currexp = ""
                if stack:
                    node = stack.pop()

            else:
                currexp = currexp + data[i]

            i = i + 1

        if currexp:
            node.val = int(currexp)
        return root if root.val != "" else None


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


def preorder(root):
    if not root:
        return

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")


tree = TreeNode(1,
                TreeNode(2,
                         None,
                         TreeNode(4)),
                TreeNode(3,
                         TreeNode(5,
                                  TreeNode(6),
                                  TreeNode(7))))
preorder(tree)
print()
inorder(tree)
print()
postorder(tree)
print()
print('-'*100)
serialzed_tree = Codec().serialize(tree)
print(serialzed_tree)
deserialized_tree = Codec().deserialize(serialzed_tree)

preorder(deserialized_tree)
print()
inorder(deserialized_tree)
print()
postorder(deserialized_tree)
print()


serialzed_tree = Codec().serialize(None)
deserialized_tree = Codec().deserialize(serialzed_tree)
print(deserialized_tree)
inorder(deserialized_tree)

serialzed_tree = Codec().serialize(TreeNode(1))
deserialized_tree = Codec().deserialize(serialzed_tree)
inorder(deserialized_tree)

print('-'*100)

tree = TreeNode(0,
                TreeNode(0,
                         TreeNode(0)),
                TreeNode(0,
                         None,
                         TreeNode(1,
                                  None,
                                  TreeNode(1))))
preorder(tree)
print()
inorder(tree)
print()
postorder(tree)
print()
print('-'*100)
serialzed_tree = Codec().serialize(tree)
print(serialzed_tree)
deserialized_tree = Codec().deserialize(serialzed_tree)

preorder(deserialized_tree)
print()
inorder(deserialized_tree)
print()
postorder(deserialized_tree)
print()

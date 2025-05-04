from Common.TreeNode import TreeNode


def preorder(node):
    if node is None:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)


root = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

preorder(root)

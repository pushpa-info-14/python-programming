from Common.TreeNode import TreeNode


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)


root = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

postorder(root)
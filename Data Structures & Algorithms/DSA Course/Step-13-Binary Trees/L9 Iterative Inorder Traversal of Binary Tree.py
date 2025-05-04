from Common.TreeNode import TreeNode


def inorder(root):
    res = []
    stack = []
    node = root
    while True:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            node = stack.pop()
            res.append(node.val)
            node = node.right

    return res


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

print(inorder(tree))
from Common.TreeNode import TreeNode


def postorder(root):
    res = []
    st1 = []
    st2 = []
    st1.append(root)
    while st1:
        node = st1.pop()
        st2.append(node)
        if node.left:
            st1.append(node.left)
        if node.right:
            st1.append(node.right)
    while st2:
        res.append(st2.pop().val)

    return res


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

print(postorder(tree))

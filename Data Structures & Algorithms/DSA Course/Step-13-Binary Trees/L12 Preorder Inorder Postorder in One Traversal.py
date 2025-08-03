from Common.TreeNode import TreeNode


def all_order(root):
    preorder = []
    inorder = []
    postorder = []

    st = [(root, 1)]
    while st:
        cur, num = st.pop()
        if num == 1:
            preorder.append(cur.val)
            st.append((cur, 2))
            if cur.left:
                st.append((cur.left, 1))
        elif num == 2:
            inorder.append(cur.val)
            st.append((cur, 3))
            if cur.right:
                st.append((cur.right, 1))
        else:
            postorder.append(cur.val)

    return [preorder, inorder, postorder]


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

print(all_order(tree))

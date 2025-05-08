from Common.TreeNode import TreeNode


def postorder(root):
    cur = root
    res = []
    st = []
    while cur or st:
        if cur:
            st.append(cur)
            cur = cur.left
        else:
            temp = st[-1].right
            if temp is None:
                temp = st.pop()
                res.append(temp.val)
                while st and temp == st[-1].right:
                    temp = st.pop()
                    res.append(temp.val)
            else:
                cur = temp

    return res


tree = TreeNode.build([1, 2, 3, 4, 5, 6, 7])

print(postorder(tree))

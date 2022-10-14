from binarytree import Node


# Given a binary tree root, check if it's symmetric around its center(a mirror of itself)
def are_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)


def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)


# T(n) = O(n)
# S(n) = O(logn)

root_test = Node(3)

node11 = Node(5)
node12 = Node(5)

node21 = Node(2)
node22 = Node(8)
node23 = Node(8)
node24 = Node(2)

node31 = Node(9)
node32 = Node(7)
node33 = Node(1)
node34 = Node(1)
node35 = Node(4)
node36 = Node(9)

node41 = Node(3)
node42 = Node(0)
node43 = Node(6)
node44 = Node(6)
node45 = Node(0)
node46 = Node(3)

root_test.left = node11
root_test.right = node12

node11.left = node21
node11.right = node22
node12.left = node23
node12.right = node24

node21.left = node31
node21.right = node32
node22.left = node33
node23.right = node34
node24.left = node35
node24.right = node36

node31.left = node41
node31.right = node42
node32.right = node43
node35.left = node44
node36.left = node45
node36.right = node46

print(root_test)
print(is_symmetric(root_test))
node35.val = 7
print(root_test)
print(is_symmetric(root_test))

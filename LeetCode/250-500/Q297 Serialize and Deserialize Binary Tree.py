from collections import deque
from typing import Optional

from Common.TreeNode import TreeNode


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque()
        q.append(root)
        res = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append("#")
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        splits = data.split(",")
        root = TreeNode(int(splits[0]))
        q = deque()
        q.append(root)
        i = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if splits[i] != "#":
                    node.left = TreeNode(int(splits[i]))
                    q.append(node.left)
                i += 1
                if splits[i] != "#":
                    node.right = TreeNode(int(splits[i]))
                    q.append(node.right)
                i += 1
        return root


# Your Codec object will be instantiated and called as such:
tree = TreeNode().build([1, 2, 3, None, None, 4, 5])
ser = Codec()
deser = Codec()
print(ser.serialize(tree))
ans = deser.deserialize(ser.serialize(tree))
ans.preorder_traversal()
print(ser.serialize(ans))

print(ser.serialize(None))
ans = deser.deserialize(ser.serialize(None))

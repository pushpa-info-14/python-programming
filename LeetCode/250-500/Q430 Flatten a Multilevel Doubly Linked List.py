# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def print(self):
        res = []
        res2 = []
        cur = self
        while cur.next:
            res.append(cur.val)
            cur = cur.next
        res.append(cur.val)
        tail = cur
        while tail:
            res2.append(tail.val)
            tail = tail.prev
        res2.reverse()
        print(res)
        print(res2)


from typing import Optional


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(node):
            if node is None:
                return node
            child_node = dfs(node.child)
            next_node = dfs(node.next)

            temp = node
            temp.child = None
            if child_node:
                temp.next = child_node
                while temp.next:
                    temp.next.prev = temp
                    temp = temp.next
            if next_node:
                temp.next = next_node
                next_node.prev = temp
            return node

        return dfs(head)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.prev = node1
node1.child = node3

s = Solution()
s.flatten(node1).print()

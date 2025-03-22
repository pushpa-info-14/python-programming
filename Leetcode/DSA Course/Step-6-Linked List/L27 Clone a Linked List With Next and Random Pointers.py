class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def print(self):
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)


def copy(head: ListNode):
    mp = {}
    temp = head
    while temp:
        mp[temp] = ListNode(temp.val)
        temp = temp.next
    temp = head
    while temp:
        copy_node = mp[temp]
        if temp.next:
            copy_node.next = mp[temp.next]
        if temp.random:
            copy_node.random = mp[temp.random]
        temp = temp.next
    return mp[head]


def copy2(head: ListNode):
    # 1. Insert copy nodes in between
    temp = head
    while temp:
        copy_node = ListNode(temp.val)
        copy_node.next = temp.next
        temp.next = copy_node
        temp = temp.next.next

    # 2. Connect random pointers
    temp = head
    while temp:
        copy_node = temp.next
        if temp.random:
            copy_node.random = temp.random.next
        temp = temp.next.next

    # 3. Connect next pointers
    dummy = ListNode(-1)
    res = dummy
    temp = head
    while temp:
        res.next = temp.next
        temp.next = temp.next.next
        res = res.next
        temp = temp.next
    return dummy.next


node7 = ListNode(7)
node13 = ListNode(13)
node11 = ListNode(11)
node10 = ListNode(10)
node1 = ListNode(1)
node7.next = node13
node13.next = node11
node11.next = node10
node10.next = node1

l = copy(node7)
l.print()

l = copy2(node7)
l.print()

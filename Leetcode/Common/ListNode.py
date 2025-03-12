class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)
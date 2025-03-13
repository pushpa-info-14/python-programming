class DoublyListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def print(self):
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)

    @staticmethod
    def create(nums):
        n = len(nums)
        head = DoublyListNode(nums[0])
        prev = head
        for i in range(1, n):
            temp = DoublyListNode(nums[i], None, prev)
            prev.next = temp
            prev = temp
        return head
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

    @staticmethod
    def create(nums):
        n = len(nums)
        temp = ListNode(0)
        cur = temp
        for i in range(n):
            cur.next = ListNode(nums[i])
            cur = cur.next
        return temp.next
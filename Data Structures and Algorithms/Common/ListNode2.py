class ListNode2:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

    def print(self):
        res = []
        cur = self
        while cur:
            res.append(cur.val)
            cur = cur.child
        print(res)

    @staticmethod
    def create(nums):
        n = len(nums)
        temp = ListNode2(0)
        cur = temp
        for i in range(n):
            cur.child = ListNode2(nums[i])
            cur = cur.child
        return temp.child
from Leetcode.Common.ListNode import ListNode


def check(head: ListNode):
    mp = {}
    cur = head
    while cur:
        if cur in mp:
            return True
        else:
            mp[cur] = 1
        cur = cur.next
    return False


def check2(head: ListNode):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


l = ListNode.create([1, 2, 3, 4, 5, 6, 7, 8, 9])
last = l
while last.next:
    last = last.next
last.next = l.next.next.next

print(check(l))
print(check2(l))

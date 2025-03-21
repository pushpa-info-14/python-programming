from Leetcode.Common.ListNode import ListNode


def loop_length(head: ListNode):
    mp = {}
    t = 0
    cur = head
    while cur:
        if cur in mp:
            return t - mp[cur]
        else:
            mp[cur] = t
        cur = cur.next
        t += 1
    return 0


def find_length(slow, fast):
    cnt = 0
    while fast:
        fast = fast.next
        cnt += 1
        if slow == fast:
            break
    return cnt


def loop_length2(head: ListNode):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return find_length(slow, fast)
    return 0


l = ListNode.create([1, 2, 3, 4, 5, 6, 7, 8, 9])
last = l
while last.next:
    last = last.next
last.next = l.next.next.next

print(loop_length(l))
print(loop_length2(l))
print(loop_length2(ListNode.create([1, 2, 3])))

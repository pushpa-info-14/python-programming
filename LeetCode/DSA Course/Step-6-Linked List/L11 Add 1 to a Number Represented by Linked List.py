from Leetcode.Common.ListNode import ListNode


def reverse(head: ListNode):
    prev = None
    cur = head
    while cur:
        front = cur.next
        cur.next = prev
        prev = cur
        cur = front
    return prev


def add(head: ListNode):
    head = reverse(head)

    carry = 1
    cur = head
    while cur:
        summation = cur.val + carry
        cur.val = summation % 10
        carry = summation // 10
        if carry == 0:
            break
        cur = cur.next

    head = reverse(head)
    if carry:
        head = ListNode(1, head)

    return head


def helper(head: ListNode):
    if head is None:
        return 1

    carry = helper(head.next)
    summation = head.val + carry
    head.val = summation % 10
    carry = summation // 10
    return carry


def add2(head: ListNode):
    carry = helper(head)
    if carry:
        head = ListNode(1, head)
    return head


ll = ListNode.create([9, 9, 9, 9])
ll = add(ll)
ll.print()
ll = ListNode.create([1, 9, 9, 9])
ll = add(ll)
ll.print()
ll = ListNode.create([1, 9, 9, 4])
ll = add(ll)
ll.print()

ll = ListNode.create([9, 9, 9, 9])
ll = add2(ll)
ll.print()
ll = ListNode.create([1, 9, 9, 9])
ll = add2(ll)
ll.print()
ll = ListNode.create([1, 9, 9, 4])
ll = add2(ll)
ll.print()

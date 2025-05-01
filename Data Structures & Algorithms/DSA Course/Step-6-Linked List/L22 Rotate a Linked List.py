from Leetcode.Common.ListNode import ListNode


def rotate(head: ListNode, k: int):
    if head is None or k == 0:
        return None
    cnt = 0
    tail = head
    while tail.next:
        cnt += 1
        tail = tail.next

    cnt += 1
    k = k % cnt
    if k == 0:
        return head

    # Attach the tail to head
    tail.next = head

    target = cnt - k
    temp = head
    while temp:
        target -= 1
        if target == 0:
            new_head = temp.next
            temp.next = None
            return new_head
        temp = temp.next


l = ListNode.create([1, 2, 3, 4, 5, 6, 7, 8, 9])
l = rotate(l, 2)
l.print()

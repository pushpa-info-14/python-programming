from typing import Optional

from Leetcode.Common.ListNode import ListNode


def oddEven1(head: ListNode) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    nums = []

    temp = head  # Odd
    while temp and temp.next:
        nums.append(temp.val)
        temp = temp.next.next
    if temp:
        nums.append(temp.val)

    temp = head.next  # Even
    while temp and temp.next:
        nums.append(temp.val)
        temp = temp.next.next
    if temp:
        nums.append(temp.val)

    temp = head
    i = 0
    while temp:
        temp.val = nums[i]
        temp = temp.next
        i += 1

    return head

def oddEven2(head: ListNode) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = even_head

    return head


ll = ListNode.create([1, 2, 3, 4, 5, 6, 7, 8, 9])
ll.print()
ll = oddEven1(ll)
ll.print()

ll = ListNode.create([1, 2, 3, 4, 5, 6, 7, 8, 9])
ll.print()
ll = oddEven2(ll)
ll.print()

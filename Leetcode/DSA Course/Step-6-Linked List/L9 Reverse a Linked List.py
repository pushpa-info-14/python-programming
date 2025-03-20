from Leetcode.Common.ListNode import ListNode


def reverse(head: ListNode):
    nums = []
    temp = head
    while temp:
        nums.append(temp.val)
        temp = temp.next

    temp = head
    while temp:
        temp.val = nums.pop()
        temp = temp.next

    return head


def reverse2(head: ListNode):
    prev = None
    temp = head
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev


def reverse3(head: ListNode):
    if head is None or head.next is None:
        return head
    new_head = reverse3(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head

ll = ListNode.create([1, 2, 3, 4, 5, 6])
ll = reverse(ll)
ll.print()

ll = ListNode.create([1, 2, 3, 4, 5, 6])
ll = reverse2(ll)
ll.print()

ll = ListNode.create([1, 2, 3, 4, 5, 6])
ll = reverse3(ll)
ll.print()

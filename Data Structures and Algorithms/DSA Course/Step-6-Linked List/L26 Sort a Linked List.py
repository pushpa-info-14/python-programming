from Leetcode.Common.ListNode import ListNode


def sort(head: ListNode):
    nums = []
    temp = head
    while temp:
        nums.append(temp.val)
        temp = temp.next
    nums.sort()
    i = 0
    temp = head
    while temp:
        temp.val = nums[i]
        i += 1
        temp = temp.next
    return head


def merge(head1: ListNode, head2: ListNode):
    dummy = ListNode(-1)
    temp = dummy
    temp1 = head1
    temp2 = head2
    while temp1 and temp2:
        if temp1.val < temp2.val:
            temp.next = temp1
            temp1 = temp1.next
        else:
            temp.next = temp2
            temp2 = temp2.next
        temp = temp.next
    if temp1:
        temp.next = temp1
    if temp2:
        temp.next = temp2
    return dummy.next


def find_middle(head: ListNode):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_sort(head: ListNode):
    if head is None or head.next is None:
        return head

    middle = find_middle(head)
    left_head = head
    right_head = middle.next
    middle.next = None
    left_sorted = merge_sort(left_head)
    right_sorted = merge_sort(right_head)
    return merge(left_sorted, right_sorted)


l = ListNode.create([3, 4, 2, 1, 5])
l = sort(l)
l.print()

l = ListNode.create([3, 4, 2, 1, 5])
l = merge_sort(l)
l.print()

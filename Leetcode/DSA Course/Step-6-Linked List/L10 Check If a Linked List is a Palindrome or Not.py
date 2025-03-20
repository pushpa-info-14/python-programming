from Leetcode.Common.ListNode import ListNode


def is_palindrome(head: ListNode):
    if head is None or head.next is None:
        return True

    data = []
    temp = head
    while temp:
        data.append(temp.val)
        temp = temp.next

    temp = head
    while temp:
        if temp.val != data.pop():
            return False
        temp = temp.next
    return True


def reverse(head: ListNode):
    prev = None
    temp = head
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev


def is_palindrome2(head: ListNode):
    if head is None or head.next is None:
        return True
    
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    new_head = reverse(slow.next)

    first = head
    second = new_head
    while second:
        if first.val != second.val:
            reverse(new_head)
            return False
        first = first.next
        second = second.next
    reverse(new_head)
    return True


ll = ListNode.create([1, 2, 3, 2, 1])
print(is_palindrome(ll))
ll = ListNode.create([1, 2, 3, 2, 7])
print(is_palindrome(ll))

ll = ListNode.create([1, 2, 3, 2, 1])
print(is_palindrome2(ll))
ll.print()
ll = ListNode.create([1, 2, 3, 2, 7])
print(is_palindrome2(ll))
ll.print()

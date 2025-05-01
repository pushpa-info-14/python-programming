from Leetcode.Common.DoublyListNode import DoublyListNode


def remove(head: DoublyListNode):
    temp = head
    while temp:
        front = temp.next
        while front and temp.val == front.val:
            front = front.next
        temp.next = front
        if front: front.prev = temp
        temp = temp.next
    return head


l = DoublyListNode.create([1, 1, 1, 2, 3, 3, 4])
l = remove(l)
l.print()

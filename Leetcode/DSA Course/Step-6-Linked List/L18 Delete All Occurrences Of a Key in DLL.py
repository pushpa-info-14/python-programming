from Leetcode.Common.DoublyListNode import DoublyListNode


def delete(head: DoublyListNode, key:int):
    temp = head
    while temp:
        if temp.val == key:
            if temp == head:
                head = head.next
            front = temp.next
            prev = temp.prev
            if front: front.prev = prev
            if prev: prev.next = front
            temp = front
        else:
            temp = temp.next
    return head


l = DoublyListNode.create([10,4,10,10,6,10])
l = delete(l, 10)
l.print()
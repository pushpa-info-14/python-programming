from Leetcode.Common.ListNode import ListNode


def reverse(head: ListNode):
    prev = None
    temp = head
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front


def find_kth_node(head: ListNode, k: int):
    cnt = 0
    temp = head
    while temp:
        cnt += 1
        if cnt == k:
            return temp
        temp = temp.next
    return None


def reverse_nodes(head: ListNode, k: int):
    temp = head
    prev_last = None
    while temp:
        kth_node = find_kth_node(temp, k)
        if kth_node is None:
            if prev_last:
                prev_last.next = temp
            break
        next_node = kth_node.next
        kth_node.next = None
        reverse(temp)
        if temp == head:
            head = kth_node
        else:
            prev_last.next = kth_node
        prev_last = temp
        temp = next_node
    return head


l = ListNode.create([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
l = reverse_nodes(l, 3)
l.print()

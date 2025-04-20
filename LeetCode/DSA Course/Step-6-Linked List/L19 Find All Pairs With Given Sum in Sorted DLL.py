from Leetcode.Common.DoublyListNode import DoublyListNode


def find(head: DoublyListNode, k: int):
    res = []
    temp1 = head
    while temp1:
        temp2 = temp1.next
        while temp2 and temp1.val + temp2.val <= k:
            if temp1.val + temp2.val == k:
                res.append([temp1.val, temp2.val])
            temp2 = temp2.next
        temp1 = temp1.next
    return res


def find2(head: DoublyListNode, k: int):
    res = []
    left = head
    right = head
    while right.next:
        right = right.next

    while left.val <= right.val:
        summation = left.val + right.val
        if summation == k:
            res.append([left.val, right.val])
            left = left.next
            right = right.prev
        elif summation < k:
            left = left.next
        else:
            right = right.prev
    return res


l = DoublyListNode.create([1, 2, 3, 4, 9])
print(find(l, 5))
print(find2(l, 5))

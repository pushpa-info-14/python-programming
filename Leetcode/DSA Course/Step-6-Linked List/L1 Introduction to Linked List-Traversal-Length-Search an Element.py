from Leetcode.Common.ListNode import ListNode


def createLinkedList(nums):
    n = len(nums)
    temp = ListNode(0)
    cur = temp
    for i in range(n):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return temp.next


def printLengthOfLinkedList(head: ListNode):
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    print(count)


def printLinkedList(head: ListNode):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


def search(head: ListNode, target):
    cur = head
    while cur is not None:
        if cur.val == target:
            return True
        cur = cur.next
    return False


ls = createLinkedList([1, 2, 3, 4, 5])
printLengthOfLinkedList(ls)
printLinkedList(ls)
print(search(ls, 5))
print(search(ls, 7))

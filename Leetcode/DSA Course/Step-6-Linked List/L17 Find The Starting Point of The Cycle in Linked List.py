from Leetcode.Common.ListNode import ListNode


def start(head: ListNode):
    mp = {}
    temp = head
    while temp:
        if temp in mp:
            return temp
        else:
            mp[temp] = True
        temp = temp.next
    return None


def start2(head: ListNode):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


l = ListNode.create([1, 2, 3, 4, 5, 6, 7, 8, 9])
last = l
while last.next:
    last = last.next
last.next = l.next.next.next

print(start(l).val)
print(start2(l).val)

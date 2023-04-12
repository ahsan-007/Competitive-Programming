# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n <= 0:
            return head
        fast = head
        while n and fast:
            fast = fast.next
            n = n - 1
        if fast is None:
            return head.next if n == 0 else None
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        if slow.next:
            slow.next = slow.next.next
        return head


def display(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


display(Solution().removeNthFromEnd(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5))

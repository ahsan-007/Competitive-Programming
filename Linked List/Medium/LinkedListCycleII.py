# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        first_iteration = True
        while fast and (slow != fast or first_iteration):
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if first_iteration:
                first_iteration = False

        if not fast:
            return None

        p1 = head
        p2 = slow
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


head = ListNode(3)
cycle = ListNode(2)
head.next = cycle
cycle.next = ListNode(0)
cycle.next.next = ListNode(-4)
cycle.next.next.next = cycle


print(Solution().detectCycle(head).val)

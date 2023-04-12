# https://leetcode.com/problems/linked-list-cycle/description/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if slow == fast:
                return True
        return False


head = ListNode(3)
cycle = ListNode(2)
head.next = cycle
cycle.next = ListNode(0)
cycle.next.next = ListNode(-4)
cycle.next.next.next = cycle


print(Solution().hasCycle(head))

# https://leetcode.com/problems/linked-list-cycle/?envType=daily-question&envId=2023-09-04

from typing import Optional

# Definition for singly-linked list.


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
                    return False

        return True

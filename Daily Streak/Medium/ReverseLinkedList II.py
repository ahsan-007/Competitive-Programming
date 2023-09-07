# https://leetcode.com/problems/reverse-linked-list-ii/?envType=daily-question&envId=2023-09-07

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        head = ListNode(-1, head)
        startNode = head
        i = 1
        while i < left:
            i = i + 1
            startNode = startNode.next

        prev = startNode.next
        next = prev.next if prev else None
        while i < right:
            temp = next.next
            next.next = prev
            prev = next
            next = temp
            i = i + 1

        startNode.next.next = next
        startNode.next = prev

        return head.next


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


display(Solution().reverseBetween(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4))

display(Solution().reverseBetween(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 5))

display(Solution().reverseBetween(
    ListNode(5), 1, 1))

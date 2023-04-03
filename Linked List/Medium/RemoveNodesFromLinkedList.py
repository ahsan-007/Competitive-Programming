# https://leetcode.com/problems/remove-nodes-from-linked-list/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        head.next = self.removeNodes(head.next)
        return head if head.next is None or head.val >= head.next.val else head.next


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


list1 = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
display(Solution().removeNodes(list1))

list1 = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1)))))
display(Solution().removeNodes(list1))

list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
display(Solution().removeNodes(list1))

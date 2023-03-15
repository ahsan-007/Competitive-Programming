# https://leetcode.com/problems/merge-nodes-in-between-zeros/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modified = head
        node = head
        sum = 0
        while node:
            if node.val == 0 and sum != 0:
                modified.next = ListNode(sum)
                sum = 0
                modified = modified.next
            sum = sum + node.val
            node = node.next
        return head.next


def display(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


head = ListNode(0, ListNode(3, ListNode(1, ListNode(
    0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
display(head)
display(Solution().mergeNodes(head))


head = ListNode(0, ListNode(1, ListNode(0, ListNode(
    3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
display(head)
display(Solution().mergeNodes(head))

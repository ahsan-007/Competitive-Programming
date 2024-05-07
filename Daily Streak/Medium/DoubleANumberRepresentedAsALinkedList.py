
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def doubleItUtil(node, num):
            if not node:
                return num * 2

            doubled = doubleItUtil(node.next, num * 10 + node.val)
            node.val = doubled % 10
            return doubled // 10

        doubled = doubleItUtil(head, 0)
        return head if not doubled else ListNode(doubled, head)


def display(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


display(Solution().doubleIt(head=ListNode(1, ListNode(8, ListNode(9)))))
display(Solution().doubleIt(head=ListNode(9, ListNode(9, ListNode(9)))))

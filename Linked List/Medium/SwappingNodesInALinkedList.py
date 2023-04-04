# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 0:
            return
        kth_node = head
        k = k - 1
        while k and kth_node:
            kth_node = kth_node.next
            k = k - 1

        if not kth_node:
            return

        node = kth_node.next
        prev = head
        while node:
            node = node.next
            prev = prev.next

        prev.val, kth_node.val = kth_node.val, prev.val
        return head


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
display(list1)
Solution().swapNodes(list1, 2)
display(list1)

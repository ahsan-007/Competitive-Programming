# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front = head
        i = 1
        while front and i < k:
            front = front.next
            i = i + 1

        end = head
        p = front
        while p.next:
            p = p.next
            end = end.next

        front.val, end.val = end.val, front.val
        return head


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


ls = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5)))))
display(Solution().swapNodes(head=ls, k=2))
ls = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5)))))
display(Solution().swapNodes(head=ls, k=3))

ls = ListNode(7, ListNode(9, ListNode(
    6, ListNode(6, ListNode(7, ListNode(8, ListNode(3, ListNode(0, ListNode(9, ListNode(5))))))))))
display(Solution().swapNodes(head=ls, k=2))

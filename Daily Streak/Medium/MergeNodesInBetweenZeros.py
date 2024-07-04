# https://leetcode.com/problems/merge-nodes-in-between-zeros/description /?envType=daily-question&envId=2024-07-04

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mergedHead = head
        while head and head.next:
            if head.next.val != 0:
                head.val = head.val + head.next.val
                head.next = head.next.next
            else:
                if head.next.next:
                    head = head.next
                else:
                    head.next = None
        return mergedHead


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


test1 = ListNode(0, ListNode(3, ListNode(
    1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
display(test1)
display(Solution().mergeNodes(test1))

test2 = ListNode(0, ListNode(1, ListNode(0, ListNode(
    3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
display(test2)
display(Solution().mergeNodes(test2))

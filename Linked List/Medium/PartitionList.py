# https://leetcode.com/problems/partition-list/


from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftHead = leftP = None
        head = ListNode(-1, head)
        p = head
        while p.next:
            if p.next.val < x:
                if leftP:
                    leftP.next = p.next
                    leftP = leftP.next
                else:
                    leftHead = leftP = p.next
                p.next = p.next.next
            else:
                p = p.next

        if leftHead:
            leftP.next = head.next
            return leftHead

        return head.next


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


# display(Solution().partition(None, 1))
display(Solution().partition(ListNode(1, ListNode(
    4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3))
display(Solution().partition(ListNode(1, ListNode(
    4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 8))

# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return

        odd = oddP = head
        even = evenP = head.next

        while evenP:
            oddP.next = evenP.next
            if oddP.next:
                evenP.next = oddP.next.next
                oddP = oddP.next
            evenP = evenP.next

        oddP.next = even
        return odd


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


display(Solution().oddEvenList(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
display(Solution().oddEvenList(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))
display(Solution().oddEvenList(
    ListNode(1, ListNode(2, ListNode(3)))))

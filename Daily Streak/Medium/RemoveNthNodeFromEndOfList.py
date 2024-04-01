# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=daily-question&envId=2024-03-03


from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        offset = head
        while n > 0 and offset:
            offset = offset.next
            n = n - 1

        if not offset:
            return head.next

        p = head
        while offset.next:
            offset = offset.next
            p = p.next

        p.next = p.next.next
        return head


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


display(Solution().removeNthFromEnd(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1))
display(Solution().removeNthFromEnd(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))
display(Solution().removeNthFromEnd(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3))
display(Solution().removeNthFromEnd(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 4))
display(Solution().removeNthFromEnd(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5))

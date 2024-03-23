# https://leetcode.com/problems/reorder-list/description/?envType=daily-question&envId=2024-03-23

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        _, reversed_second_half = self.reverse(mid.next)
        mid.next = None
        p = head
        next_node = p.next
        while reversed_second_half:
            p.next = reversed_second_half
            reversed_second_half = reversed_second_half.next
            p.next.next = next_node
            p = next_node
            if p:
                next_node = p.next
        return head

    def reverse(self, head):
        if not head.next:
            return head, head
        reversed_list, new_head = self.reverse(head.next)
        reversed_list.next = head
        head.next = None
        return head, new_head

    def findMid(self, head):
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def display(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


display(Solution().reorderList(head=ListNode(
    1, ListNode(2, ListNode(3, ListNode(4))))))

display(Solution().reorderList(head=ListNode(
    1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

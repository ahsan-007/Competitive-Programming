# https://leetcode.com/problems/reverse-linked-list/description/?envType=daily-question&envId=2024-03-21

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev_node = None
        while node:
            temp = node.next
            node.next = prev_node
            prev_node = node
            node = temp

        return prev_node

    def reverseListV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            if not node:
                return
            next = reverse(node.next)
            if next:
                next.next = node
            else:
                nonlocal head
                head = node
            node.next = None
            return node
        reverse(head)
        return head


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


display(Solution().reverseList(head=ListNode(
    1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
display(Solution().reverseList(head=ListNode(1, ListNode(2, ListNode(3)))))
display(Solution().reverseList(head=ListNode(1, ListNode(2))))
display(Solution().reverseList(head=ListNode(1)))

print('-'*100)

display(Solution().reverseListV2(head=ListNode(
    1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
display(Solution().reverseListV2(head=ListNode(1, ListNode(2, ListNode(3)))))
display(Solution().reverseListV2(head=ListNode(1, ListNode(2))))
display(Solution().reverseListV2(head=ListNode(1)))

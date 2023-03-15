# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        middle = self.findMiddle(head)

        head2 = middle.next
        middle.next = None
        _, reversed = self.reverse(head2)

        max_sum = self.findMaxSum(head, reversed)

        self.reverse(reversed)
        middle.next = head2

        return max_sum

    def findMaxSum(self, head1, head2):
        max_sum = None
        while head1:
            max_sum = max(max_sum, head1.val +
                          head2.val) if max_sum else head1.val + head2.val
            head1 = head1.next
            head2 = head2.next
        return max_sum

    def findMiddle(self, head):
        slow = fast = head
        while fast == head or fast:
            fast = fast.next
            if fast:
                fast = fast.next
            if fast:
                slow = slow.next
        return slow

    def reverse(self, node):
        if node.next is None:
            return node, node
        reversed, head = self.reverse(node.next)
        node.next = None
        reversed.next = node
        return node, head

    def display(self, node):
        while node:
            print(node.val, end=' ')
            node = node.next
        print()


head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
print(Solution().pairSum(head))

head = ListNode(1, ListNode(1000))
print(Solution().pairSum(head))

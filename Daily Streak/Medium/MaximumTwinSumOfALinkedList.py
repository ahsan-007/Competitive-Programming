# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Recursive
    def pairSum(self, head: Optional[ListNode]) -> int:
        middle = self.findMiddle(head)
        _, max_sum = self.maxSum(head, middle.next)
        return max_sum

    def maxSum(self, list1, list2):
        if not list2:
            return list1, 0
        head, max_sum = self.maxSum(list1, list2.next)
        return head.next, max(max_sum, head.val + list2.val)

    # Iteartive
    def pairSumV2(self, head: Optional[ListNode]) -> int:
        middle = self.findMiddle(head)

        _, list2_reversed = self.reverse(middle.next)
        middle.next = None

        max_sum = self.findMaxPairSum(head, list2_reversed)

        _, list2 = self.reverse(list2_reversed)
        middle.next = list2

        return max_sum

    def findMaxPairSum(self, head1, head2):
        max_sum = 0
        while head1:
            max_sum = max(max_sum, head1.val+head2.val)
            head1 = head1.next
            head2 = head2.next
        return max_sum

    # Utilities
    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        if not head or not head.next:
            return head, head
        reversed, reversed_head = self.reverse(head.next)
        reversed.next = head
        head.next = None
        return head, reversed_head


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


print(Solution().pairSum(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
print(Solution().pairSum(ListNode(12, ListNode(
    1, ListNode(31, ListNode(14, ListNode(6, ListNode(9))))))))

print(Solution().pairSumV2(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
print(Solution().pairSumV2(ListNode(12, ListNode(
    1, ListNode(31, ListNode(14, ListNode(6, ListNode(9))))))))
print(Solution().pairSumV2(ListNode(12, ListNode(100))))

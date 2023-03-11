# https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Approach 1
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)

        while lengthA > lengthB:
            headA = headA.next
            lengthA = lengthA - 1

        while lengthB > lengthA:
            headB = headB.next
            lengthB = lengthB - 1

        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

    def getLength(self, head):
        i = 0
        while head:
            i += 1
            head = head.next
        return i

    # Approach 2
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB
        while node1 != node2:
            node1 = node1.next if node1.next else headB
            node2 = node2.next if node2.next else headA
        return node1

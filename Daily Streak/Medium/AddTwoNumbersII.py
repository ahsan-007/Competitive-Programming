# https://leetcode.com/problems/add-two-numbers-ii/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length1 = self.length(l1)
        length2 = self.length(l2)
        if length1 < length2:
            l1, l2 = l2, l1
            length1, length2 = length2, length1

        carry, sum_list = self.addTwoNumbersUtil(l1, l2, length1 - length2)
        return sum_list if carry == 0 else ListNode(carry, sum_list)

    def addTwoNumbersUtil(self, l1, l2, diff):
        if diff != 0:
            carry, list = self.addTwoNumbersUtil(l1.next, l2, diff-1)
            sum_val = l1.val + carry
            list = ListNode(sum_val % 10, list)
            return sum_val // 10, list
        return self.addEqualDigitList(l1, l2)

    def addEqualDigitList(self, l1, l2):
        carry, list = 0, None
        if l1:
            carry, list = self.addEqualDigitList(l1.next, l2.next)
            sum_val = l1.val + l2.val + carry
            list = ListNode(sum_val % 10, list)
            carry = sum_val // 10
        return carry, list

    def length(self, node):
        count = 0
        while node:
            count = count + 1
            node = node.next
        return count


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


display(Solution().addTwoNumbers(ListNode(7, ListNode(
    2, ListNode(4, ListNode(3)))), ListNode(5, ListNode(6, ListNode(4)))))

display(Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4)))))

display(Solution().addTwoNumbers(ListNode(0), ListNode(0)))

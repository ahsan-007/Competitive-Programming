# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return 0
        decimal, _ = self.convertToInt(head)
        return decimal

    def getDecimalValueV2(self, head: ListNode) -> int:
        decimal = 0
        while head:
            decimal = decimal * 2 + head.val
            head = head.next
        return decimal

    def convertToInt(self, node):
        if node.next is None:
            return node.val, 0
        res, exp = self.convertToInt(node.next)
        return res + node.val * pow(2, exp + 1), exp + 1


head = ListNode(1, ListNode(0, ListNode(1)))
print(Solution().getDecimalValue(head))
print(Solution().getDecimalValueV2(head))

head = ListNode(1, ListNode(0, ListNode(1, ListNode(0))))
print(Solution().getDecimalValue(head))
print(Solution().getDecimalValueV2(head))

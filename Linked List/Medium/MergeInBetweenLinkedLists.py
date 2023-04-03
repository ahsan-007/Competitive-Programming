# https://leetcode.com/problems/merge-in-between-linked-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p = list1
        count = 0
        if a != 0:
            while count != a - 1:
                count = count + 1
                p = p.next

        q = p
        while count != b:
            count = count + 1
            q = q.next

        if a != 0:
            p.next = list2

        p = list2
        while p.next:
            p = p.next

        p.next = q.next

        return list1 if a != 0 else list2


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


list1 = ListNode(0, ListNode(1, ListNode(
    2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))

list2 = ListNode(9, ListNode(8, ListNode(7)))
display(list1)
display(list2)
display(Solution().mergeInBetween(list1, 2, 6, list2))

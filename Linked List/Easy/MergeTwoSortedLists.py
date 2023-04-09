# https://leetcode.com/problems/merge-two-sorted-lists/


from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        p = head

        while list1 and list2:
            if list1.val > list2.val:
                p.next = list2
                list2 = list2.next
            else:
                p.next = list1
                list1 = list1.next
            p = p.next

        p.next = list1 if list1 else list2
        return head.next


def display(head):
    while (head):
        print(head.val, end=' ')
        head = head.next
    print()


display(Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))),
        ListNode(1, ListNode(3, ListNode(4)))))

display(Solution().mergeTwoLists(None, None))

display(Solution().mergeTwoLists(None, ListNode(0)))

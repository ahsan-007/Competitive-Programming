# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2025-11-01

from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        head = ListNode(-1, head)
        p = head
        while p.next:
            if p.next.val in nums:
                p.next = p.next.next
            else:
                p = p.next
        return head.next


def toList(nums):
    head = None
    tail = None
    for num in nums:
        if not head:
            head = tail = ListNode(num)
        else:
            tail.next = ListNode(num)
            tail = tail.next
    return head


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next


display(Solution().modifiedList(nums=[1, 2, 3], head=toList([1, 2, 3, 4, 5])))

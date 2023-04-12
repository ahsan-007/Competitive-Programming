# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list = ListNode(-1)
        p = sorted_list
        while lists:
            i = -1
            for j in range(len(lists)):
                if lists[j] and (i == -1 or lists[j].val < lists[i].val):
                    i = j
            if i != -1:
                p.next = lists[i]
                p = p.next
                lists[i] = lists[i].next
            if lists[i] is None:
                del lists[i]
        return sorted_list.next


def display(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


list1 = ListNode(1, ListNode(4, ListNode(7, ListNode(10))))
list2 = ListNode(2, ListNode(5, ListNode(8, ListNode(11))))
list3 = ListNode(3, ListNode(6, ListNode(9, ListNode(12))))

display(Solution().mergeKLists([list1, list2, list3]))

display(Solution().mergeKLists([None, ListNode(1)]))

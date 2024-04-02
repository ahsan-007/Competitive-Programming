# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/?envType=daily-question&envId=2024-03-12

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(None, head)
        map = {0: newHead}
        runningSum = 0
        while head:
            runningSum = runningSum + head.val
            if runningSum in map:
                p = map[runningSum].next
                currSum = runningSum
                while p != head:
                    currSum = currSum + p.val
                    del map[currSum]
                    p = p.next

                map[runningSum].next = head.next

            else:
                map[runningSum] = head
            head = head.next
        return newHead.next

    def removeZeroSumSublistsV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0, head)
        map = {}
        runningSum = 0
        p = newHead
        while p:
            runningSum = runningSum + p.val
            map[runningSum] = p
            p = p.next

        runningSum = 0
        p = newHead
        while p:
            runningSum = runningSum + p.val
            p.next = map[runningSum].next
            p = p.next

        return newHead.next


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next

    print()


list1 = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))
list2 = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(4)))))
list3 = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(-2)))))
list4 = ListNode(1, ListNode(-1))

display(Solution().removeZeroSumSublists(list1))
display(Solution().removeZeroSumSublists(list2))
display(Solution().removeZeroSumSublists(list3))
display(Solution().removeZeroSumSublists(list4))

print('-' * 100)

display(Solution().removeZeroSumSublistsV2(list1))
display(Solution().removeZeroSumSublistsV2(list2))
display(Solution().removeZeroSumSublistsV2(list3))
display(Solution().removeZeroSumSublistsV2(list4))

# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description /?envType=daily-question&envId=2024-07-05

from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        distance = [-1, -1]

        def findMaxDistance(head):
            firstMinimaMaxima = None
            lastMinimaMaxima = None
            i = 0
            while head:
                if head.next and head.next.next and ((head.next.val < head.val and head.next.val < head.next.next.val) or (head.next.val > head.val and head.next.val > head.next.next.val)):
                    if firstMinimaMaxima is not None:
                        distance[1] = (i + 1) - firstMinimaMaxima
                    else:
                        firstMinimaMaxima = i + 1

                    if lastMinimaMaxima is not None:
                        distance[0] = min(
                            distance[0], (i + 1) - lastMinimaMaxima) if distance[0] > -1 else ((i + 1) - lastMinimaMaxima)
                    lastMinimaMaxima = i + 1
                head = head.next
                i = i + 1
            return distance

        return findMaxDistance(head)


print(Solution().nodesBetweenCriticalPoints(ListNode(3, ListNode(1))))
print(Solution().nodesBetweenCriticalPoints(head=ListNode(5, ListNode(
    3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))))

print(Solution().nodesBetweenCriticalPoints(
    ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode()))))))
print(Solution().nodesBetweenCriticalPoints(ListNode(6, ListNode(8, ListNode(
    4, ListNode(1, ListNode(9, ListNode(6, ListNode(6, ListNode(10, ListNode(6)))))))))))
[6, 8, 4, 1, 9, 6, 6, 10, 6]

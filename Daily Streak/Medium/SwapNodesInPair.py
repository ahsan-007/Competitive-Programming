# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Iterative
    def swapPairs(self, head):
        head = ListNode(-1, head)
        curr = head
        while curr and curr.next and curr.next.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = curr.next.next
            curr.next.next = temp
            curr = curr.next.next
        return head.next

    # Recursive
    def swapPairsV2(self, head):
        if not head or not head.next:
            return head
        swapped_head = self.swapPairsV2(head.next.next)
        head.next.next = head
        newHead = head.next
        head.next = swapped_head
        return newHead


def display(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


display(Solution().swapPairs(head=ListNode(
    1, ListNode(2, ListNode(3, ListNode(4))))))

display(Solution().swapPairs(head=ListNode(
    1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

display(Solution().swapPairs(head=ListNode(1, ListNode(2))))

display(Solution().swapPairs(head=ListNode(1)))


display(Solution().swapPairsV2(head=ListNode(
    1, ListNode(2, ListNode(3, ListNode(4))))))

display(Solution().swapPairsV2(head=ListNode(
    1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))

display(Solution().swapPairsV2(head=ListNode(1, ListNode(2))))

display(Solution().swapPairsV2(head=ListNode(1)))

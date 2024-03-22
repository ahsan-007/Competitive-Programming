# https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-03-22


from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            next = node
            prev = None
            while next:
                temp = next.next
                next.next = prev
                prev = next
                next = temp
            return prev

        if not head:
            return True

        if not head.next:
            return False

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed = reverse(slow.next if fast else slow)

        while head != slow:
            if head.val != reversed.val:
                return False
            head = head.next
            reversed = reversed.next

        return True


print(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
print(Solution().isPalindrome(
    ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))))

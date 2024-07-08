# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/?envType=daily-question&envId=2024-07-08

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        class ListNode:
            def __init__(self, val, next=None) -> None:
                self.val = val
                self.next = next

        if k == 1:
            return n

        head = None
        p = None
        for i in range(1, n + 1):
            if not head:
                head = ListNode(i)
                p = head
            else:
                p.next = ListNode(i)
                p = p.next
        p.next = head

        p = head
        i = 1
        while p.next:
            if i + 1 == k:
                p.next = p.next.next
                p = p.next
                i = 1
                if p.next == p:
                    p.next = None
            else:
                i = i + 1
                p = p.next
        return p.val


print(Solution().findTheWinner(5, 2))
print(Solution().findTheWinner(6, 5))

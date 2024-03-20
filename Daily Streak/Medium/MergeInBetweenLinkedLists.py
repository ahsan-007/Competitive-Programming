# https://leetcode.com/problems/merge-in-between-linked-lists/?envType=daily-question&envId=2024-03-20

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next

        if a != 0:
            i = 1
            list1_node = list1
            while i < a:
                list1_node = list1_node.next
                i = i + 1

            list1_node_backup = list1_node.next
            list1_node.next = list2
        else:
            list1_node_backup = list1
            list1 = list2
            i = 1

        i = i - 1
        while i < b and list1_node_backup:
            list1_node_backup = list1_node_backup.next
            i = i + 1
        list2_tail.next = list1_node_backup
        return list1


def display(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()


list1 = ListNode(10, ListNode(1, ListNode(
    13, ListNode(6, ListNode(9, ListNode(5))))))
list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))

display(list1)
display(list2)
display(Solution().mergeInBetween(list1=list1, a=3, b=4, list2=list2))

print('-'*100)
list1 = ListNode(10, ListNode(1, ListNode(
    13, ListNode(6, ListNode(9, ListNode(5))))))
list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
display(list1)
display(list2)
display(Solution().mergeInBetween(list1=list1, a=1, b=4, list2=list2))

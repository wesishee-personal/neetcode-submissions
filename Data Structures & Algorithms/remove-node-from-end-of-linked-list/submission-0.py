# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode("hodor", head)

        left = dummy_node
        right = dummy_node.next
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            print(f"right.next = {right.next}")
            left = left.next
            right = right.next
        print(left.val)
        left.next = left.next.next if left.next and left.next.next else None
        return dummy_node.next

        
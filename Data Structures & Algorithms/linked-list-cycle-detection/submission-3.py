# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        slow and fast pointer
        fast increments by 2
        slow by 1, if fast == slow, then theres a cycle
        if fast.next.next == None then return
        '''
        if head == None or head.next == None:
            return False

        slow,fast = head, head.next.next

        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next 

        return False

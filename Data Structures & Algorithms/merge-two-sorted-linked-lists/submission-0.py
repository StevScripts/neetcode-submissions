# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        combined = start = ListNode(0)


        
        while list1 and list2:
            if list1.val <= list2.val:
                combined.next = list1
                combined = combined.next
                list1 = list1.next
            else:
                combined.next = list2
                combined = combined.next
                list2 = list2.next


        if list1 is None:
            combined.next = list2
        else:
            combined.next = list1
            
            
                
            
        return start.next
                
            
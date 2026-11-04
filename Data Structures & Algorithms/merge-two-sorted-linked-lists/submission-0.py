# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()  
        p3 = list3
        p1, p2 = list1, list2 
        while(p1 and p2): 
            if (p1.val < p2.val): 
                p1_next = p1.next
                p1.next = None
                p3.next = p1
                p1 = p1_next
                p3 = p3.next 
            elif (p2.val < p1.val): 
                p2_next = p2.next
                p2.next = None
                p3.next = p2
                p2 = p2_next
                p3 = p3.next 
            else: # Equal val
                p1_next = p1.next 
                p2_next = p2.next 
                p1.next, p2.next = None, None 
                p3.next = p1 
                p3.next.next = p2 
                p3 = p2
                p1 = p1_next
                p2 = p2_next
        while(p1): 
            p1_next = p1.next
            p1.next = None
            p3.next = p1
            p1 = p1_next
            p3 = p3.next 
        while(p2): 
            p2_next = p2.next
            p2.next = None
            p3.next = p2
            p2 = p2_next
            p3 = p3.next 
        return list3.next


                


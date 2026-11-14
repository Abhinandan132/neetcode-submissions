# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        # Naive Approach, get the size of the LL. 
        curr = head 
        nodes = [] 
        while(curr): 
            nodes.append(curr) 
            curr = curr.next 
        sz = len(nodes) 
        if (n == sz): return head.next
        to_remove = sz - n 
        nodes[to_remove - 1].next = nodes[to_remove].next 
        nodes[to_remove].next = None 
        return head


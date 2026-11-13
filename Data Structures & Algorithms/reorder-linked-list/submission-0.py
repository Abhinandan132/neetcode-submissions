# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head 
        nodes = [] 
        while(curr): 
            nodes.append(curr) 
            curr = curr.next 
        f, l = 0, len(nodes) - 1
        while(f < l): 
            nodes[f].next = nodes[l] 
            f += 1
            if (f == l): break
            nodes[l].next = nodes[f] 
            l -= 1
        nodes[f].next = None 
        

            

            
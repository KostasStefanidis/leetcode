from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next
    
    def __repr__(self) -> str:
        list = []
        next_node = self
        
        while(next_node is not None):
            list.append(next_node.val)
            next_node = next_node.next
        return str(list)
    
    def __str__(self) -> str:
        return self.__repr__()

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        values_found = []
        
        node = head
        
        while node:
            if node.val not in values_found:
                values_found.append(node.val)
            
            if node.next is not None and node.val == node.next.val:
                node.next = node.next.next 
                
            node = node.next
                
        values_found.sort(reverse=True)
        
        for i, elem in enumerate(values_found, start=0):
            if i == 0:
                result = ListNode(elem)
            else:
                result = ListNode(elem, result)
        
        return result
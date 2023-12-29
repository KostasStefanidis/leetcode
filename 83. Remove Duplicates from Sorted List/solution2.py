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
        if not head or not head.next:
            return head
        
        head.next = self.deleteDuplicates(head.next)
        
        if head.val == head.next.val:
            return head.next
        else:
            return head
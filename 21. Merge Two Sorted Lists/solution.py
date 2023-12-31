from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next
    
    def __str__(self) -> str:
        list = []
        next_node = self
        
        while(next_node is not None):
            list.append(next_node.val)
            next_node = next_node.next
        return str(list)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        
        stack = []
        
        while(list1):
            stack.append(list1.val)
            list1 = list1.next
        
        while(list2):
            stack.append(list2.val)
            list2 = list2.next
        
        stack.sort(reverse=True)
        
        for i, elem in enumerate(stack, start=0):
            if i == 0:
                result = ListNode(elem)
            else:
                result = ListNode(elem, result)
        
        return result
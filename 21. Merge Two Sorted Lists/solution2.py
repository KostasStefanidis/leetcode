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
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:   
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
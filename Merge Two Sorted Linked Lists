# QUESTION: Merge Two Sorted Linked Lists

# Code with explanation->

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = start = ListNode() # tail is used to append from both lists while start is used as the placeholder keeping the head of the new list pointed at. Start has a value of 0 and the next is pointing at None.

        while list1 and list2: # The case where both lists aren't empty 
            if list1.val < list2.val: # compares the values of the current nodes in list1 and list2
                tail.next = list1 # now the tail's next is that list1's head which means that the whole head got appended to the start node
                list1 = list1.next # now the list1's head will change and it will move to the next head
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next # anyone the tail will keep on moving to append all the required nodes

# This is the case when only 1 of the list is empty

        if list1: 
            tail.next = list1
        elif list2:                
            tail.next = list2

        return start.next # Returning the next of the head of the final list node as the 1st node is initialized from 0 which isnt required.
        
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1 
        
        #using a dummy node as head 

        dummy = ListNode()
        result = dummy

        while list1 and list2:

            #compare for smaller value 
            if list2.val <= list1.val:
                #store the future head of list2
                future2 = list2.next 
                #assign the list2 to the dummy head
                dummy.next = list2
                #disconnect the list2 head from its rest
                list2.next = None 
                #the new dummy head is the head of list2
                dummy = list2 
                #assign the new head of list2 
                list2 = future2
            else:
                future1 = list1.next 
                dummy.next = list1
                list1.next = None
                dummy = list1
                list1 = future1
        
        dummy.next = list1 if list1 else list2
        return result.next
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #use the hare and tortoise algo: 
        #the hare would catch up the tortoise if the linked list has a cycle
        #the hare is twice as fast as tortoise, so eventually it will catach up
        hare = head.next.next if head.next else None
        tortoise = head

        #if the linked list has no cycle , the hare would be none and terminate the loop
        #if the linked list has cycle , the hare and tortoise would have same value
        while tortoise and hare:
            if tortoise.val == hare.val:
                return True
            tortoise = tortoise.next
            hare = hare.next.next if hare.next else None
        return False
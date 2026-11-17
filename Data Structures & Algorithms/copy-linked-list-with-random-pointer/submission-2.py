"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #one pass to create all the nodes instance mappings
        #one pass to construct the node sequences as original

        #hashmap to contain all the created nodes , initialise none to none mapping
        #as the random pointer could point to None
        nodes = {None : None}

        #create all the nodes mapping
        start = head
        while start:
            newNode = Node(start.val)
            nodes[start] = newNode
            start = start.next
        #use the mapping to construct the sequence
        start = head
        while start:
            node = nodes[start]
            nextt = nodes[start.next]
            random = nodes[start.random]
            node.next = nextt
            node.random = random
            start = start.next
        #nodes[head] is the start 
        return nodes[head]



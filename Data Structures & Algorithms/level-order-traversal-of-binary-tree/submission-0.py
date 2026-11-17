# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        #start with the root 
        nodes = deque([root])
        res  = [[root.val]]
        #temp array for storing the next level nodes
        temp = []
        #temp array for storing the vales
        vals = []

        #expand until there is no more nodes left
        while nodes:
            #get the current node to expand from left to right
            node = nodes.popleft()

            #add the left and right node of the current node to future expansion
            if node.left:
                temp.append(node.left)
                vals.append(node.left.val)
            if node.right:
                temp.append(node.right)
                vals.append(node.right.val)
            
            if not nodes:
                if temp:
                    nodes.extend(temp)
                    res.append(vals)
                    vals = []
                    temp = []
        return res




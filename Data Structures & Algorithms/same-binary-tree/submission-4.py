# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #start exploring each tree at the same node together 
        # check value or if the node is None 
        #when both nodes are none it means the tree ended on that side 

        #base case both termiantes 
        if not p and not q: 
            return True

        #recursively calls their left and right branches 
        if (p and q) and (p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False 
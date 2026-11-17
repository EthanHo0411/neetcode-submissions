# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        #base case 
        if not root:
            return None 
        #using the property of BST 
        #both are on the left branch 
        if max(p.val, q.val) < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            #they are separate on each branch 
            return root
        
        
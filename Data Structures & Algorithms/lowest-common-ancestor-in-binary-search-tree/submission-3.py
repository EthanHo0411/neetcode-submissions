# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root):
            #assume we are on the subtree with the p or q
            #base case
            if not root:
                return None
            
            #if the root is p or q , return root
            if root.val == p.val or root.val == q.val:
                return root
            
            #check the subtree
            left = dfs(root.left)
            right = dfs(root.right)

            #if both are present then its the root
            if left and right:
                return root
            #else it must be left or right
            return left if left else right
        
        #eliminate half the search space
        if not root:
            return None
        if max(p.val,q.val) <root.val:
            return dfs(root.left)
        elif min(p.val,q.val) >root.val:
            return dfs(root.right)
        else:
            return root
            
        

            
